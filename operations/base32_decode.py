import base64

NAME = "From Base32"

def run(data: str) -> str:
    return base64.b32decode(data.upper()).decode("utf-8", errors="replace")
