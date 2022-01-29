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

## Selecting a First Word

When a word is chosen in Wordle any matching letters to the target word are highlighted, helping the player determine the target word.  A good first word in Wordle would be chosen to maximize the probability of matching the letters in the target word.  A secondary benefit is that any letters that don't match can be excluded from consideration for the target word.  Therefore a starting word should be chosen to maximize the use of frequently occurring characters while avoiding duplicates as duplicate letters give comparatively less information.

The following procedure was used to rank words from the overall word list in order of their usfulness as starting words:
- Compute the frequency of each letter
- Iterate through the overall list of words
  - Exclude any words that have duplicate letters
  - Sum the relative frequencies of the letters in the word
- The resulting weighted list of words is then sorted in descending order of the sum of relative frequencies and the top N choices are displayed

The resulting list of top 10 words with the relative weighting are:
1. arose: 230.47
2. raise: 224.38
3. arise: 224.38
4. aloes: 224.35
5. stoae: 224.34
6. laser: 224.26
7. earls: 224.26
8. reals: 224.26
9. tears: 224.25
10. rates: 224.25
