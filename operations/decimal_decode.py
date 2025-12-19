# operations/from_decimal.py
NAME = "From Decimal"

def run(data: str) -> str:
    
    try:
        return "".join(chr(int(x)) for x in data.strip().split())
    except:
        return "[Invalid Decimal]"