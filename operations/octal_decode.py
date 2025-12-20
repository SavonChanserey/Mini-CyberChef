NAME = "From Octal"

def run(data: str) -> str:
    try:
        return "".join(chr(int(octet, 8)) for octet in data.strip().split())
    except:
        return "[Invalid Octal]"