#!/usr/bin/python3
"""
Testing the custom VPN implementation
Roman Yasinovskyy, 2020
"""


import pytest
from Crypto.Cipher import XOR, DES, AES, Blowfish
from Crypto.Hash import SHA256, HMAC
from src.projects.vpn.server import parse_proposal
from src.projects.vpn.server import select_cipher
from src.projects.vpn.server import generate_cipher_response
from src.projects.vpn.server import parse_dhm_request
from src.projects.vpn.server import get_key_and_iv
from src.projects.vpn.server import generate_dhm_response
from src.projects.vpn.server import read_message
from src.projects.vpn.server import validate_hmac


@pytest.mark.parametrize(
    "proposal, ciphers",
    [
        ("ProposedCiphers:AES:[256]", {"AES": [256]},),
        (
            "ProposedCiphers:AES:[128,192,256],Blowfish:[112,224,448],DES:[56]",
            {"AES": [128, 192, 256], "Blowfish": [112, 224, 448], "DES": [56]},
        ),
    ],
)
def test_parse_proposal(proposal, ciphers):
    """Testing proposal parsing"""
    assert parse_proposal(proposal) == ciphers


@pytest.mark.parametrize(
    "supported, proposed, selection",
    zip(
        [
            {"AES": [128]},
            {"AES": [256], "Blowfish": [224, 448]},
            {"AES": [128, 256], "Blowfish": [112, 224]},
        ],
        [{"DES": [56], "AES": [128, 192, 256], "Blowfish": [112, 224, 448]}] * 3,
        [("AES", 128), ("Blowfish", 448), ("AES", 256)],
    ),
)
def test_select_cipher(supported, proposed, selection):
    """Testing cipher selection"""
    assert select_cipher(supported, proposed) == selection


@pytest.mark.parametrize(
    "supported, proposed",
    zip(
        [
            {"AES": [128]},
            {"AES": [256], "Blowfish": [224, 448]},
            {"AES": [128, 256], "Blowfish": [112, 224]},
        ],
        [{"AES": [256]}, {"DES": [56]}, {"Blowfish": [448]}],
    ),
)
def test_select_cipher_error(supported, proposed):
    """Testing cipher selection error"""
    with pytest.raises(ValueError) as err:
        select_cipher(supported, proposed)
    assert str(err.value) == "Could not agree on a cipher"


@pytest.mark.parametrize(
    "cipher, key, response",
    zip(
        ["AES", "Blowfish", "DES"],
        [128, 224, 56],
        ["ChosenCipher:AES,128", "ChosenCipher:Blowfish,224", "ChosenCipher:DES,56"],
    ),
)
def test_generate_cipher_response(cipher, key, response):
    """Testing response generation"""
    assert generate_cipher_response(cipher, key) == response


@pytest.mark.parametrize(
    "message, value", [("DHMKE:101", 101), ("DHMKE:8946513853", 8946513853)]
)
def test_parse_dhm_request(message, value):
    """Testing DHM request parsing"""
    assert parse_dhm_request(message) == value


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
    "value, message", [(101, "DHMKE:101"), (8946513853, "DHMKE:8946513853")]
)
def test_generate_dhm_response(value, message):
    """Testing DHM response generations"""
    assert generate_dhm_response(value) == message


@pytest.mark.parametrize(
    "ciphertext, key, iv, plaintext, hmac",
    [
        (
            b"\xa6\xd3/\x9aW\xdb\xb5\xd2s\xb8\xb8\xc4\x90\x1dl[051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
            b"49094793659111181547021843208480",
            b"2442744371103948",
            "infosec",
            "051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
        ),
        (
            b"\xc5\xec\x00h\xac\xe6L\x8c\xdaM\xf61OtgWc7593c078051c1982878fb0d239f51350a33b519009a03da8d3668b496737ec2",
            b"2e97c59d79d1b1483364113f55d92b41",
            b"fbcf95cef4b0cb47",
            "octoduck",
            "c7593c078051c1982878fb0d239f51350a33b519009a03da8d3668b496737ec2",
        ),
        (
            b"\xfb\xd2\xd3\xc4j\xa4\t\x83\x8e\x0b\x15\xf3\x06\xd7<\x1f\x91Q%\xb3\xaf\x1e\xc0\xef2e\xaa}\xa3m:\xea\x0b\xfa=\x16\x1co\xf3\x0f\xedv\x8d\xd4:g \x1d1b072fe79eda09516021f7a5a99107524bb7846ea66efa9ae19b146144791416",
            b"2e97c59d79d1b148",
            b"3364113f55d92b41",
            "Information Assurance and Security",
            "1b072fe79eda09516021f7a5a99107524bb7846ea66efa9ae19b146144791416",
        ),
    ],
)
def test_read_message(ciphertext, key, iv, plaintext, hmac):
    """Testing message decryption"""
    crypto = AES.new(key, AES.MODE_CBC, iv)
    message, hmac_check = read_message(ciphertext, crypto)
    assert message == plaintext
    assert hmac_check == hmac


@pytest.mark.parametrize(
    "message, hmac_in, key",
    [
        (
            b"\xa6\xd3/\x9aW\xdb\xb5\xd2s\xb8\xb8\xc4\x90\x1dl[051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
            "051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
            b"49094793659111181547021843208480",
        ),
        (
            b"\xfb\xd2\xd3\xc4j\xa4\t\x83\x8e\x0b\x15\xf3\x06\xd7<\x1f\x91Q%\xb3\xaf\x1e\xc0\xef2e\xaa}\xa3m:\xea\x0b\xfa=\x16\x1co\xf3\x0f\xedv\x8d\xd4:g \x1d1b072fe79eda09516021f7a5a99107524bb7846ea66efa9ae19b146144791416",
            "1b072fe79eda09516021f7a5a99107524bb7846ea66efa9ae19b146144791416",
            b"2e97c59d79d1b148",
        ),
    ],
)
def test_validate_hmac(message, hmac_in, key):
    """Testing HMAC validation"""
    hashing = HMAC.new(key, digestmod=SHA256)
    assert validate_hmac(message, hmac_in, hashing)


@pytest.mark.parametrize(
    "message, hmac_in, key",
    [
        (
            b"\xa6\xd3/\x9aW\xdb\xb5\xd2s\xb8\xb8\xc4\x90\x1dl[051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb96",
            "051b7f5638e3a1d0eda1fd638ec35b333cda0c4497e90b9722c70934ab40eb99",
            b"49094793659111181547021843208480",
        ),
    ],
)
def test_validate_hmac_err(message, hmac_in, key):
    """Testing HMAC validation"""
    hashing = HMAC.new(key, digestmod=SHA256)
    with pytest.raises(ValueError) as err:
        assert validate_hmac(message, hmac_in, hashing)
    assert str(err.value) == "Bad HMAC"


if __name__ == "__main__":
    pytest.main(["-v", "test_server.py"])
