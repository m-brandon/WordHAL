# WordHAL Analysis

## Frequency of Letters

[An analysis](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html) of the frequency of letters in words in the English language as listed in the main entries of the Concise Oxford Dictionary shows the following frequency of English letters, normalized to the occurance of the least common (i.e. a letter with a score of 20 is twenty times more likely to appear than the least common letter):

| Letter | Proportion | Letter | Proportion |
| :---: | :---: | :---: | :---: |
| E | 56.88 | M | 15.36 |
| A | 43.31 | H | 15.31 |
| R | 38.64 | G | 12.59 |
| I | 38.45 | B | 10.56 |
| O | 36.51 | F | 9.24 |
| T | 35.43 | Y | 9.06 |
| N | 33.92 | W | 6.57 |
| S | 29.93 | K | 5.61 |
| L | 27.98 | V | 5.13 |
| C | 23.13 | X | 1.48 |
| U | 18.51 | Z | 1.39 |
| D | 17.25 | J | 1 |
| P | 16.14 | Q | 1 |

Using the list of five letter words, the [run_analyze_letter_frequency.py](https://github.com/m-brandon/WordHAL/blob/main/run_analyze_letter_frequency.py) finds the following normalized list of letter frequencies:

| Letter | Proportion | Letter | Proportion |
| :---: | :---: | :---: | :---: |
| S | 57.23 | Y | 16.72 |
| E | 56.77 | M | 15.91 |
| A | 44.3 | H | 15.36 |
| O | 36.13 | B | 13.49 |
| R | 36.04 | G | 12.81 |
| I | 30.04 | K | 11.25 |
| L | 29.92 | F | 10.58 |
| T | 29.91 | W | 9.53 |
| N | 24.25 | V | 6.0 |
| D | 22.28 | X | 2.62 |
| U | 20.55 | Z | 2.55 |
| C | 18.19 | J | 1.68 |
| P | 18.02 | Q | 1.0 |

Several letters, including "S" and "O" have a different relative frequency in the list of five letter words than the complete list of words in the English language.
