# operations/base62_decode.py
NAME = "Base62 Decode"

TABLE = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")}

def run(data: str) -> str:
    try:
        n = 0
        for c in data:
            n = n * 62 + TABLE[c]
        bytes_data = n.to_bytes((n.bit_length() + 7) // 8, 'big')
        try:
            return bytes_data.decode("utf-8")
        except:
            return bytes_data.hex()
    except:
        return "[Invalid Base62]"