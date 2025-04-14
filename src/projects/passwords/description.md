# Password Cracking

Directory _data/projects/passwords/_ contains 5 data files with usernames and their hashed passwords in various formats (Windows, Linux, web, MySQL).
Crack as many passwords as you can using any legal tool, dictionary, and service available.

## Input files

Input files contain hashed passwords in the following formats:

- _sam_: Windows NTLMv1
- _passwd_: Linux users
- _shadow_: Linux users
- _shadow2_: Linux users
- _users_: MySQL users

## Deliverables

Update file _solution.txt_.
The format of your answers should be **username:password**.

Describe your approach and methodology in the file _approach.md_.
Preserve the records of your intermediate steps (logs, commands etc) in case I ask you to explain your results.

Keep in mind that password cracking is a time-consuming task. That's why you have a few **weeks** to complete this project.

## References

- [NTLM - Wikipedia](https://en.wikipedia.org/wiki/NTLM)
- [crypt(5) — libcrypt-dev — Debian unstable — Debian Manpages](https://manpages.debian.org/unstable/libcrypt-dev/crypt.5.en.html)
- [MySQL :: MySQL 8.4 Reference Manual :: 14.13 Encryption and Compression Functions](https://dev.mysql.com/doc/refman/8.4/en/encryption-functions.html#function_password)