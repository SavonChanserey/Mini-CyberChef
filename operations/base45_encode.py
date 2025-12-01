import base45

NAME = "To Base45"

def run(data: str) -> str:
    
    return base45.b45encode(data.encode()).decode()