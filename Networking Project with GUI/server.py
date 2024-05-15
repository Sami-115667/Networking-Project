import socket
import threading
import sys
import os

class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.username = None  # Initialize username to None

    def run(self):
        try:
            self.username = self.client_socket.recv(1024).decode('utf-8')  # Receive username from client
            print(f"Welcome {self.username} to the group chat!")  # Welcome the user
            while True:
                choice = self.client_socket.recv(1024).decode('utf-8')
                if not choice:
                    break
                if choice == "m":
                    self.receive_message()
                elif choice == "f":
                    self.receive_file()
                else:
                    print(f"Invalid choice received from {self.username}")
        except Exception as e:
            print(f"Error in client handler for {self.username}: {e}")
        finally:
            self.client_socket.close()

    def receive_message(self):
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                else:
                    message = data.decode('utf-8')
                    print(f"Received message from  {self.username}: {message}")  # Display message with username
                    break
        except Exception as e:
            print(f"Error receiving message from {self.username}: {e}")

    def receive_file(self):
        try:
            ending_string = 'FILE_TRANSMISSION_COMPLETE'.encode()
            data = self.client_socket.recv(1024)
            if data.startswith(b"file:"):
                filename = data.decode('utf-8')[5:].strip()
                file_path = os.path.join("F:\\Python\\Python\\Networking Lab\\gui", filename)
                with open(file_path, "wb") as f:
                    while True:
                        data = self.client_socket.recv(1024)
                        if data.endswith(ending_string):
                            data = data[:-len(ending_string)]
                            break
                        f.write(data)
                    f.write(data) 
                print(f"Received file '{filename}' from {self.username}")
            else:
                print(f"Invalid file request received from {self.username}")
        except Exception as e:
            print(f"Error receiving file from {self.username}: {e}")


class Server:
    def __init__(self, server_socket):
        self.server_socket = server_socket

    def start_server(self):
        try:
            print("Group Chat is started....")
            while True:
                client_socket, address = self.server_socket.accept()
                client_handler = ClientHandler(client_socket, address)
                client_handler.start()
        except Exception as e:
            print("Error in server:", e)
        finally:
            self.close_server_socket()

    def close_server_socket(self):
        try:
            if self.server_socket:
                self.server_socket.close()
                print("Server socket closed.")
        except Exception as e:
            print("Error while closing server socket:", e)


def get_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        return ip
    except Exception as e:
        print("Error while getting IP:", e)
        return None


if __name__ == "__main__":
    try:
        ip = get_ip()
        if ip:
            print("Enter the dedicated port number for the group chat:")
            port = int(input())
            print("To join the group chat, give server IP:", ip, "Server port:", port)
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((ip, port))
            server_socket.listen(5)
            server = Server(server_socket)
            server.start_server()
    except KeyboardInterrupt:
        print("Server stopped.")
        sys.exit(0)
    except Exception as e:
        print("Error:", e)
