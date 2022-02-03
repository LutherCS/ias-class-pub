# Caesar Cipher

## General setup

- Create an empty **private** repository on GitHub and clone *ias-class-pub* there. Invite me as a collaborator to your private repository.

- Checkout branch main of the course repository. It contains all the input files, code templates, and the tests necessary to complete this assignment.

## Task

- Read the input file *cipher_1.txt* encrypted using Caesar's cipher with an unknown shift value. See function `encrypt` for the algorithm details.

- Find the shift value, decrypt the file *cipher_1.txt*, and write the plaintext to the *plaintext_1.txt*.
    - Idea: try every possible shift value and check if the decrypted first word is in the dictionary (*wordlist_english.txt*).
    - Note: all letters of the cipher are uppercase.

- Read an input file *cipher_2.txt* encrypted using Caesar's cipher with an unknown shift value. Keep in mind that this file has been obfuscated (does not have spaces or punctuation).

- Find the shift value, decrypt the file *cipher_2.txt*, and write the plaintext to the *plaintext_2.txt*.
    - Idea: try every possible shift value and check if the decrypted first word is in the dictionary (*wordlist_english.txt*). You need to gradually increase the length of a candidate first word.
    - Hint: the first word is longer than 3 letters

- Provided unit tests can help you verify some, but not all the functionality of your program. You are free to add more tests if you like. 

- Commit your solution and push changes to your private repository.
