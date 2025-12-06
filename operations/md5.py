import hashlib

NAME = "md5"

def run(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()