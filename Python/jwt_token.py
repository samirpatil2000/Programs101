import jwt
import datetime

secret_key = 'YOUR_SECRET_KEY'

def create_jwt(payload, ttl_seconds=3600):
    # payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=ttl_seconds)
    return jwt.encode(payload, secret_key, algorithm='HS256')

def decode_jwt(jwt_token):
    return jwt.decode(jwt_token, secret_key, algorithms=['HS256'])

payload = {"phone_number": "+919730614299", "user_id": "ertty-rtrt-fdggf-fdgfg"}

token = create_jwt(payload, secret_key)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
print(decode_jwt(token))