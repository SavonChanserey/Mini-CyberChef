import tkinter as tk
from gui.app import MiniCyberChefApp

def main():
    print("Mini-CyberChef starting...")
    
    root = tk.Tk()
    app = MiniCyberChefApp(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Make window resizable
    root.minsize(1200, 700)
    
    print("Mini-CyberChef ready!")
    root.mainloop()

if __name__ == "__main__":
    main()