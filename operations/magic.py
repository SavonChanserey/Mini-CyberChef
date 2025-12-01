# operations/magic.py
import re
import string
from pathlib import Path
import importlib.util

NAME = "Magic"

# List of all decode functions we want to try
DECODE_OPERATIONS = [
    # (display_name, module_name, function_name, needs_key?)
    ("Base64",         "base64_decode",         "run", False),
    ("Base64URL",      "base64url_decode",      "run", False),
    ("Base32",         "base32_decode",         "run", False),
    ("Base58",         "base58_decode",         "run", False),
    ("Base62",         "base62_decode",         "run", False),
    ("Base85",         "base85_decode",         "run", False),
    ("Hex",            "hex_decode",            "run", False),
    ("Binary",         "binary_decode",         "run", False),
    ("Bacon",          "bacon_decode",          "run", False),
    ("ROT13",          "rot13",                 "run", False),
    ("ROT47",          "rot47",                 "run", False),
    # Add more later if you want
]

def is_meaningful(text: str) -> bool:
    """Return True if text looks like real English / flag / code"""
    if not text:
        return False
    printable = sum(c in string.printable for c in text) / len(text)
    if printable < 0.9:
        return False
    words = re.findall(r'[a-zA-Z]{4,}', text)
    common = {'the', 'and', 'flag', 'ctf', 'pico', 'hello', 'password', 'secret', 'key', 'crypto'}
    return any(w.lower() in common for w in words) or len(words) >= 3

def run(data: str) -> str:
    data = data.strip()
    if not data:
        return "[Empty input]"

    results = []

    # Try every decode operation
    for name, mod_name, func_name, needs_key in DECODE_OPERATIONS:
        try:
            # Dynamically import the module
            path = Path(__file__).parent / f"{mod_name}.py"
            spec = importlib.util.spec_from_file_location(mod_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            func = getattr(module, func_name)
            result = func(data)

            if result and result not in {"[Invalid", "[No", data}:  # avoid junk
                if is_meaningful(result):
                    return f"[{name}] {result}"

                results.append((name, result))
        except Exception:
            pass  # silently skip broken ones

    # If nothing was clearly meaningful, return best guesses
    if results:
        best = max(results, key=lambda x: len(re.findall(r'[a-zA-Z]', x[1])), default=None)
        if best:
            return f"[Possible {best[0]}] {best[1]}"

    # Try ROT13 even on plaintext (common trick)
    try:
        from .rot13 import run as rot13_run
        rot = rot13_run(data)
        if is_meaningful(rot):
            return f"[ROT13] {rot}"
    except:
        pass

    return f"[Unknown] Likely raw or new encoding\n\nInput length: {len(data)}\nPreview: {data[:200]}{'...' if len(data)>200 else ''}"