from . import utils, server
import socket
import logging 

logger = logging.getLogger(__name__)


def main():
    """Main driving code to handle requests and such.

    Uses socket communication
    """


    #Create a server for our Wordle logic.
    wordle_server = server.Server()
    
    #Default port is 12255
    port = 12255 
    with socket.socket() as s:
        logger.info("[INFO] SOCKET CREATED")        
        s.bind(('127.0.0.1', port))
        #Listen
        s.listen(5)
        logger.info(f"[INFO] LISTENING ON PORT {port}")
        while True:
            c, addr = s.accept()
            logger.info(f"[INFO] GOT CONNECTION FROM {addr}")
            c.send("ALIVE".encode())
            c.close()
            logger.info("[INFO] CLOSING CONNECTION")
            break 


