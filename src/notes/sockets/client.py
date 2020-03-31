#!/usr/bin/env python3
"""Socket Client"""

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4600


def main():
    """Main Client loop"""
    # Create TCP socket
    client_socket = socket(AF_INET, SOCK_STREAM)
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    while True:
        msg_out = input("Enter message: ")
        print(f"You entered {msg_out}")
        if msg_out == "BYE":
            client_socket.close()
            break
        client_socket.send(msg_out.encode())
        msg_in = client_socket.recv(4096).decode("utf-8")
        print(f"Server says: {msg_in}")
    print("Done")


if __name__ == "__main__":
    main()
