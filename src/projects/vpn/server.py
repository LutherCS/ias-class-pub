#!/usr/bin/env python3
"""
VPN Sever

@author: Roman Yasinovskyy
@version: 2025.4
"""

import re
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, gethostname, socket
from types import ModuleType

import tomllib
from Crypto.Cipher import AES, DES3, Blowfish
from Crypto.Hash import HMAC, SHA256
from diffiehellman.diffiehellman import DiffieHellman

HOST = gethostname()
PORT = 4600
TEXT_TO_OBJ = {"AES": AES, "Blowfish": Blowfish, "DES3": DES3}
IV_LEN = {"AES": 16, "Blowfish": 8, "DES3": 8}


def parse_proposal(msg: str) -> dict[str, list[int]]:
    """Parse client's proposal

    :param msg: message from the client with a proposal (ciphers and key sizes)
    :return: the ciphers and keys as a dictionary
    """
    # TODO: Implement this function
    ...


def select_cipher(supported: dict, proposed: dict) -> tuple[str, int]:
    """Select a cipher to use

    :param supported: dictionary of ciphers supported by the server
    :param proposed: dictionary of ciphers proposed by the client
    :return: tuple (cipher, key_size) of the common cipher where key_size is the longest supported by both
    :raise: ValueError if there is no (cipher, key_size) combination that both client and server support
    """
    # TODO: Implement this function
    ...


def generate_cipher_response(cipher: str, key_size: int) -> str:
    """Generate a response message

    :param cipher: chosen cipher
    :param key_size: chosen key size
    :return: (cipher, key_size) selection as a string
    """
    # TODO: Implement this function
    ...


def parse_dhm_request(msg: str) -> int:
    """Parse client's DHM key exchange request

    :param msg: client's DHMKE initial message
    :return: number in the client's message
    """
    # TODO: Implement this function
    ...


def get_key_and_iv(
    shared_key: str, cipher_name: str, key_size: int
) -> tuple[ModuleType | None, bytes, bytes]:
    """Get key and IV from the generated shared secret key

    :param shared_key: shared key as computed by `diffiehellman`
    :param cipher_name: negotiated cipher's name
    :param key_size: negotiated key size
    :return: (cipher, key, IV) tuple
    cipher_name must be mapped to a Crypto.Cipher object
    `key` is the *first* `key_size` bytes of the `shared_key`
    DES3 key must be padded to 64 bits with 0
    Length `ivlen` of IV depends on a cipher
    `iv` is the *last* `ivlen` bytes of the shared key
    Both key and IV must be returned as bytes
    """
    # TODO: Implement this function
    ...


def generate_dhm_response(public_key: int) -> str:
    """Generate DHM key exchange response

    :param public_key: public portion of the DHMKE
    :return: string according to the specification
    """
    # TODO: Implement this function
    ...


def read_message(msg_cipher: bytes, crypto: ModuleType) -> tuple[str, str]:
    """Read the incoming encrypted message

    :param msg_cipher: encrypted message from the socket
    :crypto: chosen cipher, must be initialized in the `main`
    :return: (plaintext, hmac) tuple
    """
    # TODO: Implement this function
    ...


def validate_hmac(msg_cipher: bytes, hmac_in: str, hashing: ModuleType) -> bool:
    """Validate HMAC

    :param msg_cipher: encrypted message from the socket
    :param hmac_in: HMAC received from the client
    :param hashing: hashing object, must be initialized in the `main`
    :raise: ValueError is HMAC is invalid
    """
    # TODO: Implement this function
    ...


def main():
    """Main event loop

    See project description for details
    """
    with socket(AF_INET, SOCK_STREAM) as server_sckt:
        server_sckt.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_sckt.bind((HOST, PORT))
        server_sckt.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, client = server_sckt.accept()
        print(f"New client: {client[0]}:{client[1]}")
        print("Negotiating the cipher")
        print("Negotiating the key")
        print("The key has been established")
        while True:
            cipher_in = conn.recv(1024)
            if len(cipher_in) < 1:
                break
            msg_in = cipher_in.decode("utf-8")
            print(f"Received: {msg_in}")
            msg_out = f"Server says: {msg_in[::-1]}"
            conn.sendall(msg_out.encode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")
