#!/usr/bin/env python3
# encoding: UTF-8
"""A5/1 cipher"""


def populate_registers(init_keyword: str) -> tuple:
    """Populate registers

    init_keyword -- inital secret word that will be used to populate registers X, Y, and Z
    
    return registers X, Y, Z as a tuple
    """
    raise NotImplementedError


def majority(x8_bit: str, y10_bit: str, z10_bit: str) -> str:
    """Return the majority bit
    
    x8_bit -- 9th bit from the X register
    y10_bit -- 11th bit from the Y register
    z10_bit -- 11th bit from the Z register

    return the value of the majority bit
    """
    raise NotImplementedError


def step_x(register: str) -> str:
    """Stepping register X
    
    register -- X register
    
    return new value of the X register
    """
    raise NotImplementedError


def step_y(register: str) -> str:
    """Stepping register Y
    
    register -- Y register
    
    return new value of the Y register
    """
    raise NotImplementedError


def step_z(register: str) -> str:
    """Stepping register Z
    
    register -- Z register
    
    return new value of the Z register
    """
    raise NotImplementedError


def generate_bit(x: str, y: str, z: str) -> int:
    """Generate a keystream bit
    
    x -- X register
    y -- Y register
    z -- Z register

    return a single keystrema bit
    """
    raise NotImplementedError


def generate_keystream(plaintext: str, x: str, y: str, z: str) -> str:
    """Generate stream of bits to match length of plaintext
    
    plaintext -- plaintext to be encrypted
    x -- X register
    y -- Y register
    z -- Z register

    return keystream
    """
    raise NotImplementedError


def encrypt(plaintext: str, keystream: str) -> str:
    """Encrypt plaintext using A5/1
    
    plaintext -- plaintext to be encrypted
    keystream -- keystream

    return ciphertext
    """
    raise NotImplementedError


def encrypt_file(filename: str, secret: str) -> None:
    """Encrypt a file
    
    filename -- filename to be encrypted
    secret -- secret to initialize registers

    return write the result to filename.secret
    """
    raise NotImplementedError


def main():
    """Main function"""
    pass


if __name__ == "__main__":
    main()
