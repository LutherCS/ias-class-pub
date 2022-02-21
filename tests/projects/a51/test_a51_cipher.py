#!/usr/bin/python3
"""
Testing the A5/1 cipher

@authors: Roman Yasinovskyy
@version: 2022.2
"""

import importlib
import pathlib
import sys
from typing import Generator
from hashlib import sha256

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.a51 import a51_cipher as a51


DATA_DIR = pathlib.Path("data/projects/a51/")
TIME_LIMIT = 2


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
def test_majority():
    """Testing the majority function"""
    for bits, expected in zip(range(8), "00010111"):
        assert a51.majority(*tuple(f"{bits:03b}")) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "registers_given, registers_stepped",
    get_cases("test_case_basic", "registers_given", "registers_stepped"),
)
def test_stepping(registers_given: dict[str, str], registers_stepped: dict[str, str]):
    """Testing the stepping function"""
    assert a51.step_x(registers_given["x"]) == registers_stepped["x"]
    assert a51.step_y(registers_given["y"]) == registers_stepped["y"]
    assert a51.step_z(registers_given["z"]) == registers_stepped["z"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "registers_given, generated_bit",
    get_cases("test_case_basic", "registers_given", "generated_bit"),
)
def test_bit_generation(registers_given: dict[str, str], generated_bit: int):
    """Testing bit generation"""
    assert a51.generate_bit(**registers_given) == generated_bit


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "registers_given, keystream",
    get_cases("test_case_basic", "registers_given", "keystream"),
)
def test_keystream_generation(registers_given: dict[str, str], keystream: str):
    """Testing keystream generation"""
    plaintext = "U"  # Only used to get length of the keystream, 8 bits
    assert a51.generate_keystream(plaintext, **registers_given) == keystream


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keystream, ciphertext",
    get_cases("test_case_basic", "keystream", "ciphertext"),
)
def test_encrypt_char(keystream: str, ciphertext: str):
    """Testing encryption of a single character"""
    plaintext = "U"  # Only used to get length of the keystream, 8 bits
    assert a51.encrypt(plaintext, keystream) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "secret, generated_registers",
    get_cases("test_case_encryption", "secret", "generated_registers"),
)
def test_populate_registers(secret: str, generated_registers: dict[str, str]):
    """Testing generation of the registers"""
    gen_reg_x, gen_reg_y, gen_reg_z = a51.populate_registers(secret)
    assert gen_reg_x == generated_registers["x"]
    assert gen_reg_y == generated_registers["y"]
    assert gen_reg_z == generated_registers["z"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, secret, ciphertext",
    get_cases("test_case_encryption", "plaintext", "secret", "ciphertext"),
)
def test_encrypt_text(plaintext: str, secret: str, ciphertext: str):
    """Testing encryption of a string"""
    x, y, z = a51.populate_registers(secret)
    keystream = a51.generate_keystream(plaintext, x, y, z)
    assert hex(int(a51.encrypt(plaintext, keystream), 2)) == ciphertext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, secret, ciphertext",
    get_cases("test_case_encryption", "plaintext", "secret", "ciphertext"),
)
def test_decrypt_text(plaintext: str, secret: str, ciphertext: str):
    """Testing decryption of a string"""
    x, y, z = a51.populate_registers(secret)
    keystream = a51.generate_keystream(plaintext, x, y, z)
    assert a51.decrypt(ciphertext, keystream) == plaintext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, secret, checksum",
    get_cases("test_case_file_encryption", "filename", "secret", "checksum"),
)
def test_encrypt_file(filename: str, secret: str, checksum: str):
    """Testing file encryption"""
    a51.encrypt_file(pathlib.Path(DATA_DIR / filename), secret)
    encrypted_file = pathlib.Path(DATA_DIR / filename)
    if encrypted_file.exists():
        assert (
            sha256(
                open(pathlib.Path(DATA_DIR / f"{filename}.secret"), "rb").read()
            ).hexdigest()
            == checksum
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
