import threading
import socket
host = socket.gethostname()
port = 9999
Format="utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

#broadcast message from server to all client
def publish(message):
    for client in clients:
        client.send(message)
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            publish(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            publish(f'{alias} has left the group!'.encode(Format))
            aliases.remove(alias)
            break

def receive():
    while True:
        print('Server is waiting for another client ')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode(Format))
        alias = client.recv(1024).decode(Format)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode(Format))
        publish(f'{alias} has connected to the group'.encode(Format))
        client.send('you are now connected!'.encode(Format))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive()