import rsa
import socket
import threading

public_key, private_key = rsa.newkeys(1024)  # 1024 bit keys size
public_partner = None

choice = input("Do you want to host[1] or to connect[2]?: ")
ip_address = "192.168.1.38"
port = 9999


if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, port))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

    print(f"Server is running on {ip_address}:{port}")

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_address, port))

    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    print(f"Connected successfully on {ip_address}:{port}")


def sending_messages(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You: " + message)

def receiving_messages(c):
    while True:
        print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()