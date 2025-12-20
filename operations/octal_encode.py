NAME = "To Octal"

def run(data: str) -> str:
    return " ".join(f"{ord(c):03o}" for c in data)