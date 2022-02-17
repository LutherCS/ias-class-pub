#!/usr/bin/env python3
"""
Double transposition cipher implementation

@authors: Roman Yasinovskyy
@version: 2022.2
"""

from typing import Any


def encrypt(plaintext: str, row_key: tuple[int], col_key: tuple[int]) -> str:
    """Encrypt plaintext using double transposition cipher

    Process: the `plaintext` is converted into a matrix with `len(row_key)` rows
            and `len(col_key)` columns. Then the rows are reshuffled using the
            following algorithm:
            - if `row_key` is (2, 0, 1), the 3rd row in
            the plaintext matrix becomes first, the 1st - second, and the 2nd
            becomes last in the intermediary matrix `shuffled_rows`.
            - if `col_key` is (1, 0, 2), the 2nd column in `shuffled_rows` becomes
            the first, the 1st - second, and the 3rd stays in place in the resulting
            matrix `shuffled_columns`.
            The values in the resulting matrix are joined together in the string,
            row-by-row, column-by-column.
    :param plaintext: plaintext
    :param row_key: row permutation key
    :param col_key: column permutation key
    :return: ciphertext
    """
    # TODO: Implement this function
    ...


def decrypt(ciphertext: str, row_key: tuple[int], col_key: tuple[int]) -> str:
    """Decrypt ciphertext using double transposition cipher

    Process: the `ciphertext` is converted into a matrix with `len(row_key)` rows
        and `len(col_key)` columns. Then the rows are reshuffled using the
        following algorithm:
        - if `row_key` is (2, 0, 1), the 1st row in
        the ciphertext matrix becomes third, the 2nd - first, and the 3rd
        becomes second in the intermediary matrix `unshuffled_rows`.
        - if `col_key` is (1, 0, 2), the 1st column in `shuffled_rows` becomes
        the second, the 2nd - first, and the 3rd stays in place in the resulting
        matrix `unshuffled_columns`.
        The values in the resulting matrix are joined together in the string,
        row-by-row, column-by-column.
    :param ciphertext: ciphertext
    :param row_key: row permutation key
    :param col_key: column permutation key
    :return: plaintext
    """
    # TODO: Implement this function
    ...


def analyze(ciphertext: str) -> set[str]:
    """Analyze ciphertext generated using double transposition cipher

    Since the permutation keys are unknown, try them all! For example,
            "Hello World!" (12 characters) can be encrypted using matrices
            1x12 (but it's time-consuming), 2x6, 3x4, 4x3, 6x2, and
            12x1 (equally time-consuming). Each of those matrices can have
            multiple (n!) permutations of rows and columns, so manually scanning
            them can be inefficient.

    Try the following heuristics:
    - all words of a candidate phrase must be in the dictionary
    - punctuation (.,:;!?) should be ignored when comparing to the dictionary words
    - comparison should be case-insensitive

    :param ciphertext: encrypted text to analyze
    :return: set of plaintext candidate(s)
    """
    # NOTE: Recommended to implement
    ...


def main():
    """Main function"""
    print("\nANALYSIS\n")
    print(analyze(" taw.natt adakc"))


if __name__ == "__main__":
    main()
