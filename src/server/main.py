from ..utils import utils

from . import server
import socket
import logging 

logger = logging.getLogger(__name__)


def main():
    """Main driving code to handle requests and such.

    Uses socket communication
    """

    #Create a server for our Wordle logic.
    wordle_server = server.Server()
    print(wordle_server.word)
    #Default port is 12255
    port = 12255 
    with socket.socket() as s:
        #Set timeout to something else for testing.
        s.settimeout(1)
        logger.info("[INFO] SOCKET CREATED")
        s.bind(('127.0.0.1', port))
        #Listen
        s.listen(5)
        logger.info(f"[INFO] LISTENING ON PORT {port}")
        try:
            while True:
                try:
                    c, addr = s.accept()
                except TimeoutError:
                    continue
                logger.info(f"[INFO] GOT CONNECTION FROM {addr}")
                with c, c.makefile("r", encoding='utf-8', newline='\n') as f:
                    c.sendall("READY\n".encode())
                    try:
                        while True:
                            #We are now ready to recieve
                            data = utils.recv_message(f)
                            if not data:
                                logger.info("[INFO] CLIENT DISCONNECTED")
                                break 
                                
                            response = handleData(wordle_server, data)
                            c.sendall(response.encode())
                            if response == "QUIT\n":
                                logger.info(f"[INFO] {addr} HAS QUIT.")
                                wordle_server.reset()
                                c.close()
                                break
                    except (TimeoutError, ConnectionError):
                        logger.info(f"[INFO] CLIENT {addr} TIMED OUT / DISCONNECTED")
        except TimeoutError:
            logger.info("[INFO] TIMEOUT")
        except KeyboardInterrupt:
            logger.info("[INFO] SERVER STOPPED BY USER")
        
            
        
                


def handleData(wordle_server: server.Server, data : str) -> str:
    print(f"DATA {data}")
    """
    Handles data sent in by client.

    Example data:

    "G,HELLO"
    "Q"
    "R"

    :param wordle_server: The server that we're accessing
    :type wordle_server: server.Server
    :param data: The data that we're handling.
    :type data: str
    :return: the response that this server should provide.
    :rtype str:
    """
    commands = data.split(',')
    match commands[0]:
        case 'T':
            word = wordle_server.word
            return f"WORD;{word}\n"
        case 'G':
            if len(commands) < 2:
                return "ERROR;GUESS;COMMAND\n"
            resp, code = wordle_server.guess(commands[1])
            if code == '1' or code == '2' or code == '3':
                return f"ERROR;GUESS;{code}\n"
            if code == 'SUCCESS':
                return f"{code}\n" 
            else:
                return f"GUESS_AGAIN;{','.join(resp)}\n"
        case 'R':
            wordle_server.reset()
            return "RESET\n"
        case 'Q':
            #Quit
            return "QUIT\n"
        case 'S':
            if len(commands) < 2:
                return "ERROR;SET;COMMAND\n"
            w,c = wordle_server.setWord(commands[1])
            if c == '1' or c == '2':
                return f"ERROR;SET;{c}\n"
            return f"SET;{w}\n" 
        case _:
            return "ERROR;UNK;UNK\n"



if __name__ == "__main__":
    main()
