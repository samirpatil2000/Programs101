from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt

def encode_jwt(payload, private_key):
    encoded_token = jwt.encode(payload, private_key, algorithm="RS256")
    return encoded_token

def decode_jwt(token, public_key):
    decoded_payload = jwt.decode(token, public_key, algorithms=["RS256"])
    return decoded_payload

private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAy+t2uncn+0CcTDpzymfZudcjklk65IRhrL5KtgViN/rOYkmf\np1nUdvwczCm8ARJDc/SVAtUR7gJ2II+AxKAmV9r/BRiJr2rm+PzAfv9RPhT8jTV2\n2qAdNLlEYs7oaxnrVAzy28KpYF05gYD6Z9h0+Kc350jaCd9rg3RZRGBagRDYDdy+\n/vMeRS2g7O50zsb/KPyD1loIrRwoqv5jMfD0WNpVu1WH1pCs2E4ag84KAWqaYdC3\nu5vbmXf3mM7ysiesKxXYy10YLPQdythdHtRi1BXt6zjn88NWUO8K/hSl2zEOHnHf\nrg/uxWmluTuB8j5ZiRufwUKPJlrsicvryQtJbQIDAQABAoIBAAG9I26J8efVEGAg\nBs5niKDqjOLvFYRO/VblP9WB1z67Se48StBjq4mg3bf/SnCckMGuM2UU9F8EsLAs\nuRWJeLo6uP5N9sKYVUQzQjWdr2TUS1EC7zKvDIC0wbixTfm30gdjSDYygzzknpxp\nlqOzDKWgJhG3+nqnZ+R05gaiEbN/BuBc2WZ23N9GuxZ2GwpCTL1Fngkybh4Jrav5\nevNPyipkLHWaanNBkL4yhbjNdnQEQGpKvWi/TWkwVWUXBEDfQLZ+TUHYJFrmA+9y\npRydRBdwnikTVYL4RXJTqY6Low1K5+Xxv0mTuQP16oSmR/I6rAbZVn37aPMEaiwQ\naCxYeWECgYEA5u4+RJ4Dfboo5/PdJxer15IIdoZ1KsgHc589XaPkwzpUNedl6esn\n81wYhgTrCKVmfFB3n7AeWdDIJ8hoJ890daekcAn9BgbmrnmaJW3HoPcA9aTKyCTA\nwe8X9r3H7YuZKnda7GIGNPA6kF6sCY+SbQcl6V4fBeItsrlS/+5otHECgYEA4g6Q\n64mpnPed3Zvor1ob/slByZlIDbRPjZRZmjnz/94Bf0ppSyd9L8hv8rb+1QKEVu2f\nKsGjwxEbWZVsg6BF6vej6gZJ6h94K9daNeSkSwu2QBuZwZtYNKvZbENq6ObI5QTu\n1knRuCU6xk1KjyIGlhIEXjWt6bqoNuw6NLqAMr0CgYAPhnjdOBpX+4oAfh6iIC9H\nYOP8w/FgnO4TUeNYRkp87ZD3xsTNQyf+bnSfnfkHLceEGAzSyY5gz26Fbi3Cb2oO\n9uRRO/qsyw37MOWyGn1PTwvbd+bCKeZjo2VjC0NDrxzvA/My7SwppvTo+9RpGCPp\n/I8J72/6f0g/OcJgvnB/oQKBgQCH3jVgPCeDvphVwAWEj2ZQJuqxnr1d70f5Unbg\naYCsAuVnenP6xctKUvBmM3LK2G5uSPfnnOcusTN9DoBgRI6BgUI1wH3gh/WUdCU2\nSywsJuftdClf4lyLm9ZcadDyFvQcInDivw+b3FSNJ5tumAbZYA7cCOt0lcnQ6P66\n/nVbCQKBgQC3sCtW39MdG4diJw/NONGdY2GxDWLpct5IyQ1gqiX0WM5Q69qaOpcQ\nybkkoylGy+byfLuqEVeM+GoGJSMcWgF61fYcYNaNqLgJJMRMilue5eAD2/MpCToO\nxyaVLEwQB2uptWCrV4/eabFxim6Wgrfil0v/CKQyB+2Oolibwuz3Uw==\n-----END RSA PRIVATE KEY-----\n"
public_key = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy+t2uncn+0CcTDpzymfZ\nudcjklk65IRhrL5KtgViN/rOYkmfp1nUdvwczCm8ARJDc/SVAtUR7gJ2II+AxKAm\nV9r/BRiJr2rm+PzAfv9RPhT8jTV22qAdNLlEYs7oaxnrVAzy28KpYF05gYD6Z9h0\n+Kc350jaCd9rg3RZRGBagRDYDdy+/vMeRS2g7O50zsb/KPyD1loIrRwoqv5jMfD0\nWNpVu1WH1pCs2E4ag84KAWqaYdC3u5vbmXf3mM7ysiesKxXYy10YLPQdythdHtRi\n1BXt6zjn88NWUO8K/hSl2zEOHnHfrg/uxWmluTuB8j5ZiRufwUKPJlrsicvryQtJ\nbQIDAQAB\n-----END PUBLIC KEY-----\n"

payloads = [
    {"phoneNumber": "9730614299", "userId": "9b696951-8f95-49d2-aeae-8d588edbb6a9"},
    {"phoneNumber": "9730614299", "userId": "caa5d569-0aa8-4857-9b96-c50fafc46df1"},
    {"phoneNumber": "9730614299", "userId": "d8b4cd01-ce98-4970-b159-b397060062a4"},
    {"phoneNumber": "9730614299", "userId": "aaf52afe-99cc-49c9-a1c1-eac30b90b09f"},
]

for payload in payloads:
    encoded_jwt = encode_jwt(payload, private_key)
    print("\nEncoded JWT:\n", encoded_jwt)

    decoded_payload = decode_jwt(encoded_jwt, public_key)
    print("\nDecoded Payload:\n", decoded_payload)