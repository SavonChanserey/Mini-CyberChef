# operations/base58_encode.py
NAME = "Base58 Encode"

ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def run(data: str) -> str:
    bytes_data = data.encode("utf-8")
    n = int.from_bytes(bytes_data, 'big')
    result = []
    while n > 0:
        n, rem = divmod(n, 58)
        result.append(ALPHABET[rem])
    # Add leading '1' for zero bytes
    result.extend('1' for _ in range(next((i for i, b in enumerate(bytes_data) if b), len(bytes_data))))
    return ''.join(reversed(result))