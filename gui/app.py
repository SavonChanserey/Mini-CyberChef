# gui/app.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from pathlib import Path # Help find folders easily
import importlib.util # Allow dynamic importing of operation modules

class MiniCyberChefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-CyberChef")
        self.root.geometry("1600x900")
        self.root.configure(bg="#f5f7fa")

        self.operations = {} # Directory of all loaded operations
        self.filtered_operations = [] # For Search filtering
        self.recipe = [] # List of operations in order (the "recipe")
        self.drag_data = {"item": None, "x": 0, "y": 0} # Track what you're dragging
        self.dragging = False # Are we currently dragging?

        self._load_operations()
        self._setup_ui()
        self._setup_drag_drop()

    # Load all operations from the "operations" folder
    def _load_operations(self):
        ops_folder = Path(__file__).parent.parent / "operations"
        if ops_folder.exists():
            for py_file in ops_folder.glob("*.py"):
                if py_file.name.startswith("_"):
                    continue
                try:
                    spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    if hasattr(mod, "NAME") and hasattr(mod, "run"):
                        name = mod.NAME
                        self.operations[name] = {
                            "func": mod.run,
                            "desc": getattr(mod, "DESCRIPTION", name)
                        }
                except Exception as e:
                    print(f"Failed to load {py_file.name}: {e}")

        self.filtered_operations = list(self.operations.keys())

    # Build the entire user interface
    def _setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')

        main_container = tk.Frame(self.root, bg="#f5f7fa")
        main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # ========== LEFT SIDEBAR ==========
        sidebar = tk.Frame(main_container, bg="#2c3e50", width=380, relief="flat")
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Title
        title_frame = tk.Frame(sidebar, bg="#1a252f", height=70)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        tk.Label(title_frame, text="MINI-CYBERCHEF", font=("Helvetica", 18, "bold"),bg="#1a252f", fg="white").pack(pady=20)

        # Search bar
        search_frame = tk.Frame(sidebar, bg="#34495e", padx=15, pady=15)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="🔍", font=("Helvetica", 14),bg="#34495e", fg="white").pack(side="left", padx=(0, 10))
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,font=("Helvetica", 11), bg="white",relief="flat", insertbackground="#3498db")
        search_entry.pack(side="right", fill="x", expand=True, ipady=5)
        search_entry.insert(0, "Search operations...")
        search_entry.bind("<FocusIn>", lambda e: search_entry.delete(0, tk.END) if search_entry.get() == "Search operations..." else None)
        search_entry.bind("<KeyRelease>", lambda e: self._filter_ops())

        # Operation header
        ops_header = tk.Frame(sidebar, bg="#1a252f", height=40)
        ops_header.pack(fill="x", pady=(10, 0))
        ops_header.pack_propagate(False)
        tk.Label(ops_header, text="OPERATIONS", font=("Helvetica", 12, "bold"),bg="#1a252f", fg="white").pack(pady=10)
        ops_container = tk.Frame(sidebar, bg="#2c3e50")
        ops_container.pack(fill="both", expand=True, padx=15, pady=10)
        ops_canvas = tk.Canvas(ops_container, bg="#2c3e50", highlightthickness=0)
        ops_scroll = ttk.Scrollbar(ops_container, orient="vertical", command=ops_canvas.yview)
        self.ops_frame = tk.Frame(ops_canvas, bg="#2c3e50")
        ops_canvas.create_window((0, 0), window=self.ops_frame, anchor="nw")
        ops_canvas.configure(yscrollcommand=ops_scroll.set)
        ops_canvas.pack(side="left", fill="both", expand=True)
        ops_scroll.pack(side="right", fill="y")
        
        # Recipe header
        recipe_header = tk.Frame(sidebar, bg="#1a252f", height=40)
        recipe_header.pack(fill="x", pady=(10, 0))
        recipe_header.pack_propagate(False)
        tk.Label(recipe_header, text="RECIPE", font=("Helvetica", 12, "bold"),bg="#1a252f", fg="white").pack(pady=10)

        # Recipe area (scrollable)
        recipe_container = tk.Frame(sidebar, bg="#34495e")
        recipe_container.pack(fill="both", expand=True, padx=15, pady=10)
        self.recipe_canvas = tk.Canvas(recipe_container, bg="#34495e", highlightthickness=0)
        recipe_scroll = ttk.Scrollbar(recipe_container, orient="vertical", command=self.recipe_canvas.yview)
        self.recipe_frame = tk.Frame(self.recipe_canvas, bg="#34495e")
        self.recipe_canvas.create_window((0, 0), window=self.recipe_frame, anchor="nw")
        self.recipe_canvas.configure(yscrollcommand=recipe_scroll.set)
        self.recipe_canvas.pack(side="left", fill="both", expand=True)
        recipe_scroll.pack(side="right", fill="y")

        # Drop hint text
        self.drop_hint = tk.Label(self.recipe_frame,font=("Helvetica", 12), bg="#34495e", fg="#7f8c8d")
        self.drop_hint.pack(expand=True, fill="both", pady=50)
        btn_frame = tk.Frame(sidebar, bg="#2c3e50", padx=15, pady=15)
        btn_frame.pack(fill="x")

        # Clear Button 
        clear_btn = tk.Button(btn_frame, text="🗑️ Clear", font=("Helvetica", 11),bg="#e74c3c", relief="flat", cursor="hand2",command=self._clear_recipe)
        clear_btn.pack(side="left", padx=(0, 10))

        # ========== RIGHT SIDEBAR ==========
        right_panel = tk.Frame(main_container, bg="white")
        right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Input Area
        input_frame = tk.LabelFrame(right_panel, text=" INPUT ", font=("Helvetica", 13, "bold"),bg="#2c3e50", fg="white", relief="flat", labelanchor="n")
        input_frame.pack(fill="both", expand=True, padx=5, pady=(0, 10))
        
        input_ctrl = tk.Frame(input_frame, bg="#2c3e50", padx=10, pady=10)
        input_ctrl.pack(fill="x")
        
        # Copy Button
        tk.Button(input_ctrl, text="📋 Copy", font=("Helvetica", 10),bg="black", relief="flat", cursor="hand2",command=lambda: self._copy_text(self.input_text)).pack(side="left", padx=(0, 10))
        
        # Load File Button
        tk.Button(input_ctrl, text="📁 Load File", font=("Helvetica", 10),bg="#3498db", relief="flat", cursor="hand2",command=self._load_file).pack(side="left", padx=(0, 10))
        
        # Clear Button
        tk.Button(input_ctrl, text="🗑️ Clear", font=("Helvetica", 10),bg="#95a5a6", relief="flat", cursor="hand2",command=lambda: self.input_text.delete("1.0", tk.END)).pack(side="left")
        self.input_text = scrolledtext.ScrolledText(input_frame, font=("Consolas", 12),wrap=tk.WORD, bg="#f8f9fa",relief="flat", borderwidth=1)
        self.input_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Output Area
        output_frame = tk.LabelFrame(right_panel, text=" OUTPUT ", font=("Helvetica", 13, "bold"),bg="#2c3e50", fg="white", relief="flat", labelanchor="n")
        output_frame.pack(fill="both", expand=True, padx=5)
        output_ctrl = tk.Frame(output_frame, bg="#2c3e50", padx=10, pady=10)
        output_ctrl.pack(fill="x")
        
        # Copy Button
        tk.Button(output_ctrl, text="📋 Copy", font=("Helvetica", 10),bg="black", relief="flat", cursor="hand2",command=lambda: self._copy_text(self.output_text)).pack(side="left", padx=(0, 10))
        
        # Save Button
        tk.Button(output_ctrl, text="💾 Save", font=("Helvetica", 10),bg="black", relief="flat", cursor="hand2",command=self._save_output).pack(side="left", padx=(0, 10))
        
        # Clear Button
        tk.Button(output_ctrl, text="🗑️ Clear", font=("Helvetica", 10),bg="black", relief="flat", cursor="hand2",command=lambda: self.output_text.delete("1.0", tk.END)).pack(side="left")
        
        # Replace Input with Output Button
        tk.Button(output_ctrl, text="Replace input with output",font=("Helvetica", 10),bg="black", relief="flat", cursor="hand2",command=self._replace_input_with_output).pack(side="left", padx=(10,0))

        # Populate operations and set up scrolling
        self.output_text = scrolledtext.ScrolledText(output_frame, font=("Consolas", 12),wrap=tk.WORD, bg="#f8f9fa",relief="flat", borderwidth=1)
        self.output_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self._populate_operations()

        self.ops_frame.bind("<Configure>", lambda e: ops_canvas.configure(scrollregion=ops_canvas.bbox("all")))
        self.recipe_frame.bind("<Configure>", lambda e: self.recipe_canvas.configure(scrollregion=self.recipe_canvas.bbox("all")))

        # =================== MOUSE WHEEL SCROLLING FOR LEFT SIDEBAR ===================

        def on_mousewheel(event, canvas):
            
            scrollregion = canvas.bbox("all")
            if scrollregion is None:
                return
            content_height = scrollregion[3] - scrollregion[1]
            canvas_height = canvas.winfo_height()
            if content_height <= canvas_height:
                return
            if event.num == 5 or event.delta < 0:
                canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta > 0:
                canvas.yview_scroll(-1, "units")

        def bind_mousewheel_to_canvas(canvas):
            
            canvas.bind("<MouseWheel>", lambda e: on_mousewheel(e, canvas))
            canvas.bind("<Button-4>", lambda e: on_mousewheel(e, canvas))
            canvas.bind("<Button-5>", lambda e: on_mousewheel(e, canvas))
        
            frame = canvas.nametowidget(canvas.itemcget(canvas.find_withtag("all")[0], "window"))
        
            frame.bind("<MouseWheel>", lambda e: on_mousewheel(e, canvas))
            frame.bind("<Button-4>", lambda e: on_mousewheel(e, canvas))
            frame.bind("<Button-5>", lambda e: on_mousewheel(e, canvas))
        
            def bind_to_children(parent):
                for child in parent.winfo_children():
                    child.bind("<MouseWheel>", lambda e: on_mousewheel(e, canvas))
                    child.bind("<Button-4>", lambda e: on_mousewheel(e, canvas))
                    child.bind("<Button-5>", lambda e: on_mousewheel(e, canvas))
                    if child.winfo_children():
                        bind_to_children(child)
        
            bind_to_children(frame)
            frame.bind("<Configure>", lambda e: self.root.after(50, bind_to_children, frame))

        bind_mousewheel_to_canvas(ops_canvas)
        bind_mousewheel_to_canvas(self.recipe_canvas)

        def update_ops_scrollregion():
            ops_canvas.configure(scrollregion=ops_canvas.bbox("all"))
    
        def update_recipe_scrollregion():
            self.recipe_canvas.configure(scrollregion=self.recipe_canvas.bbox("all"))
    
        self.update_ops_scrollregion = update_ops_scrollregion
        self.update_recipe_scrollregion = update_recipe_scrollregion

        self.root.after(200, update_ops_scrollregion)
        self.root.after(200, update_recipe_scrollregion)

    # Populate the list of available operations
    def _populate_operations(self):
        
        for w in self.ops_frame.winfo_children():
            w.destroy()
        for name in self.filtered_operations:
            desc = self.operations[name]["desc"]
            op_frame = tk.Frame(self.ops_frame, bg="#3d566e", cursor="hand2")
            op_frame.pack(fill="x", pady=2)
            op_label = tk.Label(op_frame, text=f" {name}", font=("Helvetica", 11),bg="#3d566e", fg="white", anchor="w", padx=10, pady=8)
            op_label.pack(fill="x")
            desc_label = tk.Label(op_frame, text=f" {desc}", font=("Helvetica", 9),bg="#3d566e", fg="#bdc3c7", anchor="w", padx=10)
            desc_label.pack(fill="x", pady=(0, 8))
            for widget in [op_frame, op_label, desc_label]:
                widget.bind("<ButtonPress-1>", lambda e, n=name: self._start_drag(e, n))
                widget.bind("<ButtonRelease-1>", lambda e, n=name: self._stop_drag(e, n))
                widget.bind("<Enter>", lambda e, f=op_frame, l=op_label, d=desc_label: self._on_enter(f, l, d))
                widget.bind("<Leave>", lambda e, f=op_frame, l=op_label, d=desc_label: self._on_leave(f, l, d))

    # Hover effects for operation cards
    def _on_enter(self, frame, label, desc_label):

        frame.config(bg="#4a6278")
        label.config(bg="#4a6278")
        desc_label.config(bg="#4a6278")

    def _on_leave(self, frame, label, desc_label):
        
        frame.config(bg="#3d566e")
        label.config(bg="#3d566e")
        desc_label.config(bg="#3d566e")

    # Search filter for operations
    def _filter_ops(self):
        
        q = self.search_var.get().lower()
        if q == "search operations...":
            q = ""
        if not q:
            self.filtered_operations = list(self.operations.keys())
        else:
            self.filtered_operations = [op for op in self.operations.keys() if q in op.lower()]
        self._populate_operations()

    # Drag & Drop setup
    def _setup_drag_drop(self):
        
        self.recipe_canvas.bind("<ButtonRelease-1>", self._on_drop)
        self.recipe_frame.bind("<ButtonRelease-1>", self._on_drop)
        self.root.bind("<B1-Motion>", self._on_drag_motion)
        self.root.bind("<ButtonRelease-1>", self._stop_drag)

    # Drag & Drop functions
    def _start_drag(self, event, name):
        
        self.drag_data = {"name": name, "x": event.x_root, "y": event.y_root}
        self.dragging = True
        self.root.config(cursor="hand2")

    def _on_drag_motion(self, event):
        
        if self.dragging:
            pass

    def _stop_drag(self, event=None, name=None):
        
        self.dragging = False
        self.root.config(cursor="")

    def _on_drop(self, event):
        
        if self.drag_data and "name" in self.drag_data:
            op_name = self.drag_data["name"]
            self._add_to_recipe(op_name)
            self.drag_data = {}
            self.dragging = False
            self.root.config(cursor="")

    # Add operation to recipe
    def _add_to_recipe(self, name):
        
        if self.drop_hint.winfo_ismapped():
            self.drop_hint.pack_forget()
        item_frame = tk.Frame(self.recipe_frame, bg="#4a6278", relief="flat", bd=1)
        item_frame.pack(fill="x", pady=4, padx=10, ipady=5)
        tk.Label(item_frame, text=name, font=("Helvetica", 11, "bold"),bg="#4a6278", fg="white").pack(side="left", padx=15, pady=8)
        remove_btn = tk.Button(item_frame, text="✕", font=("Helvetica", 14),bg="#4a6278", fg="#e74c3c", bd=0, cursor="hand2",command=lambda b=item_frame: self._remove_recipe_item(b))
        remove_btn.pack(side="right", padx=15)
        self.recipe.append((name, item_frame))
        self.recipe_canvas.yview_moveto(1.0)
        if hasattr(self, 'update_recipe_scrollregion'):
            self.update_recipe_scrollregion()

        # AUTO RUN  
        self.root.after(100, self._run_recipe)  # Small delay to ensure UI updates first

    # Remove operation from recipe
    def _remove_recipe_item(self, item_frame):
        
        for i, (name, frame) in enumerate(self.recipe):
            if frame == item_frame:
                frame.destroy()
                self.recipe.pop(i)
                break
        if not self.recipe:
            self.drop_hint.pack(expand=True, fill="both", pady=50)
        if hasattr(self, 'update_recipe_scrollregion'):
            self.update_recipe_scrollregion()

        # AUTO RUN AFTER REMOVING 
        self.root.after(100, self._run_recipe)

    # Clear entire recipe
    def _clear_recipe(self):
        
        if not self.recipe:
            return
        if messagebox.askyesno("Clear Recipe", "Are you sure you want to clear the entire recipe?"):
            for _, frame in self.recipe:
                frame.destroy()
            self.recipe.clear()
            self.drop_hint.pack(expand=True, fill="both", pady=50)
            if hasattr(self, 'update_recipe_scrollregion'):
                self.update_recipe_scrollregion()

            # AUTO RUN AFTER CLEAR (output will be cleared since no recipe)
            self.root.after(100, self._run_recipe)

    # Run the full recipe (core processing)
    def _run_recipe(self):
        
        data = self.input_text.get("1.0", tk.END).strip()
        if not data and self.recipe:  # Only warn if there's a recipe but no input
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", "[No input data]")
            return
        if not self.recipe:
            self.output_text.delete("1.0", tk.END)
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", "Processing...\n")
        self.root.update_idletasks()

        result = data
        try:
            for name, _ in self.recipe:
                op_data = self.operations.get(name)
                if not op_data:
                    raise ValueError(f"Operation '{name}' not found")
                result = op_data["func"](result)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", str(result))
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", f"❌ Error in operation '{name}':\n{str(e)}\n\nLast valid result:\n{result}")

    # Replace input with current output
    def _replace_input_with_output(self):
        
        content = self.output_text.get("1.0", tk.END).strip()
        if content:
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", content)
            self.input_text.config(bg="#d4edda")
            self.root.after(300, lambda: self.input_text.config(bg="#f8f9fa"))
            # Auto-run after replacing input
            self.root.after(400, self._run_recipe)

    # Load file into input
    def _load_file(self):
        
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read().hex()
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert("1.0", content)
                except Exception as e:
                    messagebox.showerror("Error", f"Cannot read file: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot read file: {e}")
            # Auto-run after loading file
            self.root.after(200, self._run_recipe)

    # Save output to file
    def _save_output(self):
        
        content = self.output_text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("No Output", "There is no output to save.")
            return
        file_path = filedialog.asksaveasfilename(
            title="Save Output",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Saved", f"Output saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file: {e}")

    # Copy text from input or output
    def _copy_text(self, text_widget):
        
        content = text_widget.get("1.0", tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.root.update()  # Ensures clipboard is updated immediately
            
            # Visual feedback
            original_bg = text_widget.cget("bg")
            text_widget.config(bg="#d4edda")
            self.root.after(300, lambda: text_widget.config(bg=original_bg))
        else:
            messagebox.showinfo("Nothing to Copy", "The text area is empty.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniCyberChefApp(root)
    root.mainloop()