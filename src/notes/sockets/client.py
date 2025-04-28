#!/usr/bin/env python3
# encoding: UTF-8
"""
Simple TCP socket client demo

@author: Roman Yasinovskyy
@version: 2025.4
@see: https://docs.python.org/3/library/socket.html
"""

from socket import socket, gethostname
from socket import AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4600


def main():
    """Main loop"""
    # Create a TCP socket
    with socket(AF_INET, SOCK_STREAM) as client_sckt:
        # Connect to the server on the same machine
        client_sckt.connect((HOST, PORT))
        # Print a status message
        print(f"Connected to {HOST}:{PORT}")

        # Listen and respond
        while True:
            # Read user input
            msg_out = input("Enter message: ")
            # Close the connection if BYE is entered
            if msg_out == "BYE":
                break
            # Send a message
            client_sckt.sendall(msg_out.encode())
            # Read a response
            msg_in = client_sckt.recv(4096).decode("utf-8")
            # Print the response
            print(f"Server says: {msg_in}")
    print("Done")


if __name__ == "__main__":
    main()
