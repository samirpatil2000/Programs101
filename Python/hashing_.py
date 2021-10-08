from random import randint
from datetime import datetime

import hashlib



unique_request = '{}{}'.format(randint(1000,9999),datetime.now())
unique_request="samirpatil"
print(unique_request)
uid=hashlib.md5(unique_request.encode())
print(uid)
uid= uid.hexdigest()
print(uid)