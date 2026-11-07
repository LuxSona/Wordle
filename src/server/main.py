from . import utils, server
import socket
import logging 

logger = logging.getLogger(__name__)
def main():
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
            c.send("CONNECTION RECIEVED".encode())
            c.close()
            break 
