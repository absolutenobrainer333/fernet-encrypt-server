import hashlib
import base64


def convertStringToBase64String(init_key):
    hashed_key = hashlib.sha256(init_key.encode()).digest()[:32]
    return base64.urlsafe_b64encode(hashed_key)
