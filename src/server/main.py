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
            #We are now ready to recieve
            data = c.recv(1024)
            data = data.decode()
            response = handleData(wordle_server, data)
            if response == "QUIT":
                c.send("Goodybe!".encode())
                c.close()
                logger.info("[INFO] CLOSING CONNECTION")
            if response == "ERROR":
                c.send("Error!".encode())
                c.close()
                logger.info("[INFO] CLOSING CONNECTION")
            break


def handleData(wordle_server: server.Server, data : str) -> str:
    """
    Handles data sent in by client.

    :param wordle_server: The server that we're accessing
    :type wordle_server: server.Server
    :param data: The data that we're handling.
    :type data: str
    :return: the response that this server should provide.
    :rtype str:
    """
    commands = data.split(',')
    match commands[0]:
        case 'G':
            if len(commands) < 2:
                return "ERROR"
        case 'Q':
            #Quit
            return "QUIT"
        




