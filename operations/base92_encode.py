import base92

NAME = "To Base92"

def run(data: str) -> str:
    try:
        encoded_bytes = base92.encode(data.encode('utf-8'))
        return encoded_bytes.decode('ascii')  
    except Exception as e:
        return f"[Encode Error: {str(e)}]"