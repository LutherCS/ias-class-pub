# Double Transposition Cipher

Implement **double transposition** cipher.

## Implementation

Implement functions `encrypt`, `decrypt`, and `analyze` in the *doubletrans_cipher.py* and pass the provided tests.
See the function docstrings and the textbook for implementation details.

### `encrypt`

`plaintext` string is converted into a matrix with number of rows and columns defined by the `key`.
Then the rows and columns are transposed.

The values in the resulting matrix are joined together in the string, row-by-row, column-by-column, and converted to the uppercase.

### `decrypt`

The `ciphertext` is converted into a matrix with number of rows and columns defined by the `key`.
Then the rows and columns are rearranged.

The values in the resulting matrix are joined together in the string, row-by-row, column-by-column, and converted to lowercase.

### `analyze`

Since the key is unknown, try all possible permutations.
For example, "Hello, world" (12 characters) can be encrypted using matrices 1x12 (but it's time-consuming and doesn't make much sense), 2x6, 3x4, 4x3, 6x2, and 12x1 (equally time-consuming and pointless).
Each of those matrices can have multiple (`n!`) permutations of rows and columns, so manually scanning them can be inefficient.

Try the following heuristics:

- all words of a candidate phrase must be in the dictionary
- punctuation (.,:;!?) should be ignored when comparing to the dictionary words
- comparison should be case-insensitive

Decipher the following phrases and replace `...` in this file with your answer.
You may complete this task programmatically, manually, or using a hybrid approach.

- ' AEWHVA EU NHSOT,OR*E OLBMP' as plaintext is "..."
- 'MISENHTOWEGIDKC HW IA STCSYO*EM ' as plaintext is "..."
- 'TTYME ESR.OY RTDNGI EOSHF EPT OR HPREROSE A   IOMNFT' as plaintext is "..."
- 'TRRONE FOMS.Y UR,OORFF N IT M'NOI , EWRDITJU YS DSFE TIFASE,RTNGRMLI YEAA , RCZY' as plaintext is "..."

You can safely assume that plaintext is in English with spaces and punctuation preserved.

## Dictionary

*data/projects/doubletrans/words* is provided for your convenience.
