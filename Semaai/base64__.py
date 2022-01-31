


import base64
from traceback import print_tb
import json


# auth_info = "ewogICJsb2dpbiI6ICI4OTcxMTgyMTgyIiwKICAicHdkIjogIlRlY2hAU2VtYWFpMTIzISIKfQ=="
# auth_type, auth_info = auth_info.split(None, 1)
# auth_type = auth_type.lower()
# username, password = base64.b64decode(auth_info).split(b":", 1)
# print(to_unicode(username), password)

# base64_string ="ewogICJsb2dpbiI6ICI4OTcxMTgyMTgyIiwKICAicHdkIjogIlRlY2hAU2VtYWFpMTIzISIKfQ=="
# base64_bytes = base64_string.encode("ascii")
  
# sample_string_bytes = base64.b64decode(base64_bytes)
# sample_string = sample_string_bytes.decode("ascii")

# print(json.loads(sample_string)["pwd"])

temp ="<RequestsCookieJar[<Cookie session_id=e1c711e0cb3f9260fafa7fe4761ce6e86b14d913 for localhost.local/>]>"
print(temp.split(" ")[1])

print(temp.split(" ")[1].split("=")[1])