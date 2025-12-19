NAME = "From Hex"

def run(data: str) -> str:
    
    try:
        cleaned = "".join(c for c in data if c.lower() in "0123456789abcdef")
        if len(cleaned) % 2: cleaned = "0" + cleaned
        return bytes.fromhex(cleaned).decode("utf-8", errors="replace")
    except:
        return "[Invalid Hex]"