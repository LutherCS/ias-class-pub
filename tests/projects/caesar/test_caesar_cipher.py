#!/usr/bin/env python3
# encoding: UTF-8
"""
Testing the Caesar cipher

@authors: Roman Yasinovskyy
@version: 2022.02
"""


import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.caesar import caesar_cipher as cc


TIME_LIMIT = 1
import pytest

cases = [
    ("hello", 3, 1, "khoor", "KHOOR", "KHOOR"),
    ("world", 3, 1, "zruog", "ZRUOG", "ZRUOG"),
    ("zruog", -3, 1, "world", "WORLD", "WORLD"),
    ("hello world!", 3, 1, "khoor zruog!", "KHOOR ZRUOG!", "KHOORZRUOG"),
    ("hello world!", 3, 1, "khoor zruog!", "KHOOR ZRUOG!", "KHOORZRUOG"),
]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, direction, shifted, ciphertext, obfuscated", cases
)
def test_shift_by_n(plaintext, shift, direction, shifted, ciphertext, obfuscated):
    """Testing shift_by_n() method"""
    assert cc.shift_by_n(plaintext, shift, direction) == shifted


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, direction, shifted, ciphertext, obfuscated", cases
)
def test_encrypt(plaintext, shift, direction, shifted, ciphertext, obfuscated):
    """Testing encrypt() method"""
    assert cc.encrypt(plaintext, shift) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, direction, shifted, ciphertext, obfuscated", cases
)
def test_encrypt_and_obfuscate(
    plaintext, shift, direction, shifted, ciphertext, obfuscated
):
    """Testing encrypt() method with obfuscation"""
    assert cc.encrypt(plaintext, shift, True) == obfuscated


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, direction, shifted, ciphertext, obfuscated", cases
)
def test_decrypt(plaintext, shift, direction, shifted, ciphertext, obfuscated):
    """Testing decrypt() method"""
    assert cc.decrypt(ciphertext, shift) == plaintext


if __name__ == "__main__":
    pytest.main(["-v", __file__])
