#!/usr/bin/python3
"""
Testing the custom VPN implementation
Roman Yasinovskyy, 2020
"""


import pytest
from Crypto.Cipher import AES, DES, Blowfish
from Crypto.Hash import SHA256, HMAC
from src.projects.vpn.client import generate_cipher_proposal
from src.projects.vpn.client import parse_cipher_selection
from src.projects.vpn.client import generate_dhm_request
from src.projects.vpn.client import parse_dhm_response
from src.projects.vpn.client import get_key_and_iv
from src.projects.vpn.client import add_padding
from src.projects.vpn.client import encrypt_message


@pytest.mark.parametrize(
    "supported, message",
    [
        ({"AES": [256]}, "ProposedCiphers:AES:[256]"),
        ({"AES": [128, 192, 256]}, "ProposedCiphers:AES:[128,192,256]"),
        (
            {"AES": [128, 192, 256], "Blowfish": [112, 224, 448], "DES": [56]},
            "ProposedCiphers:AES:[128,192,256],Blowfish:[112,224,448],DES:[56]",
        ),
    ],
)
def test_generate_cipher_proposal(supported, message):
    """Test proposal generation"""
    assert generate_cipher_proposal(supported) == message


@pytest.mark.parametrize(
    "message, cipher_name, key_size",
    [
        ("ChosenCipher:AES,128", "AES", 128),
        ("ChosenCipher:Blowfish,224", "Blowfish", 224),
        ("ChosenCipher:DES,56", "DES", 56),
    ],
)
def test_parse_cipher_selection(message, cipher_name, key_size):
    """Test selection parsing"""
    assert parse_cipher_selection(message) == (cipher_name, key_size)


@pytest.mark.parametrize(
    "value, message", [(101, "DHMKE:101"), (8946513853, "DHMKE:8946513853")]
)
def test_generate_dhm_request(value, message):
    """Test DHMKE message generation"""
    assert generate_dhm_request(value) == message


@pytest.mark.parametrize(
    "message, value", [("DHMKE:101", 101), ("DHMKE:8946513853", 8946513853)]
)
def test_parse_dhm_response(message, value):
    """Test DHMKE message parsing"""
    assert parse_dhm_response(message) == value


@pytest.mark.parametrize(
    "shared_key, cipher_name, key_size, cipher, key, iv",
    [
        ("123456789", "DES", 56, DES, b"1234567\x00", b"23456789"),
        (
            "2e97c59d79d1b1483364113f55d92b41b7d2deb25b637416fbcf95cef4b0cb47",
            "AES",
            128,
            AES,
            b"2e97c59d79d1b148",
            b"fbcf95cef4b0cb47",
        ),
        (
            "2e97c59d79d1b1483364113f55d92b41b7d2deb25b637416fbcf95cef4b0cb47",
            "AES",
            256,
            AES,
            b"2e97c59d79d1b1483364113f55d92b41",
            b"fbcf95cef4b0cb47",
        ),
        (
            "2e97c59d79d1b1483364113f55d92b41b7d2deb25b637416fbcf95cef4b0cb47",
            "Blowfish",
            224,
            Blowfish,
            b"2e97c59d79d1b1483364113f55d9",
            b"f4b0cb47",
        ),
    ],
)
def test_get_key_and_iv(shared_key, cipher_name, key_size, cipher, key, iv):
    """Test extracting key and IV from the generated shared secret"""
    assert get_key_and_iv(shared_key, cipher_name, key_size) == (cipher, key, iv)


@pytest.mark.parametrize(
    "message, padded",
    [
        ("hello", "hello\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"),
        ("infosec", "infosec\x00\x00\x00\x00\x00\x00\x00\x00\x00"),
        (
            "Information Assurance and Security",
            "Information Assurance and Security\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        ),
    ],
)
def test_add_padding(message, padded):
    """Testing message padding"""
    assert add_padding(message) == padded


@pytest.mark.parametrize(
    "plaintext, key, iv, ciphertext, hmac",
    [
        (
            "infosec",
            b"49094793659111181547021843208480",
            b"2442744371103948",
            b"\xa6\xd3/\x9aW\xdb\xb5\xd2s\xb8\xb8\xc4\x90\x1dl[",
            "051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
        ),
        (
            "octoduck",
            b"2e97c59d79d1b1483364113f55d92b41",
            b"fbcf95cef4b0cb47",
            b"\xc5\xec\x00h\xac\xe6L\x8c\xdaM\xf61OtgW",
            "c7593c078051c1982878fb0d239f51350a33b519009a03da8d3668b496737ec2",
        ),
        (
            "Information Assurance and Security",
            b"2e97c59d79d1b148",
            b"3364113f55d92b41",
            b"\xfb\xd2\xd3\xc4j\xa4\t\x83\x8e\x0b\x15\xf3\x06\xd7<\x1f\x91Q%\xb3\xaf\x1e\xc0\xef2e\xaa}\xa3m:\xea\x0b\xfa=\x16\x1co\xf3\x0f\xedv\x8d\xd4:g \x1d",
            "1b072fe79eda09516021f7a5a99107524bb7846ea66efa9ae19b146144791416",
        ),
    ],
)
def test_encrypt_message(plaintext, key, iv, ciphertext, hmac):
    """Testing message encryption"""
    crypto = AES.new(key, AES.MODE_CBC, iv)
    hashing = HMAC.new(key, digestmod=SHA256)
    ciph_out, hmac_out = encrypt_message(plaintext, crypto, hashing)
    assert ciph_out == ciphertext
    assert hmac_out == hmac


if __name__ == "__main__":
    pytest.main(["-v", "test_client.py"])
