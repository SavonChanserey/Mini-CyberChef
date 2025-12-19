# operations/base58_decode.py
NAME = "From Base58"

TABLE = {c: i for i, c in enumerate("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")}

def run(data: str) -> str:
    try:
        n = 0
        for c in data:
            n = n * 58 + TABLE[c]
        bytes_data = n.to_bytes((n.bit_length() + 7) // 8, 'big')
        # Remove leading zero bytes
        bytes_data = bytes_data.lstrip(b'\x00')
        try:
            return bytes_data.decode("utf-8")
        except:
            return bytes_data.hex()
    except:
        return "[Invalid Base58]"