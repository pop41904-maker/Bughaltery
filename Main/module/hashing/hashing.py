import uuid, hashlib

def create_salt() -> str:
    return str(uuid.uuid4())
def hashing_data(Password : str, Salt : str) -> str:
    return hashlib.sha512((Password + Salt).encode()).hexdigest()