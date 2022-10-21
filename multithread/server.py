import socket
import threading
import time

def handle_client(conn, addr):
    print("connectado ao endereço: {}".format(addr))
    message_from_client = conn.recv(128).decode("utf-8")
    print("Mensagem do client: {} \n".format(message_from_client))
    message_to_client = "Serviço prestado"
    conn.send(message_to_client.encode("utf-8"))
    time.sleep(10)
    conn.close()

def init_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname(socket.gethostname()), 8080))
    server.listen()
    print("Servidor Rodando")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print("Numero de threads: {}\n".format(threading.activeCount()))
        thread.start()

init_server()