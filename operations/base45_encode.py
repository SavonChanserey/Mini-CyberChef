import base45

NAME = "To Base45"

def run(data: str) -> str:
    return base45.b45encode(data.encode('utf-8')).decode('utf-8')