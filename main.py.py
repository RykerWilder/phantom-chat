import rsa
import socket
import threading
import sys

def create_host(ip_addr, port, public_key):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((ip_addr, port))
        server.listen()
        print(f"Server in ascolto su {ip_addr}:{port}")
        
        client, client_address = server.accept()
        print(f"Connessione stabilita con {client_address[0]}:{client_address[1]}")
        
        # Invio della chiave pubblica
        client.send(public_key.save_pkcs1("PEM"))
        
        # Ricezione della chiave pubblica del partner
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        print("Scambio di chiavi completato")
        
        return client, public_partner
    except Exception as e:
        print(f"Errore durante la creazione del server: {e}")
        sys.exit(1)

def create_connection(ip_addr, port, public_key):
    """Crea una connessione come client verso un host"""
    print(f"Tentativo di connessione a {ip_addr}:{port}...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip_addr, port))
        print("Connessione stabilita!")
        
        # Invio della chiave pubblica
        client.send(public_key.save_pkcs1("PEM"))
        
        # Ricezione della chiave pubblica del partner
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        print("Scambio di chiavi completato")
        
        return client, public_partner
    except Exception as e:
        print(f"Errore durante la connessione: {e}")
        sys.exit(1)

def sending_messages(client, public_partner):
    """Gestisce l'invio dei messaggi"""
    try:
        while True:
            message = input("")
            # Verifica se l'utente vuole uscire
            if message.lower() == "/exit":
                print("Disconnessione in corso...")
                break
                
            # Cripta e invia il messaggio
            encrypted_message = rsa.encrypt(message.encode(), public_partner)
            client.send(encrypted_message)
            print(f"Tu: {message}")
    except Exception as e:
        print(f"Errore durante l'invio dei messaggi: {e}")
    finally:
        # Segnala la necessità di chiudere la connessione
        client.close()
        sys.exit(0)

def receiving_messages(client, private_key):
    """Gestisce la ricezione dei messaggi"""
    try:
        while True:
            # Ricezione e decrittazione del messaggio
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                print("Partner disconnesso.")
                break
                
            message = rsa.decrypt(encrypted_message, private_key).decode()
            print(f"Partner: {message}")
    except Exception as e:
        print(f"Errore durante la ricezione dei messaggi: {e}")
    finally:
        # Chiude la connessione
        client.close()
        sys.exit(0)

def main():
    """Funzione principale che gestisce il flusso del programma"""
    # Configurazione
    PORT = 9999
    
    # Generazione delle chiavi RSA
    print("Generazione delle chiavi RSA...")
    public_key, private_key = rsa.newkeys(1024)
    
    # Input dell'indirizzo IP
    default_ip = "192.168.1.38"
    ip_address = input(f"Inserisci l'indirizzo IP (default: {default_ip}): ") or default_ip
    
    # Scelta della modalità
    while True:
        choice = input("Scegli la modalità: Host [1] o Client [2]? ")
        if choice in ["1", "2"]:
            break
        print("Scelta non valida. Inserisci 1 per host o 2 per client.")
    
    # Avvio della connessione
    if choice == "1":
        client, public_partner = create_host(ip_address, PORT, public_key)
    else:
        client, public_partner = create_connection(ip_address, PORT, public_key)
    
    print("Connessione stabilita! Digita /exit per uscire.")
    
    # Avvio dei thread per invio e ricezione
    send_thread = threading.Thread(target=sending_messages, args=(client, public_partner))
    receive_thread = threading.Thread(target=receiving_messages, args=(client, private_key))
    
    # Impostazione dei thread come daemon per chiuderli quando il programma termina
    send_thread.daemon = True
    receive_thread.daemon = True
    
    # Avvio dei thread
    send_thread.start()
    receive_thread.start()
    
    # Attesa della terminazione dei thread
    try:
        send_thread.join()
        receive_thread.join()
    except KeyboardInterrupt:
        print("\nChiusura forzata del programma.")
        sys.exit(0)

if __name__ == "__main__":
    main()