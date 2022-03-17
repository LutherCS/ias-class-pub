#!/usr/bin/env python3
"""
Merkle-Hellman Knapsack cipher testing

@authors: Roman Yasinovskyy
@version: 2022.3
"""

import importlib
import pathlib
import sys
from typing import Generator

# from hashlib import sha256

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.knapsack import knapsack_cipher as knapsack


DATA_DIR = pathlib.Path("data/projects/knapsack/")
TIME_LIMIT = 2


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


def test_generate_sik_default():
    """Testing generate_sik function with default block size"""
    sik = knapsack.generate_sik()
    for idx, item in enumerate(sik):
        assert item > sum(sik[:idx])


@pytest.mark.parametrize("block_size", [8, 32, 64, 128])
def test_generate_sik(block_size):
    """Testing generate_sik function with the specified block size"""
    sik = knapsack.generate_sik(block_size)
    assert len(sik) == block_size
    for idx, item in enumerate(sik):
        assert item > sum(sik[:idx])


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "sik, n",
    get_cases("test_case_basic", "sik", "default_n"),
)
def test_calculate_n(sik, n):
    """Testing calculate_n function"""
    assert knapsack.calculate_n(sik) == n


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "n, m",
    get_cases("test_case_basic", "default_n", "default_m"),
)
def test_calculate_m(n, m):
    """Testing calculate_m function"""
    assert knapsack.calculate_m(n) == m


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "sik, i",
    get_cases("test_case_basic", "sik", "default_i"),
)
def test_calculate_inverse_default(sik, i):
    """Testing calculate_inverse function with default m and n"""
    assert knapsack.calculate_inverse(sik) == i


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "sik, n, m, i",
    get_cases("test_case_basic", "sik", "n", "m", "i"),
)
def test_calculate_inverse(sik, n, m, i):
    """Testing calculate_inverse function with the specified n and m"""
    assert knapsack.calculate_inverse(sik, n, m) == i


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "sik, genk",
    get_cases("test_case_basic", "sik", "default_genk"),
)
def test_generate_gk_default(sik, genk):
    """Testing generate_gk function with default parameters"""
    assert knapsack.generate_gk(sik) == tuple(genk)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "sik, n, m, genk",
    get_cases("test_case_basic", "sik", "n", "m", "genk"),
)
def test_generate_gk(sik, n, m, genk):
    """Testing generate_gk function"""
    assert knapsack.generate_gk(sik, n, m) == tuple(genk)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, genk, ciphertext",
    get_cases("test_case_basic", "plaintext", "genk", "ciphertext"),
)
def test_encrypt(plaintext, genk, ciphertext):
    """Testing encrypt function"""
    assert knapsack.encrypt(plaintext, genk) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "ciphertext, sik, n, m, plaintext",
    get_cases("test_case_basic", "ciphertext", "sik", "n", "m", "plaintext"),
)
def test_decrypt(ciphertext, sik, n, m, plaintext):
    """Testing decrypt function"""
    assert knapsack.decrypt(ciphertext, sik, n, m) == plaintext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, genk, ciphertext, block_size",
    get_cases("test_case_word", "plaintext", "genk", "ciphertext", "block_size"),
)
def test_encrypt_word(plaintext, genk, ciphertext, block_size):
    """Testing complex case of encryption"""
    assert knapsack.encrypt(plaintext, genk, block_size) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "ciphertext, sik, n, m, plaintext",
    get_cases("test_case_word", "ciphertext", "sik", "n", "m", "plaintext"),
)
def test_decrypt_word(ciphertext, sik, n, m, plaintext):
    """Testing complex case of decryption"""
    assert knapsack.decrypt(ciphertext, sik, n, m) == plaintext


if __name__ == "__main__":
    pytest.main(["-v", __file__])
