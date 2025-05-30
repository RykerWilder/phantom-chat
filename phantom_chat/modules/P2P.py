
class P2P:
    # IP ADDRESS
    default_ip = "192.168.1.38"
    ip_address = input(f"Insert the IP address (default: {default_ip}): ") or default_ip

    while True:
        choiceP2P = input("Choose the mod: Host [1] or Client [2]: ")
        if choiceP2P in ["1", "2"]:
            break
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")

    # START CONNECTION
    if choiceP2P == "1":
        client, public_partner = create_host(ip_address, PORT, public_key)
    else:
        client, public_partner = create_connection(ip_address, PORT, public_key)

    print(f"{Fore.GREEN}Connection established! Digit {Fore.YELLOW}\"/exit\"{Style.RESET_ALL}{Fore.GREEN} to exit.{Style.RESET_ALL}")

    # SENDING AND RECEIVING
    send_thread = threading.Thread(target=sending_messages, args=(client, public_partner))
    receive_thread = threading.Thread(target=receiving_messages, args=(client, private_key))

    send_thread.daemon = True
    receive_thread.daemon = True

    send_thread.start()
    receive_thread.start()