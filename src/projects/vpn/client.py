#!/usr/bin/env python3
"""
VPN Client

@author: Roman Yasinovskyy
@version: 2025.4
"""

from socket import AF_INET, SOCK_STREAM, gethostname, socket
from types import ModuleType

import tomllib
from Crypto.Cipher import AES, DES3, Blowfish
from Crypto.Hash import HMAC, SHA256
from diffiehellman.diffiehellman import DiffieHellman

HOST = gethostname()
PORT = 4600
TEXT_TO_OBJ = {"AES": AES, "Blowfish": Blowfish, "DES3": DES3}
IV_LEN = {"AES": 16, "Blowfish": 8, "DES3": 8}


def generate_cipher_proposal(supported: dict[str, list[int]]) -> str:
    """Generate a cipher proposal message

    :param supported: cryptosystems supported by the client
    :return: proposal as a string
    """
    # TODO: Implement this function
    ...


def parse_cipher_selection(msg: str) -> tuple[str, int]:
    """Parse server's response

    :param msg: server's message with the selected cryptosystem
    :return: (cipher_name, key_size) tuple extracted from the message
    """
    # TODO: Implement this function
    ...


def generate_dhm_request(public_key: int) -> str:
    """Generate DHM key exchange request

    :param: client's DHM public key
    :return: string according to the specification
    """
    # TODO: Implement this function
    ...


def parse_dhm_response(msg: str) -> int:
    """Parse server's DHM key exchange request

    :param msg: server's DHMKE message
    :return: number in the server's message
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
    DES key must be padded to 64 bits with 0
    Length `ivlen` of IV depends on a cipher
    `iv` is the *last* `ivlen` bytes of the shared key
    Both key and IV must be returned as bytes
    """
    # TODO: Implement this function
    ...


def add_padding(message: str) -> str:
    """Add padding (0x0) to the message to make its length a multiple of 16

    :param message: message to pad
    :return: padded message
    """
    # TODO: Implement this function
    ...


def encrypt_message(message: str, crypto: ModuleType, hashing: ModuleType) -> tuple[bytes, str]:
    """
    Encrypt the message

    :param message: plaintext to encrypt
    :param crypto: chosen cipher, must be initialized in the `main`
    :param hashing: hashing object, must be initialized in the `main`
    :return: (ciphertext, hmac) tuple

    1. Pad the message, if necessary
    2. Encrypt using cipher `crypto`
    3. Compute HMAC using `hashing`
    """
    # TODO: Implement this function
    ...


def main():
    """Main event loop

    See project description for details
    """
    with socket(AF_INET, SOCK_STREAM) as client_sckt:
        client_sckt.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Pick cipher and key size
        print("Negotiating the cipher")
        print("Negotiating the key")
        print("The key has been established")

        while True:
            msg_out = input("Enter message: ")
            if msg_out == "\\quit":
                break
            cipher_out = msg_out
            client_sckt.sendall(cipher_out.encode("utf-8"))
            msg_in = client_sckt.recv(1024)
            print(msg_in.decode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")
