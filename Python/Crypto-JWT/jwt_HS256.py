import jwt

SECRET_KEY = "F9BNdSJqoV0j+YuEq0erYXp+/eY7rAVU9+U+AFHzy3w="

def encode_jwt(payload):
    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return encoded_token

def decode_jwt(token):
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return decoded_payload

payload = {"clientId": "a201d1bd-71a2-491d-8023-ce4792afeaf2"}
token = encode_jwt(payload=payload)
print("token :", token)
print("payload :", decode_jwt(token))

new_token = ""
# print("payload :", decode_jwt(new_token))