NAME = "To Binary"

def run(data: str) -> str:
    return " ".join(f"{ord(c):08b}" for c in data)