#!/usr/bin/env python3
# encoding: UTF-8
"""
Simple TCP socket server demo

@author: Roman Yasinovskyy
@version: 2025.4
@see: https://docs.python.org/3/library/socket.html
"""

from socket import socket, gethostname
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

HOST = gethostname()
PORT = 4600


def main():
    """Main loop"""
    # Create a TCP socket
    with socket(AF_INET, SOCK_STREAM) as server_sckt:
        # Prevent OSError: [Errno 98] Address already in use
        server_sckt.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # Bind the program to a port
        server_sckt.bind((HOST, PORT))
        # Become a server socket
        server_sckt.listen()
        print(f"Listening on {HOST}:{PORT}")
        # Accept a connection
        conn, client = server_sckt.accept()
        # Receive and respond
        with conn:
            print(f"New client: {client[0]}:{client[1]}")
            while True:
                # Read 4 KB of data
                msg_in = conn.recv(4096).decode("utf-8")
                # Close the connection if the client closed it
                if len(msg_in) < 1:
                    break
                print(f"Received: {msg_in}")
                msg_out = msg_in[::-1]
                # Send a response
                conn.sendall(msg_out.encode())
    print("Done")


if __name__ == "__main__":
    main()
