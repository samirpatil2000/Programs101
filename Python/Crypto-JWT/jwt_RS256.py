from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode("utf-8")

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode("utf-8")

    return private_pem, public_pem

def encode_jwt(payload, private_key):
    encoded_token = jwt.encode(payload, private_key, algorithm="RS256")
    return encoded_token

def decode_jwt(token, public_key):
    decoded_payload = jwt.decode(token, public_key, algorithms=["RS256"])
    return decoded_payload

private_key, public_key = generate_key_pair()
print({"Private Key": private_key})
print({"Public Key": public_key})

payloads = [
    {"phoneNumber": "9730614299", "userId": "9b696951-8f95-49d2-aeae-8d588edbb6a9"},
    {"phoneNumber": "9730614299", "userId": "caa5d569-0aa8-4857-9b96-c50fafc46df1"},
    {"phoneNumber": "9730614299", "userId": "d8b4cd01-ce98-4970-b159-b397060062a4"},
]

for payload in payloads:
    encoded_jwt = encode_jwt(payload, private_key)
    print("\nEncoded JWT:\n", encoded_jwt)

# decoded_payload = decode_jwt(encoded_jwt, public_key)
# print("\nDecoded Payload:\n", decoded_payload)
