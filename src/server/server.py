from . import utils
import random 

class Server():
    """Server class for handling the wordle implementation
    """    
    def __init__(self, word : str | None = None):
        self.wordlist = utils.getWords()
        self.guesses = 6
        self.word = random.choice(self.wordlist) if word is None else word
        self.letter_counts = utils.getFrequencies(self.word)
    
    
    def guess(self, guessed: str) -> tuple[list[chr], chr]:
        """Given a guess, returns either how close that guess is and an exit code. 
        Codes look like this:
            'I' - Unsuccesful guess
            'S' - Successful guess
            '1' - Error code for bad length word
            '2' - Error code for non alphabetical guess

        :param guessed: The word guessed
        :type guessed: str
        :return: The guess result and the code.
        :rtype: tuple[list[chr], chr]
        """
        #Make sure guessed is lower
        guessed = guessed.lower()
        guessed_list = list(guessed)
        if len(guessed) != 5:
            #Must be a five letter word.
            return ['N','N','N','N','N'], '1'
        
        if any(not(x.isalpha()) for x in guessed_list):
            #Guess must be alphabetic.
            return ['N','N','N','N','N'], '2'
        
        result = []
        counts = self.letter_counts.copy()
        success = True
        for (a, b) in zip(guessed_list, list(self.word)):
            if a == b and counts.get(a,0) != 0:
                result.append('T')
                counts[a] = counts[a] - 1
            elif counts.get(a,0) != 0:
                result.append('E')
                success = False 
                counts[a] = counts[a] - 1 
            else:
                success = False
                result.append('N')
        code = 'S' if success else 'I'
        return result, code
    
    def setWord(self, word : str):
        """Sets to new word

        :param word: The new word to set
        :type word: str
        """
        self.word = word 
        self.letter_counts = utils.getFrequencies(word)
    