import hashlib

NAME = "SHA256"

def run(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()