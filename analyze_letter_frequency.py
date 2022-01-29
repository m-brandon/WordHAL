import config_params as cfg
import load_word_list
import pprint
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


def get_total_letter_count(letter_dict):
    total_letters = 0
    for currkey in letter_dict:
        total_letters += letter_dict[currkey]

    return total_letters


def scale_letter_count(letter_dict, total_letters):
    scaled_letter_dict = dict()
    for currkey in letter_dict:
        scaled_letter_dict[currkey] = letter_dict[currkey] / total_letters

    scaled_letter_dict = dict(sorted(
        scaled_letter_dict.items(), 
        key=lambda item: item[1], 
        reverse=True
    ))

    return scaled_letter_dict


def main():
    word_list = load_word_list.main(cfg.filename_wordlist, cfg.ftype_wordlist)
    letter_dict = create_letter_dict()
    count_letters_in_word_list(word_list, letter_dict)
    scaled_letter_dict = scale_letter_count(
        letter_dict, 
        get_total_letter_count(letter_dict)
    )

    return scaled_letter_dict


if __name__ == "__main__":
    print(f"WordHAL v{cfg.ver_maj}.{cfg.ver_min}")
    print("Letter Frequency Analyzer")
    print("-"*30)

    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

    scaled_letter_dict = main()

    pp.pprint(scaled_letter_dict)
