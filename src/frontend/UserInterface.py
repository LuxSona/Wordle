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
        self.word_rows = [[(None, None)]*5]*6
        self.current_row = 0
        self.current_col = 0

        self._initalizeRows()
        self.word_frame.pack(fill="y",expand=True)
        self.button_panel.pack()
        self.root.mainloop()
        self._add_event_binding()
    
    def _initalizeRows(self):
        """Initializes the word grid rows for the interface.
        """
        for row in range(6):
            for col in range(5):
                tile = tk.Canvas(self.word_frame,background="lightgray",width=50,height=50)
                tile.grid(row=row, column=col, padx=5, pady=7, sticky='')
                text_id = tile.create_text(25,25,text='')
                self.word_rows[row][col] = (text_id,tile)

    
    def _add_event_binding(self):
        def _onKeyEntered(self):
            ...

client = WordleClient()
a = UserInterface(client)
