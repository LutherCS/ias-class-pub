#!/usr/bin/env python3
"""
Testing the Caesar cipher

@authors: Roman Yasinovskyy
@version: 2025.2
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
    from src.projects.caesar import caesar_cipher as cc


DATA_DIR = pathlib.Path("data/projects/caesar/")
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, shifted",
    get_cases("test_case", "plaintext", "shift", "shifted"),
)
def test_shift_by_n(plaintext, shift, shifted):
    """Testing shift_by_n() method"""
    assert cc.shift_by_n(plaintext, shift) == shifted


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, ciphertext",
    get_cases("test_case", "plaintext", "shift", "ciphertext"),
)
def test_shift_by_negative_n(plaintext, shift, ciphertext):
    """Testing shift_by_n() method"""
    assert cc.shift_by_n(ciphertext, -shift) == plaintext.upper()


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, ciphertext",
    get_cases("test_case", "plaintext", "shift", "ciphertext"),
)
def test_encrypt(plaintext, shift, ciphertext):
    """Testing encrypt() method"""
    assert cc.encrypt(plaintext, shift) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, obfuscated",
    get_cases("test_case", "plaintext", "shift", "obfuscated"),
)
def test_encrypt_and_obfuscate(plaintext, shift, obfuscated):
    """Testing encrypt() method with obfuscation"""
    assert cc.encrypt(plaintext, shift, True) == obfuscated


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, shift, ciphertext",
    get_cases("test_case", "plaintext", "shift", "ciphertext"),
)
def test_decrypt(plaintext, shift, ciphertext):
    """Testing decrypt() method"""
    assert cc.decrypt(ciphertext, shift) == plaintext


if __name__ == "__main__":
    pytest.main(["-v", __file__])
