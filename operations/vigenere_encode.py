from tkinter import simpledialog
import tkinter as tk

NAME = "Vigenère Encode"

def run(data: str) -> str:
    root = tk.Tk()
    root.withdraw()
    key = simpledialog.askstring("Vigenère Encode", "Enter key:")
    root.destroy()
    if not key:
        return data

    key = "".join(c.upper() for c in key if c.isalpha())
    if not key:
        return "[No valid key]"

    result = []
    ki = 0
    for c in data:
        if c.isupper():
            shifted = (ord(c) - 65 + ord(key[ki % len(key)]) - 65) % 26 + 65
            result.append(chr(shifted))
            ki += 1
        elif c.islower():
            shifted = (ord(c) - 97 + ord(key[ki % len(key)]) - 65) % 26 + 97
            result.append(chr(shifted))
            ki += 1
        else:
            result.append(c)
    return "".join(result)