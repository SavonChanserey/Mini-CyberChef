# operations/to_decimal.py
NAME = "To Decimal"

def run(data: str) -> str:
    return " ".join(str(ord(c)) for c in data)