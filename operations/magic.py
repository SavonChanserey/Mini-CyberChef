# operations/magic.py
from pathlib import Path
import importlib.util
import string

NAME = "Magic"

# ONLY automatic decoders — NO popups!
DECODE_OPERATIONS = [
    ("Base32",      "base32_decode"),
    ("Base58",      "base58_decode"),
    ("Base62",      "base62_decode"),
    ("Base64",      "base64_decode"),
    ("Base85",      "base85_decode"),
    ("Base92",      "base92_decode"),
    ("Hex",         "hexadecimal_decode"),
    ("Binary",      "binary_decode"),
    ("Octal",       "octal_decode"),
    ("URL",         "url_decode"),
    ("Morse",       "morsecode_decode"),
    ("Bacon",       "bacon_decode"),
    ("ROT13",       "rot13"),
    ("ROT47",       "rot47"),
]

def is_good_result(text: str) -> bool:
    
    if not text or len(text) < 5:
        return False
    
    if not all(c in string.printable for c in text):
        return False
    
    letters = sum(c.isalpha() for c in text)
    spaces = text.count(" ") + text.count("\n")
    return (letters + spaces) >= len(text) * 0.5  # Real text has letters + spaces

def run(data: str) -> str:
    original = data.strip()
    if not original:
        return "[Empty input]"

    candidates = []

    for display_name, module_name in DECODE_OPERATIONS:
        try:
            path = Path(__file__).parent / f"{module_name}.py"
            if not path.exists():
                continue

            spec = importlib.util.spec_from_file_location(module_name, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            result = mod.run(original)

            if not result or result == original:
                continue
            if any(err in result for err in ["[Invalid", "[Error", "[No key"]):
                continue

            # Good result → return immediately
            if is_good_result(result):
                return f"[{display_name}] {result}"

            # Save as candidate
            score = sum(c.isalpha() or c.isspace() for c in result)
            candidates.append((score, display_name, result))

        except (ValueError, TypeError, OSError) as e:  # Handle expected errors
            # print(f"Skipping invalid entry: {e}")  # Optional logging
            continue

    if candidates:
        candidates.sort(reverse=True)
        score, name, result = candidates[0]
        return f"[Possible {name}] {result}"

    return f"[No match]\nTried {len(DECODE_OPERATIONS)} automatic decoders."