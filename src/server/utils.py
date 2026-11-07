from importlib.resources import files 
from random import choice

def getWords() -> list[str]:
    """Opens the wordlist as a list of strings.

    :return: A list of strings representing our wordlist.
    :rtype: list[str]
    """    
    resources = files("src.server.resources").joinpath("wordlist.txt").read_text(encoding='utf-8')
    return resources.split('\n')[:-1]


def getFrequencies(word : str) -> dict:
    """Gets the frequencies of letters

    :param word: The word to test
    :type word: str
    :return: Dictionary containing letters and frequencies.
    :rtype: dict
    """ 
    letter_counts = {}       
    for letter in word:
        if not letter.isalpha():
            return {}
        
        freq = letter_counts.get(letter.lower(), 0)
        letter_counts[letter.lower()] = freq + 1
    return letter_counts
