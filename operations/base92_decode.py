import base92

NAME = "From Base92"

def run(data: str) -> str:
    try:
        # Convert the input string to bytes first (required by base92.decode)
        encoded_bytes = data.strip().encode('ascii')
        decoded_bytes = base92.decode(encoded_bytes)
        
        # Try to return as readable text
        try:
            return decoded_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If not valid UTF-8 (binary data), show as hex
            return decoded_bytes.hex()
    except Exception as e:
        return f"[Decode Error: Invalid Base92 - {str(e)}]"