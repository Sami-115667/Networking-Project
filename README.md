# Networking-Project
This project is a client-server application for group chats and file transfers. The server handles multiple clients, while the client uses a Tkinter GUI for easy interaction. It enables users to send messages and files efficiently, utilizing Python's socket programming and threading for stable communication.


# Group Chat and File Transfer Application

This project is a client-server application for group chats and file transfers. The server handles multiple clients, while the client uses a Tkinter GUI for easy interaction. It enables users to send messages and files efficiently, utilizing Python's socket programming and threading for stable communication.

## Features

- **Concurrent Client Connections**: Multiple clients can connect to the server simultaneously.
- **Message Broadcasting**: Clients can send messages to the server, which are broadcast to all connected clients.
- **File Transfer**: Clients can send files to the server, which are saved in a specified directory.
- **User Interface**: A simple Tkinter GUI for the client to enter server details, username, choice of action, and input for messages or file paths.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Setup and Usage

### Server

1. Run the server script:
    ```bash
    python -u server.py
    ```

2. Enter the dedicated port number when prompted.

### Client

1. Run the client script:
    ```bash
    python -u client.py
    ```

2. In the GUI, enter the server IP, port, and your username.

3. Enter 'm' to send a message or 'f' to send a file.

4. For messages, type your message and click 'Send'.

5. For files, enter the file path (e.g., `F:\Python\Python\Networking Lab\gui`) and click 'Send'.

## File Storage

Files sent from clients are stored in the directory: `F:\Python\Python\Networking Lab\Networking Project`.

## Example

1. Start the server:
    ```bash
    python server.py
    ```

2. Start the client:
    ```bash
    python client.py
    ```

3. Connect the client to the server using the GUI.

4. Send messages or files through the client GUI.

## License

This project is licensed under the MIT License.
