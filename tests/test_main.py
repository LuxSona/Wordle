import pytest 
import socket 
import multiprocessing
import time 
import src.server.main as main 

#Test socket connection
def run_server():
    main.main()

@pytest.fixture(scope="class")
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


@pytest.mark.timeout(5)
def test_server(run_server_in_separate_process):
    port = 12255
    time.sleep(10)
    # with socket.socket() as s:
    #     s.connect(('127.0.0.1', port))
    #     data = s.recv(1024)
    #     assert data.decode() == "ALIVE"
