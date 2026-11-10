from .UserInterface import UserInterface
from .WordleClient import WordleClient
import tkinter as tk
import threading 
import queue 

class Controller():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.client = WordleClient()
        self.secret_word = self.client.send("T\n").split(';')[1]
        self.ui = UserInterface(self._enqueueGuess, self._reset, self._on_quit, self.root, self.secret_word)
        self.inbox = queue.Queue() 
        self.outbox = queue.Queue()
        self.io_thread = threading.Thread(target=self._worker_thread, daemon=True)
        self.io_thread.start()
        self.root.protocol("WM_DELETE_WINDOW", self._on_quit)
        self.poll_queue()
    

    def _on_quit(self):
        self.client.send("Q\n")
        self.root.destroy()

    def quit(self):
        self.root.quit()

    def handle_message(self, message : str):
        print(f"MESSAGE {message}")
        #We have a million kinds of messages that we can recieve, but let's start with the most basic
        if message is None:
            self.root.quit()
        message_parts = message.split(';')
        command = message_parts[0]
        match command:
            case "GUESS_AGAIN":
                colors = message_parts[1].split(',')
                self.ui.accepted(colors)
            case "SUCCESS":
                self.ui.show_win()
            case "QUIT":
                self.quit()
            case "ERROR":
                error_type = message_parts[1]
                error_code = message_parts[2]

                self.ui.show_error(error_type, error_code)
            case "RESET":
                self.ui.reset()
                #Get the secret word again
                resp = self.client.send("T")
                self.word = resp.split(';')[1]
                self.ui.word = self.word

            #These branches shouldn't be used at all
            case "SET":
                pass
                #These won't be used at all.
            case "WORD":
                pass
            case _:
                pass 

        
    def poll_queue(self):
        try:
            while True:
                in_message = self.inbox.get_nowait()
                self.handle_message(in_message)
        except queue.Empty:
            pass
    
        self.root.after(100, self.poll_queue)
    
    def _worker_thread(self):
        while True:
            try:
                sendoff = self.outbox.get()
                resp = self.client.send(sendoff)
                self.inbox.put(resp)
            except queue.Empty:
                pass 

    def _enqueueGuess(self, word : str):
        print(f"GUESSING {word}")
        """Handles the guess on the part of the wordle client

        :param word: The word to send
        :type word: string
        """
        self.outbox.put(f"G,{word}\n")
    
    
    def _reset(self):
        self.outbox.put("R")
    
