import hashlib
import base64
# import secrets

# Using SHA-256 (Secure Hash Algorithm 256-bit) for hashing 
# Encoding the result in Base64 (with URL-safe encoding)

def convertStringToBase64String(init_key):
    hashed_key = hashlib.sha256(init_key.encode()).digest()[:32]
    return base64.urlsafe_b64encode(hashed_key)

# def generateAESKey(init_key):
#     random_bytes = secrets.token_bytes(16)  # AES block size is 16 bytes
#     combined_key = init_key.encode() + random_bytes
#     hashed_combined_key = hashlib.sha256(combined_key).digest()[:32]
#     return hashed_combined_key  # Return raw bytes for AES

