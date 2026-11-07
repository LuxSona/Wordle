from . import utils as wp
import random 

class Server():
    """Server class for handling the wordle implementation
    """    
    def __init__(self, word : str | None = None):
        self.wordlist = wp.getWords()
        self.guesses = 6
        self.word = random.choice(self.wordlist) if word is None else word
        self.letter_counts = self._getFrequencies(self.word)
    
    def _getFrequencies(self, word : str) -> dict:
        """Gets the frequencies of letters

        :param word: The word to test
        :type word: str
        :return: Dictionary containing letters and frequencies.
        :rtype: dict
        """ 
        letter_counts = {}       
        for letter in word:
            freq = letter_counts.get(letter, 0)
            letter_counts[letter] = freq + 1
        return letter_counts
    
    def guess(self, guessed: str) -> list[chr]:
        """Returns the value of a guess

        :param guessed: The word guessed
        :type guessed: str
        :return: A list of characters, [c,c,c,c,c], where c is either T, when a letter is placed right, E, where a letter is placed wrong but present, and N, where the letter is not present. May return ['1'] for 
        :rtype: list[chr]
        """
        guessed_list = list(guessed)
        if len(guessed) != 5:
            #Must be a five letter word.
            return ['1']
        
        if any(not(x.isalpha()) for x in guessed_list):
            #Guess must be alphabetic.
            return ['2']
        
        


def main():
    c = wp.getWords()
    print(c)

main()
