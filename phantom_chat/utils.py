import socket
from colorama import Style, Fore
import sys

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"  # Fallback a localhost
        

def cleanup(instance):
    if not instance.running:
        return
            
    instance.running = False
    if instance.client:
        try:
            instance.client.shutdown(socket.SHUT_RDWR)
            instance.client.close()
        except:
            pass
    print(f"\n{Fore.BLUE}[INFO]{Style.RESET_ALL} Connection closed{Style.RESET_ALL}")
    sys.exit(0)

def exit(signum, frame):
    print(f"\n{Fore.RED}[X] Phantom Chat closed{Style.RESET_ALL}")
    sys.exit(0)

def print_welcome_message():
    print(r""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀__________.__                   __                  
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠄⠀⠀⠄⠀⠀⠀\______   \  |__ _____    _____/  |_  ____   _____  
⠀⠀⠀⠀⢀⠀⠀⠀⠀⣸⣦⣸⣧⣼⣿⣦⣄⣀⣈⣴⣾⣿⣿⣦⡐⠄⠀⠀|     ___/  |  \\__  \  /    \   __\/  _ \ /     \ 
⠀⢠⣶⣶⣦⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀|    |   |   Y  \/ __ \|   |  \  | (  <_> )  Y Y  \
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⡀|____|   |___|  (____  /___|  /__|  \____/|__|_|  /
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢠⠀             \/     \/     \/                  \/ 
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡙⢿⡿⠛⢿⣿⣿⣿⠀⠀_________ .__            __                       
⠀⠄⢿⣿⣿⣿⡿⠿⣿⡿⠉⠙⣿⣿⣿⣿⣿⡇⢘⠐⠨⠄⠁⠄⢻⣿⣿⠀⠀\_   ___ \|  |__ _____ _/  |_                     
⠀⠀⡈⢿⣿⣿⡇⠆⠈⠃⠃⠁⠸⣿⣿⣿⣿⣷⢸⠀⠀⠀⠀⠈⡈⢿⡿⢀⠀/    \  \/|  |  \\__  \\   __\                    
⠀⠀⠀⠄⠻⣿⣇⠠⠀⠀⠀⠀⠂⢹⣿⣿⣿⣿⠈⠀⠀⠀⠀⠀⢀⠸⠋⠄⠀\     \___|   Y  \/ __ \|  |                      
⠀⠀⠀⠀⠀⠈⠻⡆⠀⠀⠀⠀⠈⠄⢿⣿⣿⣿⡆⠂⠀⠀⠀⠀⠀⠀⠈⠀⠀ \______  /___|  (____  /__|                      
⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠈⠄⢻⣿⣿⣧⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       \/     \/     \/                          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠹⣿⣿⡆⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢿⣿⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀                                                 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡙⠳⠈⠀⠀⠀⠀⠀⠀⠀⠀                                                 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 ⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                       
    """)