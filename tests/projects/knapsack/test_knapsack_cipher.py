#!/usr/bin/env python3
"""
Testing the Merkle–Hellman Knapsack cipher
@author: Roman Yasinovskyy
"""

import pathlib
import pytest
from src.projects.knapsack import knapsack_cipher as knapsack


siks = (
    (171, 196, 457, 1191, 2410),  # Merkle-Hellman paper
    (2, 3, 7, 14, 30, 57, 120, 251),  # Stamp's book
    (2, 3, 6, 13, 27, 52),  # Stamp's site
    (2, 7, 11, 21, 42, 89, 180, 354),  # Wikipedia
)
ns = (8443, 491, 105, 881)
ms = (2550, 41, 31, 588)
invs = (3950, 12, 61, 442)
gks = (
    (5457, 1663, 216, 6013, 7439),
    (82, 123, 287, 83, 248, 373, 10, 471),
    (62, 93, 81, 88, 102, 37),
    (295, 592, 301, 14, 28, 353, 120, 236),
)
plaintexts = ("\x0b", "\x96", "5", "a")
ciphertexts = ([15115], [548], [280], [1129])


def test_generate_sik_default():
    """Testing generate_sik function with default block size"""
    sik = knapsack.generate_sik()
    for i in range(len(sik)):
        assert sik[i] > sum(sik[:i])


@pytest.mark.parametrize("block_size", [4, 8, 32, 64])
def test_generate_sik(block_size):
    """Testing generate_sik function with the specified block size"""
    sik = knapsack.generate_sik(block_size)
    assert len(sik) == block_size
    for i in range(len(sik)):
        assert sik[i] > sum(sik[:i])


@pytest.mark.parametrize("sik, n", zip(siks, (4426, 485, 104, 707)))
def test_calculate_n(sik, n):
    """Testing calculate_n function"""
    assert knapsack.calculate_n(sik) == n


@pytest.mark.parametrize(
    "sik, n, m", zip(siks, (4426, 485, 104, 707), (4425, 484, 103, 706)),
)
def test_calculate_m(sik, n, m):
    """Testing calculate_m function"""
    assert knapsack.calculate_m(sik, n) == m


@pytest.mark.parametrize("sik, inverse", zip(siks, (4425, 484, 103, 706)))
def test_calculate_inverse_default(sik, inverse):
    """Testing calculate_inverse function with default m and n"""
    assert knapsack.calculate_inverse(sik) == inverse


@pytest.mark.parametrize(
    "sik, n, m, inverse", zip(siks, ns, ms, invs),
)
def test_calculate_inverse(sik, n, m, inverse):
    """Testing calculate_inverse function with the specified n and m"""
    assert knapsack.calculate_inverse(sik, n, m) == inverse


@pytest.mark.parametrize(
    "sik, gk",
    zip(
        siks,
        (
            (4255, 4230, 3969, 3235, 2016),
            (483, 482, 478, 471, 455, 428, 365, 234),
            (102, 101, 98, 91, 77, 52),
            (705, 700, 696, 686, 665, 618, 527, 353),
        ),
    ),
)
def test_generate_gk_default(sik, gk):
    """Testing generate_gk function with default parameters"""
    assert knapsack.generate_gk(sik) == gk


@pytest.mark.parametrize(
    "sik, n, m, gk", zip(siks, ns, ms, gks),
)
def test_generate_gk(sik, n, m, gk):
    """Testing generate_gk function"""
    assert knapsack.generate_gk(sik, n, m) == gk


@pytest.mark.parametrize(
    "plaintext, gk, ciphertext", zip(plaintexts, gks, ciphertexts)
)
def test_encrypt(plaintext, gk, ciphertext):
    """Testing encrypt function"""
    assert knapsack.encrypt(plaintext, gk) == ciphertext


@pytest.mark.parametrize(
    "ciphertext, sik, n, m, plaintext",
    zip(ciphertexts, siks, ns, ms, plaintexts),
)
def test_decrypt(ciphertext, sik, n, m, plaintext):
    """Testing decrypt function"""
    assert knapsack.decrypt(ciphertext, sik, n, m) == plaintext


@pytest.mark.parametrize("plaintext, ciphertext", zip(["octoduck", "infosec"], [10937952106318749431957, 9680004055205841196375]))
def test_encrypt_word(plaintext, ciphertext):
    """Testing complex case of encryption"""
    with open(pathlib.Path("data", "projects", "knapsack", "knapsack.public"), "r") as f:
        gk = list(map(int, f.readline().strip().split(", ")))
    assert knapsack.encrypt(plaintext, gk) == [ciphertext]


@pytest.mark.timeout(2)
def test_decrypt_word():
    """Testing complex case of decryption"""
    with open(pathlib.Path("data", "projects", "knapsack", "knapsack.private"), "r") as f:
        sik = list(map(int, f.readline().strip().split(", ")))
        n = int(f.readline().strip())
        m = int(f.readline().strip())
    assert knapsack.decrypt([10937952106318749431957], sik, n, m) == "octoduck"


if __name__ == "__main__":
    pytest.main(["-v", "test_knapsack_cipher.py"])
