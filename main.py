from colorama import Fore, Style
from phantom_chat.modules import P2P
from phantom_chat.utils import print_welcome_message
import threading

def main():
    print_welcome_message()

    print(f"""
        [{Fore.BLUE}1{Style.RESET_ALL}] P2P
        [{Fore.BLUE}2{Style.RESET_ALL}] Public host
    """)

    choice = input(f"{Fore.GREEN}[?] Select your choice => {Style.RESET_ALL}")

    if choice == "1":
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} You choose P2P. You can be a host or a client only in your network'")
        P2P().P2P_manager()
    elif choice == "2":
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} You choose public host.")
    else: 
        print(f"{Fore.RED}[X] Invalid choice{Style.RESET_ALL}")
    


    try:
        send_thread.join()
        receive_thread.join()
    except KeyboardInterrupt:
        print(f"{Fore.RED}[X] Forced closure program.{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()