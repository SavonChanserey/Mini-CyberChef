import base58

NAME = "To Base58"

def run(data: str) -> str:
    return base58.b58encode(data.encode('utf-8')).decode('utf-8')