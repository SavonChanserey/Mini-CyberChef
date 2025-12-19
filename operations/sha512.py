import hashlib

NAME = "SHA512"

def run(data: str) -> str:
    
    return hashlib.sha512(data.encode()).hexdigest()