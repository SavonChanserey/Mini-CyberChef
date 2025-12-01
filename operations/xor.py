# operations/xor.py
from tkinter import simpledialog
import tkinter as tk
NAME = "XOR (single key)"
def run(data: str) -> str:
    root = tk.Tk(); root.withdraw()
    key = simpledialog.askstring("XOR Key", "Enter key (text or hex with 0x):")
    root.destroy()
    if not key: return data
    if key.lower().startswith("0x"):
        try: key = bytes.fromhex(key[2:])
        except: return "[Bad hex]"
    else:
        key = key.encode()
    result = bytes(b ^ key[i % len(key)] for i, b in enumerate(data.encode()))
    try:
        txt = result.decode()
        if all(32 <= ord(c) <= 126 or c in "\n\r\t" for c in txt):
            return txt
    except: pass
    return result.hex()