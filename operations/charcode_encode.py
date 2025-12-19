NAME = "To Charcode"

def run(data: str) -> str:
    return ' '.join(str(ord(c)) for c in data)