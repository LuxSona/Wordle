import tkinter as tk 

class UserInterface():
    def __init__(self):
        #Root pane
        self.root = tk.Tk()
        self.word_frame = tk.Frame(self.root, width=150, height=300)
        self.root.geometry("600x400")
        self.button_panel = tk.Frame(self.root, width=600,height=100)
        #Rows
        self.ROW_COUNT = 6
        self.word_rows = []
        self.current_row = 0

        self.initalizeRows()
        for row in self.word_rows:
            row.pack(fill="both", expand=True)
        self.word_frame.pack(fill="y",expand=True)
        self.button_panel.pack()
        self.root.mainloop()
    
    def initalizeRows(self):
        for row_idx in range(self.ROW_COUNT):
            row = tk.Frame(self.word_frame)
            
            for col in range(5):
                row.grid_columnconfigure(col, weight=1)

            row.grid_rowconfigure(0,weight=1)
            for col in range(5):
                label = tk.Label(row, text=f"{row_idx},{col}")
                label.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
            self.word_rows.append(row)


a = UserInterface()
