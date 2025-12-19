# operations/base45_encode.py
NAME = "To Base45"

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

def run(data: str) -> str:
    bytes_data = data.encode("utf-8")
    if not bytes_data:
        return ""
    result = []
    for i in range(0, len(bytes_data), 2):
        if i + 1 == len(bytes_data):
            value = bytes_data[i]
            result.append(ALPHABET[value % 45])
            result.append(ALPHABET[value // 45])
        else:
            value = bytes_data[i] + bytes_data[i+1] * 256
            result.append(ALPHABET[value % 45])
            result.append(ALPHABET[(value // 45) % 45])
            result.append(ALPHABET[value // 2025])
    return "".join(result)