import tkinter as tk
from tkinter import messagebox
from .WordleClient import WordleClient
from collections.abc import Callable

class UserInterface():
    """The user interface class
    """     
    def __init__(self, on_guess : Callable[[str], None], on_reset: Callable, on_quit: Callable, root : tk.Tk, word : str):
        """The initialization function for the wordle interface class.

        :param client: A reference to the client connection handler
        :type client: WordleClient
        """        
        #Root pane and callables
        self.word = word 
        self.root = root
        self.on_guess = on_guess
        self.on_reset = on_reset
        self.on_quit = on_quit
        self.COLOR_DICTIONARY = {'G': "chartreuse", 'Y': "goldenrod1", 'R': "gray57"}
        #Heading table. 
        self.heading_table = tk.Frame(self.root, width=150,height=100)
        self.title = tk.Label(self.heading_table, text="WORDLE v. 0.1.1", font=("Franklin Gothic", 24, "bold"))
        self.title.pack()
        #Set up letters available
        self.letters_available = tk.Frame(self.root, width=150,height=300)
        self.letters_to_tiles = {}
        self.letters_to_colors = {}

        self.initialize_letters()

        self.word_frame = tk.Frame(self.root, width=150, height=300)
        self.root.geometry("600x700")
        #Rows and words
        self.ROW_COUNT = 6
        self.word_rows : list[list[tuple[int | None, tk.Canvas | None]]] = [[(None, None) for _ in range(5)] for _ in range(6)]
        self.current_row = 0
        self.current_col = 0
        self.current_row_word : list[str] = []
    
        self._initalizeRows()
        self._add_event_binding()
        self.heading_table.pack()
        self.word_frame.pack(fill="y",expand=True)
        self.letters_available.pack(fill="y",expand=True)

    def show_win(self):
        self.color_row(['G','G','G','G','G'])
        response = messagebox.askyesno("Win!",f"You won in {self.current_row+1} guesses! Would you like to play again?")
        if response:
            self.reset()
            self.on_reset()
        else:
            self.on_quit()
    
    def show_lose(self):
        response = messagebox.askyesno("Lose", f"Sorry! The word was {self.word}. Would you like to play again?")
        if response:
            self.on_reset()
        else:
            self.on_quit()
    
    def color_row(self, colors : list[str]):
        for col, color in enumerate(colors):
            _, tile = self.word_rows[self.current_row][col]
            tile.configure(bg=self.COLOR_DICTIONARY[color])
    
    def color_letters(self, colors : list[str]):
        for letter, color in zip(self.current_row_word, colors):
            if self.letters_to_colors[letter]  != "chartreuse":
                self.letters_to_colors[letter] = self.COLOR_DICTIONARY[color] 
                self.letters_to_tiles[letter].configure(bg=self.COLOR_DICTIONARY[color])

        
    def initialize_letters(self):
        """Initializes the letters

        """
        keyboard_row1 = "qwertyuiop"
        keyboard_row2 = "asdfghjkl"
        keyboard_row3 = "zxcvbnm"
        top_row = tk.Frame(self.letters_available,width=10*25)
        mid_row = tk.Frame(self.letters_available, width=9*25)
        bottom_row = tk.Frame(self.letters_available, width=7*25)
        
        #First row
        for letter in keyboard_row1:
            letter_tile = tk.Canvas(top_row, background="lightgray", width=25, height=50)
            letter_tile.create_text(13,25,text=letter)
            self.letters_to_tiles[letter] = letter_tile
            self.letters_to_colors[letter] = "lightgray"
            letter_tile.pack(side="right",padx=1)
        
        #Second row
        for letter in keyboard_row2:
            letter_tile = tk.Canvas(mid_row, background="lightgray", width=25, height=50)
            letter_tile.create_text(13,25,text=letter)
            self.letters_to_tiles[letter] = letter_tile
            self.letters_to_colors[letter] = "lightgray"
            letter_tile.pack(side="right",padx=1)
        
        for letter in keyboard_row3:
            letter_tile = tk.Canvas(bottom_row, background="lightgray", width=25, height=50)
            letter_tile.create_text(13,25,text=letter)
            self.letters_to_tiles[letter] = letter_tile
            self.letters_to_colors[letter] = "lightgray"
            letter_tile.pack(side="right",padx=1)
        
        top_row.pack()
        mid_row.pack()
        bottom_row.pack()
    

    def _initalizeRows(self):
        """Initializes the word grid rows for the interface.
        """
        for row in range(6):
            for col in range(5):
                tile = tk.Canvas(self.word_frame,background="lightgray",width=50,height=50)
                tile.grid(row=row, column=col, padx=5, pady=7, sticky='')
                text_id = tile.create_text(25,25,text='')
                self.word_rows[row][col] = (text_id,tile)
    
    def accepted(self, colors : list[str]):
        #Accepted a guess.
        self.color_row(colors)
        self.color_letters(colors)
        if self.current_row < 6:
            self.current_col = 0
            self.current_row += 1
            self.current_row_word = []
        if self.current_row == 6:
            self.show_lose()
        
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
                returned_word = "".join(self.current_row_word)
                self.on_guess(returned_word)
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
        self.current_row_word = []
        for letter in "qwertyuiopasdfghjklzxcvbnm":
            tile = self.letters_to_tiles[letter].configure(bg ="lightgray")
            self.letters_to_colors[letter] = "lightgray"
    
    
    def show_error(self, error_type : str, error_code : str):
        error_messages = {
            "1": "Your guessed word is shorter than the allowed FIVE letters",
            "2": "Your guessed word has invalid characters.",
            "3": "You've run out of guesses",
            "COMMAND": "Somehow, an internal error has occurred. Check the logs",
            "UNK": "An unknown error has occurred. Check the logs."}
        resp = messagebox.askyesno("ERROR",f"You made an error during {error_type}: {error_messages[error_code]}. Do you wish to reset? No will quit.")
        if resp:
            self.on_reset()
        else:
            self.on_quit()

