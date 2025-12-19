import hashlib

NAME = "SHA1"

def run(data: str) -> str:
    
    return hashlib.sha1(data.encode(), usedforsecurity=False).hexdigest()