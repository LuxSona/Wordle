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
    
    
    def guess(self, guessed: str) -> list[chr]:
        """Returns the value of a guess

        :param guessed: The word guessed
        :type guessed: str
        :return: A list of characters, [c,c,c,c,c], where c is either T, when a letter is placed right, E, where a letter is placed wrong but present, and N, where the letter is not present. May return ['1'] for ne 5 or ['2'] for numbers
        :rtype: list[chr]
        """
        #Make sure guessed is lower
        guessed = guessed.lower()
        guessed_list = list(guessed)
        if len(guessed) != 5:
            #Must be a five letter word.
            return ['1']
        
        if any(not(x.isalpha()) for x in guessed_list):
            #Guess must be alphabetic.
            return ['2']
        
        result = []
        counts = self.letter_counts.copy()
        for (a, b) in zip(guessed_list, list(self.word)):
            if a == b and counts.get(a,0) != 0:
                result.append('T')
                counts[a] = counts[a] - 1
            elif counts.get(a,0) != 0:
                result.append('E')
                counts[a] = counts[a] - 1 
            else:
                result.append('N')
        return result 
    
    def setWord(self, word : str):
        """Sets to new word

        :param word: The new word to set
        :type word: str
        """
        self.word = word 
        self.letter_counts = utils.getFrequencies(word)
        

def main():
    c = utils.getWords()
    print(c)

main()
