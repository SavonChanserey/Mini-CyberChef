import base62

NAME = "To Base62"

def run(data: str) -> str:
    return base62.encodebytes(data.encode())


        