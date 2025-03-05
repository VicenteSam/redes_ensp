import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12000))

    username = input("Enter your username: ")
    client_socket.send(username.encode())

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input()
        if message == "/exit":
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == '__main__':
    start_client()
