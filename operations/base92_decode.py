# operations/base92_decode.py

import base92

NAME = "From Base92"

def run(data: str) -> str:
    try:
        # Clean the input (remove spaces, newlines, optional <~ ~> wrapper)
        cleaned = data.strip().replace(" ", "").replace("\n", "").replace("\r", "")
        cleaned = cleaned.removeprefix("<~").removesuffix("~>")

        # CRITICAL FIX: base92.b92decode expects BYTES, not str!
        # So we encode the cleaned string to bytes first
        decoded_bytes = base92.b92decode(cleaned.encode('ascii'))

        # Try to decode as UTF-8 text
        try:
            return decoded_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If not text, return as hex (safe fallback)
            return decoded_bytes.hex()

    except Exception as e:
        return f"[Base92 Decode Error] {str(e)}"