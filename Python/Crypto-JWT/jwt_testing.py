from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt


def decode_jwt(token, public_key):
    decoded_payload = jwt.decode(token, public_key, algorithms=["RS256"])
    return decoded_payload

encoded_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInBob25lX251bWJlciI6Ijk3MzA2MTQyOTkifQ.HDl9vVk7Do6flobkWWzjcbFxDYqxnUjOAbVMkoBFB6uenyhmRgia3_L64ThS18Cgfrr3FlRwqBm9rK0Kt4HR7O03i_qC-DHLHRpPNV5A4t3C30kTiReelPzir3Ojeu9cgquAmsFsYPdLl-vc58wKKC16fTpUBxt13UwE8mj2Mu_VU1QeYaqtujG1J9yiVSiNxw3vSK5gqq_wTYUKN6F8LJAiTjmQsWhRVFJegCfI4dD6xqiENjTIQrR6pi74JaVHR7LAjuveknLbxq8-lX2UlV-SBhj-zoX_QO1WURMrWZawNDnqEdDzO2X5dH7wx8M4IBL6tuFOj-lK8i07nIWWgA"

public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzEkKCDq1BvH3JIKdxDHq
TzTct71OlQvLw0pz40m+sNiShGz5uinG5oO6SZ6QCBEsgO88cmOTwdpHXnayPGy+
hjFm0qPShcPuDG85O8tb8S6gpnecjnbm7mrMtLC8BWGD0WVKWXrQfzaFcUz/wvhF
iPihW3KYyuC01zasbOYqICOflN4+COy6RpRqY3Y7fdfl2Cb1toPBoGa14ZpwQ4Kd
njXwMsbMxjscwEwv4Yq9DkfbK3iIje2Bq65LqbAjJTTvu2TWqO8O3tdpj6HY8G7i
wJuYAch554xuXGFAl4IdCovlF47DGs21MShmydJKhm4+aYAV8VPnfc6VhUUX0oQj
nQIDAQAB
-----END PUBLIC KEY-----
"""
decoded_payload = decode_jwt(encoded_jwt, public_key)
print("\nDecoded Payload:\n", decoded_payload)