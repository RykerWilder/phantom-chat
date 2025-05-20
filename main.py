import rsa
import socket
import threading

choice = input("Do you want to host[1] or to connect[2]?: ")

if choice == "1":
    server = socket.socket(socket.AFI_INET, socket.SOCK_STREAM)
    server.bind(("IP ADDRESS", 9999))
    server.listen()

    print("Server is listening...")

    client, _ = server.accept()
elif choice == "2":
    client = socket.socket(socket.AFI_INET, socket.SOCK_STREAM)
    client.connect(("IP ADDRESS", 9999))
    print("Connected successfully!")
else:
    print("Invalid choice")