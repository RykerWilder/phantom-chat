from colorama import Fore, Style
from phantom_chat.modules import P2P
from phantom_chat.utils import print_welcome_message, exit
import threading
import signal

def main():
    # ctrl+c handler
    signal.signal(signal.SIGINT, exit)

    print_welcome_message()

    print(f"""
        [{Fore.BLUE}1{Style.RESET_ALL}] P2P pattern (recommended)
        [{Fore.BLUE}2{Style.RESET_ALL}] Server - Client pattern
    """)

    choice = input(f"{Fore.GREEN}[?] {Style.RESET_ALL} Select your choice =>")

    if choice == "1":
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} You choose P2P. You can be a host or a client only in your network.")
        print(f"{Fore.YELLOW}[!] Waiting to connect.{Style.RESET_ALL}")

        P2P().P2P_manager()
    elif choice == "2":
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} You choose public host.")
    else:
        print(f"{Fore.RED}[X] Invalid choice.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()