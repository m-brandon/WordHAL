# WordHAL
[Wordle](https://www.powerlanguage.co.uk/wordle/) analysis and suggestions

## Word Source

The list of words found in [five-letter-word-list.txt](https://github.com/m-brandon/WordHAL/blob/main/five-letter-word-list.txt) is taken from [Donald Knuth's](https://en.wikipedia.org/wiki/Donald_Knuth) list of words that he's used in computer science curricula.  The original can be found at [this link](https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt).

It contains 5757 five letter words which according to [this site](https://charlesreid1.com/wiki/Five_Letter_Words) meet the following criteria:
- No proper nouns
- No punctuation, hyphens, or accent marks
- No extremely rare words that would only be useful to Scrabble players

## Current Functionality

The following capabilities are currently implemented in this set of scripts:
- Analyze Letter Frequency:  import all the five letter words in the word list and analyze how frequently each letter, A-Z, occurs in those words.  The script [run_analyze_letter_frequency.py](https://github.com/m-brandon/WordHAL/blob/main/run_analyze_letter_frequency.py) will print out a list of each letter and it's relative frequency sorted from most common to least common.
- Choose Start Word:  ranks all of the words in the word list based on the relative frequency of the letters that make up a word.  Because this is intended to help choose start words for the game, any words that have duplicate letters are excluded from this ranking as duplicate letters provide comparatively less useful information as starting words.
