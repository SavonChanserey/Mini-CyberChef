# operations/count_chars.py
NAME = "Count Characters"

def run(data: str) -> str:
    
    length = len(data)
    lines = len(data.splitlines())
    words = len(data.split())
    return f"Characters: {length}\nLines: {lines}\nWords: {words}"