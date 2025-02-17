#!/usr/bin/python3
"""
Double transposition cipher testing

@authors: Roman Yasinovskyy
@version: 2022.2
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import tomllib

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.doubletrans import analyze, decrypt, encrypt


DATA_DIR = pathlib.Path("data/projects/doubletrans/")
TIME_LIMIT = 5


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, key, ciphertext",
    get_cases("test_case", "plaintext", "key", "ciphertext"),
)
def test_encrypt(plaintext: str, key: tuple[tuple[int, ...], tuple[int, ...]], ciphertext: str):
    """Testing the encryption"""
    assert encrypt(plaintext, key) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, key, ciphertext",
    get_cases("test_case", "plaintext", "key", "ciphertext"),
)
def test_decrypt(plaintext: str, key: tuple[tuple[int, ...], tuple[int, ...]], ciphertext: str):
    """Testing the decryption"""
    assert decrypt(ciphertext, key) == plaintext


@pytest.mark.timeout(TIME_LIMIT)
# @pytest.mark.skip()
@pytest.mark.parametrize(
    "ciphertext, candidates",
    get_cases("test_case", "ciphertext", "candidates"),
)
def test_analyze(ciphertext: str, candidates: set[str]):
    """Testing the analysis"""
    if candidates:
        assert analyze(ciphertext) == set(candidates)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
