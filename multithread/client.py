import socket

def connect_to_server(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostbyname(socket.gethostname()), 8080))

    
    message = "Pode me prestar um serviço?"
    client.send(message.encode("utf-8"))
        
    try: 
        message_from_server = client.recv(128).decode("utf-8")
        print("Mensagem do Servidor: {}\n".format(message_from_server))
    except BrokenPipeError:
        pass

connect_to_server()