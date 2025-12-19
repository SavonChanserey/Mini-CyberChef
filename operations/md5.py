import hashlib

NAME = "MD5"

def run(data: str) -> str:
    return hashlib.md5(data.encode(), usedforsecurity=False).hexdigest()