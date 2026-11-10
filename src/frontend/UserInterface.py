import tkinter as tk 
from .WordleClient import WordleClient
from collections.abc import Callable

class UserInterface():
    """The user interface class
    """     
    def __init__(self, on_guess : Callable[[str]], on_reset: Callable, on_quit: Callable):
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
        #Rows and words
        self.ROW_COUNT = 6
        self.word_rows : list[list[tuple[int | None, tk.Canvas | None]]] = [[(None, None) for _ in range(5)] for _ in range(6)]
        self.current_row = 0
        self.current_col = 0
        self.current_row_word : list[str] = []
    
        self._initalizeRows()
        self._add_event_binding()
        self.word_frame.pack(fill="y",expand=True)
        self.button_panel.pack()
        self.root.mainloop()
    
    def show_dialog(self, text: str):
        ...
    
    def color_row(self, colors : list[str]):
        ...
    
    
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
                self.current_col -= 1
                id, tile = self.word_rows[self.current_row][self.current_col]
                tile.itemconfig(id, text = '')
                self.current_row_word.pop()
            
        elif event.keysym == "Return":
            if self.current_col == 5 and self.current_row < 6:
                #Set the row to the next one over. Set the col to 0
                self.current_row += 1
                self.current_col = 0
                returned_word = "".join(self.current_row_word)
                print(returned_word)
                self.current_row_word = []
        else:
            if event.char.isalpha():
                if self.current_col < 5 and self.current_row < 6:
                    id, tile = self.word_rows[self.current_row][self.current_col]
                    tile.itemconfig(id, text=event.char.upper())
                    self.current_col += 1
                    self.current_row_word.append(event.char.lower())
    
    def _add_event_binding(self):
        self.root.bind("<Key>",self._onKeyEntered)
    
    def reset(self):
        self.current_col = 0
        self.current_row = 0
        for row in self.word_rows:
            for id, tile in row:
                tile.itemconfig(id, text="")
                tile.configure(bg="lightgray")
    
    def show_win(self):
        ...

client = WordleClient()
a = UserInterface(client)
