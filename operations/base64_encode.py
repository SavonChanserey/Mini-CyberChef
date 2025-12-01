import base64

NAME = "To Base64"

def run(data: str) -> str:
    
    return base64.b64encode(data.encode()).decode()