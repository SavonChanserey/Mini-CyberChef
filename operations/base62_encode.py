# operations/base62_encode.py
NAME = "Base62 Encode"

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def run(data: str) -> str:
    bytes_data = data.encode("utf-8")
    n = int.from_bytes(bytes_data, 'big')
    if n == 0:
        return "0"
    result = []
    while n > 0:
        n, rem = divmod(n, 62)
        result.append(ALPHABET[rem])
    return ''.join(reversed(result))