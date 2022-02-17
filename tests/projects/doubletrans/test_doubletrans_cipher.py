#!/usr/bin/python3
"""
Double transposition cipher testing

@authors: Roman Yasinovskyy
@version: 2022.2
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
    from src.projects.doubletrans import analyze, decrypt, encrypt


DATA_DIR = pathlib.Path("data/projects/doubletrans/")
TIME_LIMIT = 2


@pytest.mark.parametrize(
    "plaintext, row_key, col_key, ciphertext",
    [
        ("hello world!", (2, 1, 0), (3, 2, 1, 0), "!dlrow olleh"),
        ("Luther College", (1, 0), (5, 4, 6, 0, 1, 3, 2), "geeCollre Luht"),
        (
            "Information Assurance and Security.",
            (5, 3, 1, 6, 4, 0, 2),
            (3, 1, 0, 4, 2),
            "cS uenrucaiamotyir.tn edaonIrfs nsA",
        ),
        ("Computer Science", (3, 0, 1, 2), (1, 2, 3, 0), "nceeompCteruSci "),
    ],
)
@pytest.mark.timeout(TIME_LIMIT)
def test_encrypt(plaintext, row_key, col_key, ciphertext):
    """Testing phrase encryption"""
    assert encrypt(plaintext, row_key, col_key) == ciphertext


@pytest.mark.parametrize(
    "ciphertext, row_key, col_key, plaintext",
    [
        ("!dlrow olleh", (2, 1, 0), (3, 2, 1, 0), "hello world!"),
        ("geeCollre Luht", (1, 0), (5, 4, 6, 0, 1, 3, 2), "Luther College"),
        (
            "cS uenrucaiamotyir.tn edaonIrfs nsA",
            (5, 3, 1, 6, 4, 0, 2),
            (3, 1, 0, 4, 2),
            "Information Assurance and Security.",
        ),
        ("nceeompCteruSci ", (3, 0, 1, 2), (1, 2, 3, 0), "Computer Science"),
    ],
)
@pytest.mark.timeout(TIME_LIMIT)
def test_decrypt(ciphertext, row_key, col_key, plaintext):
    """Testing phrase decryption"""
    assert decrypt(ciphertext, row_key, col_key) == plaintext


@pytest.mark.parametrize(
    "ciphertext, candidates",
    [
        ("!dlrow olleh", {"!world hello", "hello world!"}),
        ("geeCollre Luht", {"Luther College"}),
        (
            " taw.natt adakc",
            {"attack at dawn.", "attack dawn. at"},
        ),
        ("nceeompCteruSci ", {"Computer Science"}),
    ],
)
@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.skip()
def test_analyze(ciphertext, candidates):
    """Testing phrase analysis"""
    assert analyze(ciphertext) == candidates


if __name__ == "__main__":
    pytest.main(["-v", __file__])
