# WordHAL Analysis

## Frequency of Letters

[An analysis](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html) of the frequency of letters in words in the English language as listed in the main entries of the Concise Oxford Dictionary shows the following frequency of English letters, normalized to the occurance of the least common (i.e. a letter with a score of 20 is twenty times more likely to appear than the least common letter):

| Letter | Proportion | Letter | Proportion | Letter | Proportion |
| :---: | :---: | :---: | :---: | :---: | :---: |
| E | 56.88 | C | 23.13 | Y | 9.06 |
| A | 43.31 | U | 18.51 | W | 6.57 |
| R | 38.64 | D | 17.25 | K | 5.61 |
| I | 38.45 | P | 16.14 | V | 5.13 |
| O | 36.51 | M | 15.36 | X | 1.48 |
| T | 35.43 | H | 15.31 | Z | 1.39 |
| N | 33.92 | G | 12.59 | J | 1 |
| S | 29.93 | B | 10.56 | Q | 1 |
| L | 27.98 | F | 9.24  | |

Using the list of five letter words, the [run_analyze_letter_frequency.py](https://github.com/m-brandon/WordHAL/blob/main/run_analyze_letter_frequency.py) finds the following normalized list of letter frequencies:

| Letter | Proportion | Letter | Proportion | Letter | Proportion |
| :---: | :---: | :---: | :---: | :---: | :---: |
| S | 57.23 | D | 22.28 | K | 11.25 |
| E | 56.77 | U | 20.55 | F | 10.58 |
| A | 44.3  | C | 18.19 | W | 9.53 |
| O | 36.13 | P | 18.02 | V | 6.0 |
| R | 36.04 | Y | 16.72 | X | 2.62 |
| I | 30.04 | M | 15.91 | Z | 2.55 |
| L | 29.92 | H | 15.36 | J | 1.68 |
| T | 29.91 | B | 13.49 | Q | 1.0 |
| N | 24.25 | G | 12.81 | |

Several letters, including "S" and "O" have a different relative frequency in the list of five letter words than the complete list of words in the English language.
