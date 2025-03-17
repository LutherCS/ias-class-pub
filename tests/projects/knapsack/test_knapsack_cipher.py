#!/usr/bin/env python3
"""
Merkle-Hellman Knapsack cipher testing

@authors: Roman Yasinovskyy
@version: 2025.3
"""

import importlib
import pathlib
import sys
import tomllib
from typing import Generator

import pytest

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
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.parametrize("size", [8, 32, 64, 128])
def test_generate_sik(size):
    """Testing generate_sik function with the specified size"""
    sik = knapsack.generate_sik(size=size)
    assert len(sik) == size
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
    "plaintext, public_file, ciphertext",
    get_cases("test_case_word", "plaintext", "public_file", "ciphertext"),
)
def test_encrypt_word(plaintext, public_file, ciphertext):
    """Testing complex case of encryption"""
    with open(pathlib.Path("data", "projects", "knapsack", public_file), "r") as f:
        gk = list(map(int, f.readline().strip().split(", ")))
    assert knapsack.encrypt(plaintext, gk) == ciphertext, knapsack.encrypt(plaintext, gk)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "ciphertext, private_file, plaintext",
    get_cases("test_case_word", "ciphertext", "private_file", "plaintext"),
)
def test_decrypt_word(ciphertext, private_file, plaintext):
    """Testing complex case of decryption"""
    with open(pathlib.Path("data", "projects", "knapsack", private_file), "r") as f:
        private_file = list(map(int, f.readline().strip().split(", ")))
        n = int(f.readline().strip())
        m = int(f.readline().strip())
    assert knapsack.decrypt(ciphertext, private_file, n, m) == plaintext


if __name__ == "__main__":
    pytest.main(["-v", __file__])
