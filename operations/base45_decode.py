import base45

NAME = "From Base45"

def run(data: str) -> str:
    
    return base45.b45decode(data).decode()
