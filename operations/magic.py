from pathlib import Path # Use to locate the file in the operation folder
import importlib.util # Dynamic load the file from other file in the operations folder
import string

NAME = "Magic"

# List of decode operations to try. First: Display name, Second: Python file without .py
DECODE_OPERATIONS = [
    ("Base32",      "base32_decode"),
    ("Base58",      "base58_decode"),
    ("Base62",      "base62_decode"),
    ("Base64",      "base64_decode"),
    ("Base85",      "base85_decode"),
    ("Base92",      "base92_decode"),
    ("Binary",      "binary_decode"),
    ("Charcode",    "charcode_decode"),
    ("Decimal",     "decimal_decode"),
    ("Hex",         "hexadecimal_decode"),
    ("HTML_Entity", "html_entity_decode"),
    ("Morse",       "morsecode_decode"),
    ("Octal",       "octal_decode"),
    ("URL",         "url_decode"),
    ("Bacon",       "bacon_decode"),
]

# Prevent from garbage results, at least 5 characters, printable character
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

    # Find .py file dynamically and run 
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

            # Display and error message
            if not result or result == original:
                continue
            if any(err in result for err in ["[Invalid", "[Error", "[No key"]):
                continue

            # Return the result
            if is_good_result(result):
                return f"[{display_name}] {result}"

            # Save as candidate
            score = sum(c.isalpha() or c.isspace() for c in result)
            candidates.append((score, display_name, result))

        except (ValueError, TypeError, OSError) as e:  
            continue

    if candidates:
        candidates.sort(reverse=True)
        score, name, result = candidates[0]
        return f"[Possible {name}] {result}"

    return f"[No match]\nTried {len(DECODE_OPERATIONS)} automatic decoders."