NAME = "ROT47"

def run(data: str) -> str:
    return "".join(chr((ord(c) - 33 + 47) % 94 + 33) if 33 <= ord(c) <= 126 else ord(c) for c in data)