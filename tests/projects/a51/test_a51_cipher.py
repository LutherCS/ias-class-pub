#!/usr/bin/python3
"""
Testing the A5/1 cipher

@authors: Roman Yasinovskyy
@version: 2025.3
"""

import importlib
import pathlib
import sys
import tomllib
from hashlib import sha256
from typing import Generator

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.a51 import a51_cipher as a51


DATA_DIR = pathlib.Path("data/projects/a51/")
TEST_DIR = pathlib.Path("tests/projects/a51/")
TIME_LIMIT = 2


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
def test_majority():
    """Testing the majority function"""
    for bits, expected in zip(range(8), map(int, list("00010111"))):
        assert a51.majority(*map(int, tuple(f"{bits:03b}"))) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "register_given, register_stepped",
    get_cases("test_case_basic", "register_given", "register_stepped"),
)
def test_step_x(register_given: dict[str, list[int]], register_stepped: dict[str, list[int]]):
    """Testing the stepping function"""
    x = register_given["x"]
    a51.step_x(x)
    assert x == register_stepped["x"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "register_given, register_stepped",
    get_cases("test_case_basic", "register_given", "register_stepped"),
)
def test_step_y(register_given: dict[str, list[int]], register_stepped: dict[str, list[int]]):
    """Testing the stepping function"""
    y = register_given["y"]
    a51.step_y(y)
    assert y == register_stepped["y"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "register_given, register_stepped",
    get_cases("test_case_basic", "register_given", "register_stepped"),
)
def test_step_z(register_given: dict[str, list[int]], register_stepped: dict[str, list[int]]):
    """Testing the stepping function"""
    z = register_given["z"]
    a51.step_z(z)
    assert z == register_stepped["z"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "register_given, generated_bit",
    get_cases("test_case_basic", "register_given", "generated_bit"),
)
def test_generate_bit(register_given: dict[str, list[int]], generated_bit: int):
    """Testing bit generation"""
    assert a51.generate_bit(**register_given) == generated_bit


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "register_given, keystream, plaintext",
    get_cases("test_case_basic", "register_given", "keystream", "plaintext"),
)
def test_generate_keystream(
    register_given: dict[str, list[int]], keystream: list[int], plaintext: str
):
    """Testing keystream generation"""
    assert a51.generate_keystream(len(plaintext), **register_given) == keystream


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "keystream, ciphertext, plaintext",
    get_cases("test_case_basic", "keystream", "ciphertext", "plaintext"),
)
def test_encrypt_char(keystream: list[int], ciphertext: list[int], plaintext: str):
    """Testing encryption of a single character"""
    assert a51.encrypt(plaintext, keystream) == bytearray(ciphertext)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "secret, generated_register",
    get_cases("test_case_general", "secret", "generated_register"),
)
def test_populate_registers(secret: str, generated_register: dict[str, list[int]]):
    """Testing generation of the registers"""
    gen_reg_x, gen_reg_y, gen_reg_z = a51.populate_registers(secret)
    assert gen_reg_x == generated_register["x"]
    assert gen_reg_y == generated_register["y"]
    assert gen_reg_z == generated_register["z"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, secret, ciphertext",
    get_cases("test_case_general", "plaintext", "secret", "ciphertext"),
)
def test_encrypt_text(plaintext: str, secret: str, ciphertext: list[int]):
    """Testing encryption of a string"""
    x, y, z = a51.populate_registers(secret)
    keystream = a51.generate_keystream(len(plaintext), x, y, z)
    assert a51.encrypt(plaintext, keystream) == bytearray(ciphertext)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "plaintext, secret, ciphertext",
    get_cases("test_case_general", "plaintext", "secret", "ciphertext"),
)
def test_decrypt_text(plaintext: str, secret: str, ciphertext: list[int]):
    """Testing decryption of a string"""
    x, y, z = a51.populate_registers(secret)
    keystream = a51.generate_keystream(len(plaintext), x, y, z)
    assert a51.decrypt(bytearray(ciphertext), keystream) == plaintext


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, secret, checksum_cipher",
    get_cases("test_case_file_encryption", "filename", "secret", "checksum_cipher"),
)
def test_encrypt_file(filename: str, secret: str, checksum_cipher: str):
    """Testing file encryption"""
    encrypted_file = pathlib.Path(TEST_DIR / f"{filename}.secret")
    a51.encrypt_file(pathlib.Path(DATA_DIR / filename), secret, encrypted_file)
    assert encrypted_file.exists()
    assert sha256(open(encrypted_file, "rb").read()).hexdigest() == checksum_cipher
    encrypted_file.unlink()


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, secret, checksum_plain",
    get_cases("test_case_file_encryption", "filename", "secret", "checksum_plain"),
)
def test_decrypt_file(filename: str, secret: str, checksum_plain: str):
    """Testing file decryption"""
    decrypted_file = pathlib.Path(TEST_DIR / f"{filename}.txt")
    a51.decrypt_file(pathlib.Path(DATA_DIR / filename).with_suffix(".bin"), secret, decrypted_file)
    assert decrypted_file.exists()
    assert sha256(open(decrypted_file, "rb").read()).hexdigest() == checksum_plain
    decrypted_file.unlink()


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, secret, checksum_plain",
    get_cases("test_case_file_decryption", "filename", "secret", "checksum_plain"),
)
def test_decrypt_more_files(filename: str, secret: str, checksum_plain: str):
    """Testing file decryption"""
    decrypted_file = pathlib.Path(TEST_DIR / f"{filename}.txt")
    a51.decrypt_file(pathlib.Path(DATA_DIR / filename).with_suffix(".bin"), secret, decrypted_file)
    assert decrypted_file.exists()
    assert sha256(open(decrypted_file, "rb").read()).hexdigest() == checksum_plain
    decrypted_file.unlink()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
