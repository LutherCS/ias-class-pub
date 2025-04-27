# Capture the Flag

## Objective

Find flags hidden within the web application (see link on KATIE).
Most flags appear as plaintext (`flag{sha256value}`) in various parts of the application but a few flags can be found in other formats:
- `base64`-encoded
- hex dumps
- text embedded inside an image

You are encouraged to explore the application and try various methods of accessing it but you should not need to exploit any vulnerabilities to find flags.
Rely on your experience (including class discussions) in this class and the prerequisite courses to find the flags.

## Useful tools

Even though most flags are plaintext it may not be easy to spot them.
The following tools can be helpful:

1. `base64`
2. `curl`
3. `exif`
3. `exiftool`
4. `file`
5. `strings`
6. `xxd`

## Scoring

Each flag must be submitted to the scoreboard (link on KATIE) in the folowing format: `flag{sha256value}`.

**Only use the scoreboard to claim flags.**

## Write-up

Each team must submit a description of their approach to the project.
The write-up must include the following:
- A screenshot of the flag
- Flag location (file name)
- Methodology used to find the flag

An example of a good write-up can be found at [PicoCTF 2018 Writeup: Web Exploitation · Alan's Blog](https://tcode2k16.github.io/blog/posts/picoctf-2018-writeup/web-exploitation/)
