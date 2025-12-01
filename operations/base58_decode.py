import base58

NAME = "From Base58"

def run(data: str) -> str:
    
    return base58.b58decode(data).decode(errors="ignore")