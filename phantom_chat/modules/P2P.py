from colorama import Style, Fore
from phantom_chat import get_local_ip
import rsa
import socket
import threading
import sys

class P2P:

    # KEYS GENERATION
    public_key, private_key = rsa.newkeys(1024)

    # IP ADDRESS
    port = 9999
    ip_address = input(f"{Fore.BLUE}[INFO]{Style.RESET_ALL}Your local IP is =>{Fore.BLUE}{get_local_ip()}{Style.RESET_ALL}")
    while True:
        choiceP2P = input("Choose the mod: Host [1] or Client [2]: ")
        if choiceP2P in ["1", "2"]:
            break
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")

    # START CONNECTION
    if choiceP2P == "1":
        client, public_partner = self.create_host(ip_address, port, public_key)
    else:
        client, public_partner = self.create_connection(ip_address, port, public_key)

    print(f"""
        {Fore.GREEN}Connection established!{Style.RESET_ALL}
        {Fore.YELLOW}Digit \"/exit\"{Style.RESET_ALL} to exit.
    """)

    # SENDING AND RECEIVING
    send_thread = threading.Thread(target=sending_messages, args=(client, public_partner))
    receive_thread = threading.Thread(target=receiving_messages, args=(client, private_key))

    send_thread.daemon = True
    receive_thread.daemon = True

    send_thread.start()
    receive_thread.start()


    def create_host(self, ip_addr, port, public_key):
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

    def create_connection(self, ip_addr, port, public_key):

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

    def sending_messages(self, client, public_partner):

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

    def receiving_messages(self, client, private_key):

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