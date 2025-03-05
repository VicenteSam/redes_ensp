import socket
import threading

clients = {}

def client_list():
    print("Current clients:")
    for username, (ip, port) in clients.items():
        print(f"{username} ({ip}:{port})")

def handle_client(client_socket, client_address):
    try:
        username = client_socket.recv(1024).decode()
        clients[username] = client_address
        print(f"New connection: {username} - {client_address[0]}:{client_address[1]}")
        client_list()

        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message.startswith("/list"):
                client_socket.send(str(clients).encode())
            elif message.startswith("/msg"):
                _, recipient, content = message.split(' ', 2)
                if recipient in clients:
                    recipient_ip, recipient_port = clients[recipient]
                    try:
                        recipient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        recipient_socket.connect((recipient_ip, recipient_port))
                        recipient_socket.send(f"{username}: {content}".encode())
                        recipient_socket.close()
                    except Exception as e:
                        print(f"Error sending message to {recipient}: {e}")
                else:
                    client_socket.send(f"User {recipient} not found.".encode())
            else:
                for user, (ip, port) in clients.items():
                    if user != username:
                        try:
                            user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            user_socket.connect((ip, port))
                            user_socket.send(f"{username}: {message}".encode())
                            user_socket.close()
                        except Exception as e:
                            print(f"Error broadcasting message to {user}: {e}")

    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        if username in clients:
            del clients[username]
            print(f"{username} disconnected.")
            client_list()
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12000))
    server.listen(5)
    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == '__main__':
    start_server()
    
