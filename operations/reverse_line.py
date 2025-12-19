# operations/reverse_lines.py
NAME = "Reverse Lines"

def run(data: str) -> str:
    
    return "\n".join(reversed(data.strip().splitlines()))