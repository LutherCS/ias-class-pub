#!/usr/bin/env python3
"""Socket Server"""

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4600


def main():
    """Main Server loop"""
    # Create TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    # Bind to a port
    server_socket.bind((HOST, PORT))
    # Start listening for incoming connection
    server_socket.listen()
    print(f"Listening for incoming connections on {HOST}:{PORT}")
    # Accept a connection
    conn, client = server_socket.accept()
    print(f"New client: {client[0]}:{client[1]}")

    while True:
        # Read 4KB from the socket
        msg_in = conn.recv(4096).decode("utf-8")
        print(f"Received {msg_in}")
        if len(msg_in) < 1:
            conn.close()
            break
        msg_out = msg_in[::-1]
        conn.send(msg_out.encode())
    print("Done")


if __name__ == "__main__":
    main()
