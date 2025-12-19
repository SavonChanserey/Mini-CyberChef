# operations/base45_decode.py
NAME = "From Base45"

TABLE = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")}

def run(data: str) -> str:
    data = data.strip()
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        if i + 2 > len(data):
            return "[Invalid Base45]"
        if i + 2 == len(data):
            e1 = TABLE[data[i]]
            e2 = TABLE[data[i+1]]
            value = e1 + e2 * 45
            result.append(value)
        else:
            e0 = TABLE[data[i]]
            e1 = TABLE[data[i+1]]
            e2 = TABLE[data[i+2]]
            value = e0 + e1 * 45 + e2 * 2025
            result.append(value % 256)
            result.append(value // 256)
        i += 3 if i + 2 < len(data) else 2
    try:
        return bytes(result).decode("utf-8")
    except:
        return bytes(result).hex()