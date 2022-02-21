#!/usr/bin/env python3
"""
A5/1 cipher implementation

@authors: Roman Yasinovskyy
@version: 2022.2
"""

from hashlib import sha256
from pathlib import Path


def populate_registers(init_keyword: str) -> tuple[str, str, str]:
    """Populate registers

    Important: if the keyword is shorted than 8 characters (64 bits),
    pad the resulting short bit string with zeros (0) up to the required 64 bits

    :param init_keyword: initial secret word that will be used to populate registers X, Y, and Z
    :return: registers X, Y, Z as a tuple
    """
    # TODO: Implement this function
    ...


def majority(x8_bit: str, y10_bit: str, z10_bit: str) -> str:
    """Return the majority bit

    :param x8_bit: 9th bit from the X register
    :param y10_bit: 11th bit from the Y register
    :param z10_bit: 11th bit from the Z register
    :return: the value of the majority bit
    """
    # TODO: Implement this function
    ...


def step_x(register: str) -> str:
    """Stepping register X

    :param register: X register
    :return: new value of the X register
    """
    # TODO: Implement this function
    ...


def step_y(register: str) -> str:
    """Stepping register Y

    :param register: Y register
    :return: new value of the Y register
    """
    # TODO: Implement this function
    ...


def step_z(register: str) -> str:
    """Stepping register Z

    :param register: Z register
    :return: new value of the Z register
    """
    # TODO: Implement this function
    ...


def generate_bit(x: str, y: str, z: str) -> int:
    """Generate a keystream bit

    :param x: X register
    :param y: Y register
    :param z: Z register
    :return: a single keystream bit
    """
    # TODO: Implement this function
    ...


def generate_keystream(plaintext: str, x: str, y: str, z: str) -> str:
    """Generate stream of bits to match length of plaintext

    :param plaintext: plaintext to be encrypted
    :param x: X register
    :param y: Y register
    :param z: Z register
    :return: keystream of the same length as the plaintext
    """
    # TODO: Implement this function
    ...


def encrypt(plaintext: str, keystream: str) -> str:
    """Encrypt plaintext using A5/1

    :param plaintext: plaintext to be encrypted
    :param keystream: keystream
    :return: ciphertext
    """
    # TODO: Implement this function
    ...


def encrypt_file(filename: str, secret: str) -> None:
    """Encrypt a file

    For the sake of output comparison you should preserve end-of-line (\n) symbols
    in the output file.

    :param filename: filename to be encrypted
    :param secret: secret to initialize registers
    :return: write the result to filename.secret
    """
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    # NOTE: Use this space as you see fit
    ...


if __name__ == "__main__":
    main()
