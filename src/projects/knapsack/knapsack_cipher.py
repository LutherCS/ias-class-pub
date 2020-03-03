#!/usr/bin/env python3
"""Merkle–Hellman Knapsack cipher"""

import math
import pathlib
import random

BLOCK_SIZE = 64


def generate_sik(size: int = BLOCK_SIZE) -> tuple:
    """Generate a superincreasing knapsack of the specified size"""
    raise NotImplementedError


def calculate_n(sik: tuple) -> int:
    """Calculate N value
    N is the smallest number, greater than the sum of values in the knapsack
    """
    raise NotImplementedError


def calculate_m(sik: tuple, n: int) -> int:
    """Calculate M value
    M is the largest number in the range [1, N) that is co-prime of N
    """
    raise NotImplementedError


def calculate_inverse(sik: tuple, n: int = None, m: int = None) -> int:
    """Calculate inverse modulo"""
    raise NotImplementedError


def generate_gk(sik: tuple, n: int = None, m: int = None) -> tuple:
    """Generate a general knapsack from the provided superincreasing knapsack"""
    raise NotImplementedError


def encrypt(plaintext: str, gk: tuple, block: int = BLOCK_SIZE) -> list:
    """Encrypt a message"""
    raise NotImplementedError


def decrypt(
    ciphertext: list, sik: tuple, n: int = None, m: int = None, block: int = BLOCK_SIZE,
) -> str:
    """Decrypt a single block"""
    raise NotImplementedError


def main():
    """
    Main function
    Use your own values to check that functions work as expected
    You still need to rely on tests for proper verification
    """
    print("Hellman-Merkle example")


if __name__ == "__main__":
    main()
