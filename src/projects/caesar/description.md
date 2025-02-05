# Caesar cipher

Implement the Caesar cipher.

## Task

Implement functions `shift_by_n`, `encrypt`, and `decrypt` in the *caesar_cipher.py*.

Verify your solution by passing the provided unit tests.

## Challenge

Analyze and decrypt files *ciphertext_0.txt*, *ciphertext_1.txt*, and *ciphertext_2.txt* found in the data directory.

Implement function `analyze_file` that tries various shift values and looks for candidate words in the dictionary file.

Assume all letters of the ciphertext are uppercase.

### Idea

1. Read the input file  encrypted using Caesar's cipher with an unknown shift value.
2. Try every possible shift value and check if the decrypted first word is in the dictionary.
3. Once a possible shift value is found, decrypt the file and write the plaintext to the output file.
