import threading
import socket
host = socket.gethostname()
port = 9999
Format="utf-8"
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# recive message from another client
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode(Format)
            if message == "alias?":
                client.send(alias.encode(Format))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break
# send message from another client
def client_send():
    while 21==21:
        message = f'{alias}: {input("")}'
        client.send(message.encode(Format))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()