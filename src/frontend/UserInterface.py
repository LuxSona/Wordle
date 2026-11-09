import tkinter as tk 
from .WordleClient import WordleClient

class UserInterface():
    """The user interface class
    """     
    def __init__(self, client : WordleClient):
        """The initialization function for the wordle interface class.

        :param client: A reference to the client connection handler
        :type client: WordleClient
        """        
        #Root pane
        self.client = client
        self.root = tk.Tk()
        self.word_frame = tk.Frame(self.root, width=150, height=300)
        self.root.geometry("600x400")
        self.button_panel = tk.Frame(self.root, width=600,height=100)
        #Rows
        self.ROW_COUNT = 6
        self.word_rows : list[list[tuple[int | None, tk.Canvas | None]]] = [[(None, None) for _ in range(5)] for _ in range(6)]
        self.current_row = 0
        self.current_col = 0

        self._initalizeRows()
        self.word_frame.pack(fill="y",expand=True)
        self.button_panel.pack()
        self._add_event_binding()
        self.root.mainloop()
    
    def _initalizeRows(self):
        """Initializes the word grid rows for the interface.
        """
        for row in range(6):
            for col in range(5):
                tile = tk.Canvas(self.word_frame,background="lightgray",width=50,height=50)
                tile.grid(row=row, column=col, padx=5, pady=7, sticky='')
                text_id = tile.create_text(25,25,text='')
                self.word_rows[row][col] = (text_id,tile)

    def _onKeyEntered(self, event):
        print(self.current_row, self.current_col)
        #Get current cell

        if event.keysym == "BackSpace":
            if self.current_col > 0 and self.current_row < 6:
                id, tile = self.word_rows[self.current_row][self.current_col]
                self.current_col = max(self.current_col-1, 0)
                tile.itemconfig(id, text = '')
            
        elif event.keysym == "Return":
            if self.current_col == 5 and self.current_row < 6:
                #Set the row to the next one over. Set the col to 0
                self.current_row += 1
                self.current_col = 0
        else:
            if event.char.isalpha():
                if self.current_col < 5 and self.current_row < 6:
                    id, tile = self.word_rows[self.current_row][self.current_col]
                    tile.itemconfig(id, text=event.char.upper())
                    self.current_col += 1 
    
    def _add_event_binding(self):
        self.root.bind("<Key>",self._onKeyEntered)
                

client = WordleClient()
a = UserInterface(client)
