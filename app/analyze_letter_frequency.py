import app.config_params as cfg
import app.load_word_list as load_word_list
from string import ascii_uppercase


def create_letter_dict():
    letter_dict = dict()
    for curr_letter in ascii_uppercase:
        letter_dict[curr_letter] = 0

    return letter_dict


def count_letters_in_word(word_in, letter_dict):
    for curr_letter in word_in:
        letter_dict[curr_letter.upper()] += 1


def count_letters_in_word_list(list_in, letter_dict):
    for curr_word in list_in:
        count_letters_in_word(curr_word, letter_dict)


def get_min_letter_count(letter_dict):
    return min(list(letter_dict.values()))


def normalize_letter_count(letter_dict, min_count):
    scaled_letter_dict = dict()
    for currkey in letter_dict:
        scaled_letter_dict[currkey] = round(letter_dict[currkey] / min_count, 2)

    scaled_letter_dict = dict(sorted(
        scaled_letter_dict.items(), 
        key=lambda item: item[1], 
        reverse=True
    ))

    return scaled_letter_dict

def print_relative_freq_table(normalized_letter_dict):
    print("| Letter | Proportion |")
    print("| :---: | :---: |")
    for currkey in normalized_letter_dict:
        print(f"| {currkey} | {normalized_letter_dict[currkey]} |")


def main():
    word_list = load_word_list.main(cfg.filename_wordlist, cfg.ftype_wordlist)
    letter_dict = create_letter_dict()
    count_letters_in_word_list(word_list, letter_dict)
    normalized_letter_dict = normalize_letter_count(
        letter_dict, 
        get_min_letter_count(letter_dict)
    )

    return normalized_letter_dict
