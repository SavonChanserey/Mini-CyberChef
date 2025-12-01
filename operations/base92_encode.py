BASE92_CHARS = "!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~"
TABLE = {c: i for i, c in enumerate(BASE92_CHARS)}

def _enc(b: bytes) -> str:
    n, bits, out = 0, 0, 0, []
    for byte in b:
        n = (n << 8) | byte
        bits += 8
        while bits >= 13:
            bits -= 13
            out.append(BASE92_CHARS[(n >> bits) & 8191])
    if bits:
        out.append(BASE92_CHARS[n << (13 - bits) & 8191])
        
NAME = "To Base92"

def run(data: str) -> str:
    
    return _enc(data.encode())