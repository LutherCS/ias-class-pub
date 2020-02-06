#!/usr/bin/env python3
# encoding: UTF-8
"""
Testing the Caesar cipher
Roman Yasinovskyy, 2018
"""

import pytest
from src.projects.caesar import caesar_cipher as cc


def test_shift_by_n():
    """Testing shift_by_n() method"""
    assert cc.shift_by_n("hello", 3, 1) == "khoor"
    assert cc.shift_by_n("ZRUOG", 3, -1) == "WORLD"


def test_encrypt():
    """Testing encrypt() method"""
    assert cc.encrypt("hello", 3) == "KHOOR"
    assert cc.encrypt("hello world!", 3) == "KHOOR ZRUOG!"


def test_encrypt_and_obfuscate():
    """Testing encrypt() method with obfuscation"""
    assert cc.encrypt("hello world", 3, True) == "KHOORZRUOG"
    assert cc.encrypt("hello world!", 3, True) == "KHOORZRUOG"


def test_decrypt():
    """Testing decrypt() method"""
    assert cc.decrypt("ZRUOG", 3) == "world"
    assert cc.decrypt("KHOOR ZRUOG!", 3) == "hello world!"


if __name__ == "__main__":
    pytest.main(["-v", "test_caesar_cipher.py"])
