BASE92_CHARS = "!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~"

TABLE = {c: i for i, c in enumerate(BASE92_CHARS)}

def _dec(s: str) -> bytes:
    n, bits, out = 0, 0, []
    for c in s:
        if c not in TABLE: continue
        n = (n << 13) | TABLE[c]
        bits += 13
        while bits >= 8:
            bits -= 8
            out.append((n >> bits) & 255)
    return bytes(out)

NAME = "From Base92"

def run(data: str) -> str:

    return _dec(data).decode(errors="ignore")