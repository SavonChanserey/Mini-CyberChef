NAME = "From Charcode"

def run(data: str) -> str:
    data = data.strip()
    result = []
    codes = data.replace(',', ' ').split()
    for code in codes:
        code = code.strip()
        if not code:
            continue
        try:
            if code.lower().startswith('0x'):
                result.append(chr(int(code, 16)))
            elif code.lower().startswith('0o'):
                result.append(chr(int(code, 8)))
            else:
                result.append(chr(int(code)))
        except ValueError:
            result.append(code)  # keep invalid as-is
    return ''.join(result)