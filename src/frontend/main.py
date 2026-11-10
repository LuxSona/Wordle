import tkinter as tk
from src.frontend.Controller import Controller

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
    #Quits afterward
    app.outbox.put("Q")
    
if __name__ == "__main__":
    main()
