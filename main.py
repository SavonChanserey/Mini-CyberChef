#!/usr/bin/env python3
# main.py  ←←←  ONLY RUN THIS FILE

import sys
from pathlib import Path

# Fix the Python path so imports work perfectly
PROJECT_ROOT = Path(__file__).parent.absolute()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Optional debug – shows you everything is found (you can delete these two lines later)
print("Mini-CyberChef started")
print("Found operations:", [f.stem for f in PROJECT_ROOT.joinpath("operations").glob("*.py") if not f.name.startswith("__")])

# Launch the app
from gui.app import MiniCyberChefApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniCyberChefApp(root)
    root.mainloop()
