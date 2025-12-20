import base58

NAME = "From Base58"

def run(data: str) -> str:
    try:
        decoded_bytes = base58.b58decode(data.strip())
        return decoded_bytes.decode('utf-8', errors='replace')
    except Exception as e:
        return f"[Error: Invalid Base58 - {str(e)}]"