import socket
from colorama import Style, Fore

def get_local_ip():
    try:
        # Temporary socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # public DNS connection
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"{Fore.RED}[X]Error: {e}{Style.RESET_ALL}")
        return None