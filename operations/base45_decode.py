import base45

NAME = "From Base45"

def run(data: str) -> str:
    try:
        decoded_bytes = base45.b45decode(data.strip())
        return decoded_bytes.decode('utf-8', errors='replace')
    except Exception as e:
        return f"[Error: Invalid Base45 - {str(e)}]"