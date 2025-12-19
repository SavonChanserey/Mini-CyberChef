import base92

NAME = "To Base92"

def run(data: str) -> str:
    try:
        bytes_data = data.encode('utf-8')
        encoded = base92.b92encode(bytes_data)
        return encoded.decode('ascii')  # Clean ASCII output
    except Exception as e:
        return f"[Base92 Encode Error] {e}"