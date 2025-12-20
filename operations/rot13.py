import codecs

NAME = "ROT13"

def run(data: str) -> str:
    return codecs.encode(data, "rot_13")