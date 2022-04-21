# Password Generator

## Purpose

Build a web app to generate password(s) based on user preferences.

## Technical requirements

1. User-friendly front-end built with **Bootstrap** or another *HTML/CSS* framework. Use of any *JavaScript* framework is optional.
2. Back-end implemented using any language/framework. Note that **Flask** is already included in the *requirements.txt* of **this** repository but it should not limit your choice of technology.
3. Both front-end and back-end must be deployed and communicate using API.

## Functional requirements

This tool must generate either *passwords* or *passphrases* and the user interface must include the following controls:

1. Characters to be used in a password:
   1. Digits **only** (`/digits`)
   2. Lowercase letters **only** (`/lower`)
   3. Uppercase letters **only** (`/upper`)
   4. Lowercase **and** uppercase letters (`/letters`)
   5. Digits **and** letters (`/alphanum`)
   6. Special printable characters **only** (`/special`)
   7. **All** printable characters (digits, letters, and special) (`/all`)
2. Word **separator** if a passphrase is chosen (e.g. `_` or `*`). Note that words should be chosen randomly from some dictionary (e.g. */usr/share/dict/words*)
3. **Length** of the generated pass-word/-phrase (number of characters in the password or words in the passphrase) (1--30).
4. **Number** of passwords to generate (1--20).

Generated passwords must not include the following characters:

- 0 (zero, `0x30`)
- 1 (one, `0x31`)
- I (uppercase letter I, `0x49`)
- O (uppercase letter O, `0x4F`)
- l (lowercase letter l, `0x6C`)

Generated passwords must be evaluated and their entropy calculated based on the following formula: $E = \log_2(C^L)$, where $C$ is a number of *possible* characters and $L$ is the number of characters in the password. Strength of a password must be communicated to the user based on the following scale:

1. **Very strong** (entropy of 100 bits or more)
2. **Strong** (entropy of 80 bits or more)
3. **Weak** (entropy of 60 bits or more)
4. **Very weak** (entropy of 40 bits or more)
5. **Avoid** (entropy below 40 bits)

**Optionally**, the user should be able to specify characters **not** included in the password (e.g. `\` or `).

## Example

Your API routes should have the following format: `/api/v1/char_pool/passwd_length/passwds_to_generate`, where `char_pool` and `passwd_length` are required, `passwds_to_generate` is optional (defaults to 1).

## References

- [Password Entropy: The Value of Unpredictable Passwords | Okta](https://www.okta.com/identity-101/password-entropy/)
