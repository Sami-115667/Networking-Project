import socket
import os
import tkinter as tk
from tkinter import ttk

class Client:
    def __init__(self, root):
        self.root = root
        self.server_ip = None
        self.server_port = None
        self.username = None
        self.choice = None
        self.socket = None
        self.create_ui()

    def create_ui(self):
        ip_label = ttk.Label(self.root, text="Server IP:")
        ip_label.grid(row=0, column=0, padx=5, pady=5)
        self.ip_entry = ttk.Entry(self.root)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        port_label = ttk.Label(self.root, text="Server Port:")
        port_label.grid(row=1, column=0, padx=5, pady=5)
        self.port_entry = ttk.Entry(self.root)
        self.port_entry.grid(row=1, column=1, padx=5, pady=5)

        username_label = ttk.Label(self.root, text="Username:")
        username_label.grid(row=2, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(row=2, column=1, padx=5, pady=5)

        connect_button = ttk.Button(self.root, text="Connect", command=self.connect_to_server)
        connect_button.grid(row=3, columnspan=2, padx=5, pady=5)

        ttk.Separator(self.root, orient=tk.HORIZONTAL).grid(row=4, columnspan=2, sticky="ew", pady=5)

        choice_label = ttk.Label(self.root, text="Choice (m for message, f for file):")
        choice_label.grid(row=5, column=0, padx=5, pady=5)
        self.choice_entry = ttk.Entry(self.root)
        self.choice_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Separator(self.root, orient=tk.HORIZONTAL).grid(row=6, columnspan=2, sticky="ew", pady=5)

        self.message_entry = ttk.Entry(self.root)
        self.message_entry.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.file_path_entry = ttk.Entry(self.root)
        self.file_path_entry.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        send_button = ttk.Button(self.root, text="Send", command=self.send_data)
        send_button.grid(row=9, columnspan=2, padx=5, pady=5)

    def connect_to_server(self):
        self.server_ip = self.ip_entry.get()
        self.server_port = int(self.port_entry.get())
        self.username = self.username_entry.get()

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_ip, self.server_port))
            print("Connected to the server.")
            self.socket.sendall(self.username.encode('utf-8'))  # Send username to server
        except ConnectionRefusedError:
            print("Connection to the server failed. Make sure the server is running.")
        except Exception as e:
            print("Error:", e)

    def send_data(self):
        choice = self.choice_entry.get()

        try:
            if choice == "m" or choice == "f":
                self.socket.sendall(choice.encode('utf-8'))  # Encode the choice before sending
                if choice == "m":
                    message = self.message_entry.get()
                    if message:
                        full_message = message
                        self.socket.sendall(full_message.encode('utf-8'))
                        print("Message sent successfully.")
                    else:
                        print("Error: Message cannot be empty.")
                elif choice == "f":
                    file_path = self.file_path_entry.get()
                    if os.path.isfile(file_path):
                        filename = os.path.basename(file_path)
                        self.socket.sendall(f"file:{filename}".encode('utf-8'))
                        with open(file_path, "rb") as f:
                            while True:
                                data = f.read(1024)
                                if not data:
                                    break
                                self.socket.sendall(data)
                            self.socket.send(b"FILE_TRANSMISSION_COMPLETE")
                        print("File sent successfully.")
                    else:
                        print("Error: File does not exist.")
            else:
                print("Error: Invalid choice.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Client")
    client = Client(root)
    root.mainloop()
