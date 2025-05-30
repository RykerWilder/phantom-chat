from colorama import Fore, Style
import rsa
import socket
import threading
import sys

def create_host(ip_addr, port, public_key):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((ip_addr, port))
        server.listen()
        print(f"Server listening on {Fore.GREEN}{ip_addr}:{port}{Style.RESET_ALL}")
        
        client, client_address = server.accept()
        
        # Invio della chiave pubblica
        client.send(public_key.save_pkcs1("PEM"))
        
        # Ricezione della chiave pubblica del partner
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        
        return client, public_partner
    except Exception as e:
        print(f"Error creating server {e}")
        sys.exit(1)

def create_connection(ip_addr, port, public_key):

    print(f"Attempting to connect to {Fore.YELLOW}{ip_addr}:{port}{Style.RESET_ALL}...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip_addr, port))
        
        # Invio della chiave pubblica
        client.send(public_key.save_pkcs1("PEM"))
        
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        print("Keys exchange completed")
        
        return client, public_partner
    except Exception as e:
        print(f"{Fore.RED}Error while connecting {e}{Style.RESET_ALL}")
        sys.exit(1)

def sending_messages(client, public_partner):

    try:
        while True:
            message = input("")

            # EXIT
            if message.lower() == "/exit":
                print("Disconnection in progress...")
                break
                
            # SEND ENCRYPTED MESSAGE
            encrypted_message = rsa.encrypt(message.encode(), public_partner)
            client.send(encrypted_message)
            print(f"{Fore.YELLOW}You{Style.RESET_ALL}: {message}")
    except Exception as e:
        print(f"{Fore.RED}Error sending message: {e}{Style.RESET_ALL}")
    finally:
        # Close connection
        client.close()
        sys.exit(0)

def receiving_messages(client, private_key):

    try:
        while True:
            # RECEIVE AND DECRYPT MESSAGE
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                print(f"{Fore.RED}Partner disconnected.{Style.RESET_ALL}")
                break
                
            message = rsa.decrypt(encrypted_message, private_key).decode()
            print(f"{Fore.BLUE}Partner{Style.RESET_ALL}: {message}")
    except Exception as e:
        print(f"{Fore.RED}Error receiving message: {e}{Style.RESET_ALL}")
    finally:
        # CLOSE CONNECTION
        client.close()
        sys.exit(0)

def main():

    PORT = 9999
    
    # KEYS GENERATION
    public_key, private_key = rsa.newkeys(1024)

    print("""
        [1] P2P
        [2] Public host
    """)

    choice = input(f"{Fore.GREEN}[?]Select your choice => {Style.RESET_ALL}")

    if choice == "1":
        print("[INFO] You choose P2P. You can be a host or a client only in your network")
        start_P2P()
    


    try:
        send_thread.join()
        receive_thread.join()
    except KeyboardInterrupt:
        print(f"{Fore.RED}Forced closure program.{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()