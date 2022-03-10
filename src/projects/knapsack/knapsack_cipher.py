#!/usr/bin/env python3
"""
Merkle-Hellman Knapsack cipher implementation

@authors: 
@version: 2022.3
"""

import math
import pathlib
import random

BLOCK_SIZE = 64



def generate_sik(size: int = BLOCK_SIZE) -> tuple[int, ...]:
    """
    Generate a superincreasing knapsack of the specified size

    :param size: block size
    :return: a superincreasing knapsack as a tuple
    """
    # TODO: Implement this function
    ...


def calculate_n(sik: tuple) -> int:
    """
    Calculate N value

    N is the smallest number greater than the sum of values in the knapsack

    :param sik: a superincreasing knapsack
    :return: n
    """
    # TODO: Implement this function
    ...


def calculate_m(n: int) -> int:
    """
    Calculate M value

    M is the largest number in the range [1, N) that is co-prime of N
    :param n: N value
    """
    # TODO: Implement this function
    ...


def calculate_inverse(sik: tuple[int, ...], n: int = None, m: int = None) -> int:
    """
    Calculate inverse modulo

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: inverse modulo i so that m*i = 1 mod n
    """
    # TODO: Implement this function
    ...


def generate_gk(sik: tuple[int, ...], n: int = None, m: int = None) -> tuple[int, ...]:
    """
    Generate a general knapsack from the provided superincreasing knapsack

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: the general knapsack
    """
    # TODO: Implement this function
    ...


def encrypt(
    plaintext: str, gk: tuple[int, ...], block_size: int = BLOCK_SIZE
) -> list[int]:
    """
    Encrypt a message

    :param plaintext: text to encrypt
    :param gk: general knapsack
    :param block_size: size of the encryption block
    :return: encrypted text
    """
    # TODO: Implement this function
    ...


def decrypt(
    ciphertext: list[int],
    sik: tuple[int, ...],
    n: int = None,
    m: int = None,
    block_size: int = BLOCK_SIZE,
) -> str:
    """
    Decrypt a single block
    
    :param ciphertext: text to decrypt
    :param sik: superincreasing knapsack
    :param n: N value
    :param m: M value
    :param block_size: block size
    :return: decrypted string
    """
    # TODO: Implement this function
    ...


def main():
    """
    Main function
    Use your own values to check that functions work as expected
    You still need to rely on tests for proper verification
    """
    print("Hellman-Merkle example")


if __name__ == "__main__":
    main()
