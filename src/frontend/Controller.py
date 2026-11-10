from .UserInterface import UserInterface
from .WordleClient import WordleClient

class Controller():
    def __init__(self):
        self.client = WordleClient()
        self.ui = UserInterface(self._handleGuess, self._reset, self._quit)
        self.secret_word = self.client.request_word()
    

    def _quit(self):
        self.client.quit()
        
    def _handleGuess(self, word : str):
        """Handles the guess on the part of the wordle client

        :param word: The word to send
        :type word: string
        """        
        response = self.client.guess(word)
        parts = response.split(';')
        if parts[0] == "SUCCESS":
            self.ui.show_win()
        
        elif len(parts) == 1:
            self.ui.show_dialog("Invalid Word!")
        else:
            colors = response[1].split(',')
            self.ui.color_row(colors)
    
    def _reset(self):
        self.ui.reset()
        self.client.reset()
        self.reset()
    
    def reset(self):
        self.secret_word = self.client.request_word()
