# gui/app.py
import tkinter as tk
from tkinter import ttk, scrolledtext
from pathlib import Path
import importlib.util
import sys

class MiniCyberChefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-CyberChef v1.0")
        self.root.geometry("1200x750")

        self.operations = self._load_operations()
        self._build_ui()

    def _load_operations(self):
        ops = {}
        op_folder = Path(__file__).parent.parent / "operations"

        for py_file in op_folder.glob("*.py"):
            if py_file.name.startswith("_"):
                continue

            module_name = py_file.stem
            try:
                spec = importlib.util.spec_from_file_location(module_name, py_file)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                if hasattr(module, "NAME") and hasattr(module, "run"):
                    ops[module.NAME] = module.run
                else:
                    print(f"[SKIP] {module_name} missing NAME or run()")
            except Exception as e:
                print(f"[FAILED] {module_name}: {e}")

        return ops

    def _build_ui(self):
        paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left side
        left = ttk.Frame(paned)
        paned.add(left, weight=1)

        ttk.Label(left, text="Available Operations (double-click to add):", font=12).pack(anchor="w", pady=(0,5))
        self.list_ops = tk.Listbox(left, font=("Menlo", 11))
        self.list_ops.pack(fill=tk.BOTH, expand=True)
        for name in sorted(self.operations.keys()):
            self.list_ops.insert(tk.END, name)
        self.list_ops.bind("<Double-1>", lambda e: self._add())

        ttk.Separator(left, orient="horizontal").pack(fill="x", pady=12)

        ttk.Label(left, text="Active Recipe:", font=12).pack(anchor="w")
        self.list_recipe = tk.Listbox(left, height=12, bg="#fffbe6")
        self.list_recipe.pack(fill=tk.BOTH, expand=True)
        self.list_recipe.bind("<Double-1>", lambda e: self.list_recipe.delete(tk.ACTIVE))

        ttk.Button(left, text="Clear Recipe", command=lambda: self.list_recipe.delete(0, tk.END)).pack(pady=5)

        # Right side
        right = ttk.Frame(paned)
        paned.add(right, weight=3)

        ttk.Label(right, text="Input:", font=12).pack(anchor="w")
        self.txt_in = scrolledtext.ScrolledText(right, font=("Menlo", 11))
        self.txt_in.pack(fill=tk.BOTH, expand=True, pady=(0,10))

        ttk.Button(right, text="Run Recipe", command=self._run).pack(pady=10)

        ttk.Label(right, text="Output:", font=12).pack(anchor="w")
        self.txt_out = scrolledtext.ScrolledText(right, bg="#f0fff0", font=("Menlo", 11))
        self.txt_out.pack(fill=tk.BOTH, expand=True)

    def _add(self):
        sel = self.list_ops.curselection()
        if sel:
            self.list_recipe.insert(tk.END, self.list_ops.get(sel))

    def _run(self):
        data = self.txt_in.get("1.0", tk.END).rstrip("\n")
        self.txt_out.delete("1.0", tk.END)

        for i in range(self.list_recipe.size()):
            name = self.list_recipe.get(i)
            func = self.operations[name]
            try:
                data = func(data)
            except Exception as e:
                data = f"[ERROR in {name}] {e}"

        self.txt_out.insert(tk.END, data)