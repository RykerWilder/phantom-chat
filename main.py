import rsa
import socket
import threading

choice = input("Do you want to host[1] or to connect[2]?: ")
ip_address = "192.168.3.149"

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, 9999))
    server.listen()

    print("Server is listening...")

    client, _ = server.accept()
elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_address, 9999))
    print("Connected successfully!")
else:
    print("Invalid choice, retry")


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)

def receiving_messages(c):
    while True:
        print("Partner: " + c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()