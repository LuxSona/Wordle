from . import utils
import random 

class Server():
    """Server class for handling the wordle implementation
    """    
    def __init__(self, word : str | None = None):
        self.wordlist = utils.getWords()
        self.guesses = 6
        self.word = random.choice(self.wordlist) if word is None else word.lower()
        self.letter_counts = utils.getFrequencies(self.word)
    
    
    def guess(self, guessed: str, debug=False) -> tuple[list[chr], str]:
        """Given a guess, returns either how close that guess is and an exit code. 
        Codes look like this:
            'INCOMPLETE' - Unsuccessful guess
            'SUCCESS' - Successful guess
            '1' - Error code for bad length word
            '2' - Error code for non alphabetical guess
            '3' - Out of guesses

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
            return ['R']*5, '1'
        
        if any(not(x.isalpha()) for x in guessed_list):
            #Guess must be alphabetic.
            return ['R']*5, '2'

        if self.guesses <= 0:
            return ['R']*5, '3'
            
        success = (guessed == self.word)
        if success:
            #Don't even bother
            return ['G']*5, 'SUCCESS'
    
        result = ['R']*5
        counts = self.letter_counts.copy()

        #Collect all letters that correspond one-to-one with the secret word.
        #First pass
        for i, (a, b) in enumerate(zip(guessed_list, list(self.word))):
            if a == b:
                result[i] = 'G'
                #We know that a exists in frequency
                counts[a] -= 1 
            elif counts.get(a, 0) != 0:
                #If we've already placed a T and that pushed it to 0, we don't even have to worry about it. Else, assume yellow
                result[i] = 'Y'
        
        #Second pass, turn yellows to grays
        for i, (letter_guessed,result_color) in enumerate(zip(guessed_list, result)):
            if result_color != 'Y':
                #Don't even bother
                continue 
            #Color should be 'Y' now
            if counts.get(letter_guessed,0) == 0:
                #TODO // Is this safe? We're mutating a list in the middle of a for-loop. It *should* be okay, but maybe let's double check.
                result[i] = 'R'
            else:
                counts[letter_guessed] -= 1
        #Decrement guesses
        if not debug:
            self.guesses -= 1
        #Results should be through
        return result, 'INCOMPLETE'
    
    def reset(self, word : str | None = None):
        """Resets the game

        :param word: If we want a specific word, reset with that word. Else, reset randomly.
        :type word: str | None
        """
        self.guesses = 6
        self.word = random.choice(self.wordlist) if word is None else word.lower()
        self.letter_counts = utils.getFrequencies(self.word)

    def setWord(self, word : str) -> tuple[str, str]:
        """Sets to new word

        :param word: The new word to set
        :type word: str
        """
        if len(word) != 5:
            #Must be a five letter word.
            return self.word, '1'
        
        if any(not(x.isalpha()) for x in word):
            #Guess must be alphabetic.
            return self.word, '2'

        self.word = word.lower()
        self.letter_counts = utils.getFrequencies(word)
        return self.word, 'SUCCESS'
    