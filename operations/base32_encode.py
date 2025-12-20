import base64

NAME = "To Base32"

def run(data: str) -> str:
    return base64.b32encode(data.encode()).decode().rstrip("=")