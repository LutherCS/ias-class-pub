#!/usr/bin/python3
"""
Merkle-Hellman Knapsack cipher implementation

@authors:
@version: 2025.3
"""

LARGE_N = 100


def generate_sik(size: int) -> tuple[int, ...]:
    """
    Generate a superincreasing knapsack of the specified size
    Assuming 1-based indexing, i-th item in this knapsack is chosen uniformly from the following range:
    [pow(2, i-1) * pow(2, LARGE_N) + 1, pow(2, i-1)*pow(2, LARGE_N)]

    :param size: size (in bits) of the knapsack
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


def calculate_inverse(sik: tuple[int, ...], n: int = 0, m: int = 0) -> int:
    """
    Calculate inverse modulo

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: inverse modulo i so that m*i = 1 mod n
    """
    # TODO: Implement this function
    ...


def generate_gk(sik: tuple[int, ...], n: int = 0, m: int = 0) -> tuple[int, ...]:
    """
    Generate a general knapsack from the provided superincreasing knapsack

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: the general knapsack
    """
    # TODO: Implement this function
    ...


def encrypt(plaintext: str, gk: tuple[int, ...]) -> int:
    """
    Encrypt a message

    :param plaintext: text to encrypt
    :param gk: general knapsack
    :return: encrypted text
    :raise: ValueError if the message is longer than the knapsack
    """
    # TODO: Implement this function
    ...


def decrypt(ciphertext: int, sik: tuple[int, ...], n: int = 0, m: int = 0) -> str:
    """
    Decrypt a single block

    :param ciphertext: text to decrypt
    :param sik: superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: decrypted string
    """
    # TODO: Implement this function
    ...


def main():
    """
    Main function
    Use your own values to check that functions work as expected
    """


if __name__ == "__main__":
    main()
