#!/usr/bin/env python3
# encoding: UTF-8
"""Caesar cipher"""

DICT_ENG = set()


def shift_by_n(word: str, shift: int, direction: int) -> str:
    """Shifting all letters in a word by n. Direction specifies encryption (>0) or decryption (<0)"""
    # TODO: Implement this function
    ...


def encrypt(plaintext: str, shift: int, obfuscate=False) -> str:
    """Encrypt and optionally obfuscate a string"""
    cipher = shift_by_n(plaintext, shift, 1).upper()  # 1 for encryption
    if obfuscate:
        punctuation = ";:,.!?'() \n\t"
        for symbol in punctuation:
            cipher = cipher.replace(symbol, "")
    return cipher


def encrypt_file(file_in_name: str, file_out_name: str, shift: int, obfuscate=False):
    """Encrypt a file and write the cipher to a file"""
    with open(file_in_name, "r", encoding="utf-8") as file_in:
        plaintext = file_in.read().lower()
    cipher = encrypt(plaintext, shift, obfuscate)
    with open(file_out_name, "w", encoding="utf-8") as file_out:
        file_out.write(cipher)


def decrypt(cipher: str, shift: int) -> str:
    """Decrypt a string"""
    # TODO: Implement this function
    ...


def decrypt_file(file_in_name: str, file_out_name: str, shift: int):
    """Decrypt a file that has not been obfuscated"""
    with open(file_in_name, "r", encoding="utf-8") as file_in:
        cipher = file_in.read()
    plaintext = decrypt(cipher, shift)
    with open(file_out_name, "w", encoding="utf-8") as file_out:
        file_out.write(plaintext)


def analyze_file(file_in_name: str, file_out_name: str, dictionary: set):
    """Analyze a file that has been obfuscated"""
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    print("---Caesar cipher---")
    analyze_file("cipher_1.txt", "plaintext_1.txt", DICT_ENG)
    analyze_file("cipher_2.txt", "plaintext_2.txt", DICT_ENG)
    print("---Over and out---")


if __name__ == "__main__":
    main()
