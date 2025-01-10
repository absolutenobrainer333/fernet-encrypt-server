import hashlib
import base64

# Using SHA-256 (Secure Hash Algorithm 256-bit) for hashing 
# Encoding the result in Base64 (with URL-safe encoding)

def convertStringToBase64String(init_key):
    hashed_key = hashlib.sha256(init_key.encode()).digest()[:32]
    return base64.urlsafe_b64encode(hashed_key)
