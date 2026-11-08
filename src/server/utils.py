from importlib.resources import files 
from random import choice
import socket

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


def recv_message(f) -> str | None:
    """Recieves message

    :param socket: The socket which we are recieving from
    :type socket: socket.socket
    :raises ConnectionError: If the server closes connection... there wont be anything sent.
    :return: The message.
    :rtype: str
    """    
    buf = b""
    line = f.readline()
    if not line:
        return None 
    return line.rstrip("\r\n")
