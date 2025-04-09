# Password Manager

## Purpose

Build a web app to securely store user passwords.

## Technical requirements

1. User-friendly front-end using any CSS/HTML framework.
2. Back-end implemented using **Flask**.
3. User accounts and profiles stored in the **SQLite3** database.

## Functional requirements

Users should be able to:

1. Register an *account* with your application using username and password.
2. OPTIONAL: Edit account information.
3. OPTIONAL: Deactivate (delete) their account.
4. Log into an existing account.
5. Create any number of *profiles* (username, password, and expiration date).
6. Edit username, password, and expiration date for any profile already created.
7. Delete any profile already created.
8. See password strength for any profile already created.
9. OPTIONAL: Generate a strong password for a profile.

The application must generate user encryption key based on the account password and the **application secret** (see `scrypt` of the `hashlib` module for details).

The application must store all user account data in the table `account` with the following fields:

- `id`: (automatically generated) user identifier
- `username`: account name (e.g. email)
- `password`: account password (salted and hashed using `bcrypt`)
- `key`: user's 256-bit key (derived from the account password)

The application must store all user profile data in the table `profile` with the following fields:

- `id`: profile identifier
- `user`: user identifier (a foreign key to the `account` table)
- `name`: profile name (e.g. Work, NorseKey etc.)
- `username`: username in the profile (**encrypted** using AES)
- `password`: profile password (**encrypted** using AES)
- `expires`: profile password expiration date

The application must display all profiles for a **logged in** user with the strength of each password as follows:

| Entropy bits  | Strength   |
|---------------|------------|
| Fewer than 50 | Weak       |
| 50 – 79       | Acceptable |
| 80 or more    | Strong     |

## References

- [Password Entropy: The Value of Unpredictable Passwords | Okta](https://www.okta.com/identity-101/password-entropy/)
- [Password Entropy: What It Is and Why It’s Important](https://www.keepersecurity.com/blog/2024/03/04/password-entropy-what-it-is-and-why-its-important/)
- [hashlib — Secure hashes and message digests — Python 3.13.3 documentation](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt)
