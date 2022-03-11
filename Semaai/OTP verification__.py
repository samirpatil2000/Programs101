
class OtpVerify(models.Model):
    EMAIL_MODE = 0
    PHONE_MODE = 1
    MODES = (
        (EMAIL_MODE, 'Email'),
        {PHONE_MODE, 'Phone'}
    )

    mode = models.SmallIntegerField(choices=MODES)
    email = models.EmailField(unique=True, blank=True, null=True)
    country_code = models.CharField(max_length=4, choices=PHONE_CODE_CHOICES)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    otp = models.CharField(max_length=10, default="000000")
    num_sends = models.SmallIntegerField(default=0)
    attempts = models.SmallIntegerField(default=0)

    MAX_SENDS = 10
    MAX_ATTEMPTS = 5

    # ----- OTP GENERATION -------------

    @staticmethod
    def _generate_otp_string(num_digits=6):
        otp = 0
        while otp < 10 ** (num_digits - 1):
            otp = floor(random() * 10 ** num_digits)
        return str(otp)

    def generate_otp(self):
        if self.num_sends >= self.MAX_SENDS:
            # TODO Error
            return

        self.otp = self._generate_otp_string()
        self.num_sends += 1
        self.save()

        print(self.otp)

    @classmethod
    def generate_phone_otp(cls, phone, country_code="91"):
        try:
            obj = cls.objects.get(phone=phone, country_code=country_code)
        except cls.DoesNotExist:
            obj = cls.objects.create(
                mode=cls.PHONE_MODE,
                phone=phone,
                country_code=country_code
            )

        obj.generate_otp()

    @classmethod
    def generate_email_otp(cls, email):
        try:
            obj = cls.objects.get(email=email)
        except cls.DoesNotExist:
            obj = cls.objects.create(
                mode=cls.EMAIL_MODE,
                email=email,
            )

        obj.generate_otp()

    # ----- OTP VALIDATION -------------
    @classmethod
    def encoded(cls, payload):
        # TODO encode time validity
        return jwt.encode(payload, SECRET_KEY, algorithms="HS256")

    @classmethod
    def decode_token(cls, token):
        # TODO check time validity
        return jwt.decode(token, SECRET_KEY, algorithms="HS256")

    @classmethod
    def verify_email_otp(cls, otp, email):
        try:
            obj = cls.objects.get(email=email)
            if obj.otp == otp:
                obj.delete()
                return cls.encoded(dict(email=email))
            return False
        except cls.DoesNotExist:
            return False

    @classmethod
    def verify_phone_otp(cls, otp, phone, country_code="91"):
        try:
            obj = cls.objects.get(phone=phone, country_code=country_code)
            if obj.otp == otp:
                obj.delete()
                return cls.encoded(dict(phone=phone, country_code=country_code))
            return False
        except cls.DoesNotExist:
            return False
