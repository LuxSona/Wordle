import socket 
import queue 
from src.utils import utils

class WordleClient():
    def __init__(self):
        self.message_queue = queue.Queue()
        self.PORT = 12255
        self.log = []
    
    def quit(self):
        ...
    
    def send(self, message : str) -> str | None:
        with socket.socket() as s, s.makefile('r',encoding='utf-8',newline='\n') as f:
            s.connect(('127.0.0.1', self.PORT))
            data = utils.recv_message(f)
            if not message.endswith("\n"):
                message = f"{message}\n"
            if data == "READY":
                s.sendall(message.encode())
                resp = utils.recv_message(f)
                return resp
    
    def reset(self):
        ...

