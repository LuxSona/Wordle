import pytest 
import socket 
import multiprocessing
import time 
import src.server.main as main 
from src.utils import utils
#Test socket connection
def run_server():
    main.main()

@pytest.fixture(scope="module")
def run_server_in_separate_process():
    proc = multiprocessing.Process(target=run_server,daemon=True)
    proc.start()
    time.sleep(1)
    #Yield
    yield proc 

    #Closing tasks.
    proc.terminate()
    proc.join(timeout=2)
    if proc.is_alive():
        proc.kill()


@pytest.mark.timeout(60)
def test_server(run_server_in_separate_process):
    port = 12255
    time.sleep(1)
    with socket.socket() as s, s.makefile('r',encoding='utf-8',newline='\n') as f:
        s.connect(('127.0.0.1', port))
        
        data = utils.recv_message(f)
        assert data == "READY"

        s.sendall("G,H1LLO\n".encode())
        resp = utils.recv_message(f)
        assert resp == "ERROR;GUESS 2"
        print("First test")

        #Check length
        s.sendall("G,HELLOO\n".encode())
        resp = utils.recv_message(f)
        assert resp == "ERROR;GUESS 1"
        print("Second test")

        #Check empty
        s.sendall("G\n".encode())
        resp = utils.recv_message(f)
        assert resp == "ERROR;COMMAND"
        print("Third test")

        #Check out_of_guesses
        for _ in range(6):
            s.sendall("G,ZYZZX\n".encode())
            #Wait
            utils.recv_message(f)
            time.sleep(0.5)
        s.sendall("G,ZZYZX\n".encode())
        resp =utils.recv_message(f)
        assert resp == "ERROR;GUESS 3"
        print("Fourth test")

        #Check reset
        s.sendall("R\n".encode())
        resp =utils.recv_message(f)
        assert resp == "RESET"
        print("Fifth test")

        #Check set empty
        s.sendall("S\n".encode())
        resp =utils.recv_message(f)
        assert resp == "ERROR;SET COMMAND"
        print("Sixth test")

        #Check set with bad values
        s.sendall("S,HELLOO\n".encode())
        resp =utils.recv_message(f)
        assert resp == "ERROR;SET 1"
        print("Seventh test")

        s.sendall("S,H1LLO\n".encode())
        resp =utils.recv_message(f)
        assert resp == "ERROR;SET 2"
        print("Eight test")

        #Check set works with good values
        s.sendall("S,HELLO\n".encode())
        resp = utils.recv_message(f)
        assert resp == "SET;hello"
        print("Ninth test")

        s.sendall("T\n".encode())
        resp = utils.recv_message(f)
        assert resp == "WORD;hello"
        print("Tenth test")

        #Check guess works with good but inaccurate values
        s.sendall("G,HILLO\n".encode())
        resp =utils.recv_message(f)
        assert resp == "GUESS_AGAIN;G,R,G,G,G"
        print("Eleventh test")

        #Check guess works with good and accurate values
        s.sendall("G,HELLO\n".encode())
        resp =utils.recv_message(f)
        assert resp == "SUCCESS"
        print("Twelvth test")

        #Check quit works
        s.sendall("Q\n".encode())
        resp =utils.recv_message(f)
        assert resp == "QUIT"
        print("Thirteenth test")
