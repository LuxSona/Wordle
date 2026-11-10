import socket 
import queue 

class WordleClient():
    def __init__(self):
        self.message_queue = queue.Queue()
        self.PORT = 12255
        self.log = []
    
    def quit(self):
        ...
    def request_word(self) -> str:
        ...
    def poll_queue(self):
        ...
    
    def guess(self, word:str) -> str:
        ...
