#!/usr/bin/python3
"""
Testing the A5/1 cipher
@author: Roman Yasinovskyy
"""


import pytest
from src.projects.a51 import a51_cipher as a51
from hashlib import sha256
from pathlib import Path

given_registers = [
    {
        "x": "1010101010101010101",
        "y": "1100110011001100110011",
        "z": "11100001111000011110000",
    },
    {
        "x": "0101010101010101010",
        "y": "0011001100110011001100",
        "z": "00011100011100011100011",
    },
]

given_registers_stepped = [
    {
        "x": "0101010101010101010",
        "y": "0110011001100110011001",
        "z": "11110000111100001111000",
    },
    {
        "x": "0010101010101010101",
        "y": "0001100110011001100110",
        "z": "00001110001110001110001",
    },
]

bits_without_stepping = [0, 1]

keystreams = ["10000011", "11100101"]

ciphers = ["11011010", "10111100"]

phrases_plain = ["Yakety Yak", "Bippity bippity bop", "Luther College"]

secrets = ["octoduck", "security", "infosec"]  # pad with right 0 if necessary

generated_registers = [
    {
        "x": "0110111101100011011",
        "y": "1010001101111011001000",
        "z": "11101010110001101101011",
    },
    {
        "x": "0111001101100101011",
        "y": "0001101110101011100100",
        "z": "11010010111010001111001",
    },
    {
        "x": "0110100101101110011",
        "y": "0011001101111011100110",
        "z": "11001010110001100000000",
    },
]

phrases_encrypted = [
    "0x5c2cb46763deeaddb318",
    "0xc8b591d8c66baf33a5a324cc7665d310bf3b95",
    "0xa9f26f6116b87927b693e31152e7",
]


def test_majority():
    """Testing majority function"""
    assert a51.majority("0", "0", "0") == "0"
    assert a51.majority("0", "0", "1") == "0"
    assert a51.majority("0", "1", "0") == "0"
    assert a51.majority("0", "1", "1") == "1"
    assert a51.majority("1", "0", "0") == "0"
    assert a51.majority("1", "0", "1") == "1"
    assert a51.majority("1", "1", "0") == "1"
    assert a51.majority("1", "1", "1") == "1"


@pytest.mark.parametrize(
    "old_xyz, new_xyz", zip(given_registers, given_registers_stepped)
)
def test_step_x(old_xyz, new_xyz):
    assert a51.step_x(old_xyz["x"]) == new_xyz["x"]


@pytest.mark.parametrize(
    "old_xyz, new_xyz", zip(given_registers, given_registers_stepped)
)
def test_step_y(old_xyz, new_xyz):
    assert a51.step_y(old_xyz["y"]) == new_xyz["y"]


@pytest.mark.parametrize(
    "old_xyz, new_xyz", zip(given_registers, given_registers_stepped)
)
def test_step_z(old_xyz, new_xyz):
    assert a51.step_z(old_xyz["z"]) == new_xyz["z"]


@pytest.mark.parametrize("secret, xyz", zip(secrets, generated_registers))
def test_populate_registers(secret, xyz):
    """Testing register population function"""
    x, y, z = a51.populate_registers(secret)
    assert x == xyz["x"]
    assert y == xyz["y"]
    assert z == xyz["z"]


@pytest.mark.parametrize("xyz, bit", zip(given_registers, bits_without_stepping))
def test_generate_bit(xyz, bit):
    """Testing bit generation"""
    assert a51.generate_bit(**xyz) == bit


@pytest.mark.parametrize("xyz, keystream", zip(given_registers, keystreams))
def test_generate_keystream(xyz, keystream):
    """Testing keystream generation"""
    plaintext = "Y"  # Only used to get length of the keystream
    assert a51.generate_keystream(plaintext, **xyz) == keystream


@pytest.mark.parametrize(
    "xyz, keystream, ciphertext", zip(given_registers, keystreams, ciphers)
)
def test_encrypt_letter(xyz, keystream, ciphertext):
    """Testing letter encryption"""
    plaintext = "Y"
    keystream = a51.generate_keystream(plaintext, **xyz)
    assert a51.encrypt(plaintext, keystream) == ciphertext


@pytest.mark.parametrize(
    "plaintext, secret, ciphertext", zip(phrases_plain, secrets, phrases_encrypted)
)
def test_encrypt_text(plaintext, secret, ciphertext):
    """Testing phrase encryption"""
    x, y, z = a51.populate_registers(secret)
    keystream = a51.generate_keystream(plaintext, x, y, z)
    assert hex(int(a51.encrypt(plaintext, keystream), 2)) == ciphertext


def test_encrypt_file():
    """Testing file encryption"""
    filename = "data/projects/a51/roster"
    a51.encrypt_file("data/projects/a51/roster", "martin")
    encrypted_file = Path(filename)
    if encrypted_file.exists():
        assert (
            sha256(open(f"{filename}.secret", "rb").read()).hexdigest()
            == "c6cffc32f7c20ecbbfd633796696359e05abcf09f1c8e96508162dd6f738752d"
        )


if __name__ == "__main__":
    pytest.main(["-v", "test_a51_cipher.py"])
