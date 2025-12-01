import base62

NAME = "From Base62"

def run(data: str) -> str:
    return base62.decodebytes(data).decode(errors="ignore")