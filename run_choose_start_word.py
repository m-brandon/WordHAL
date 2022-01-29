import app.choose_start_word
import app.disp_intro_string
import argparse
import pprint


n_entries_to_print_default = 10


if __name__ == "__main__":
    app.disp_intro_string.main("Choose Starting Word")
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    
    parser = argparse.ArgumentParser(
        description=("Calculate the five letter words containing the "
        "most common letters with no repeats")
    )
    parser.add_argument(
        "-n", "--n_entries_to_print", 
        nargs="?", 
        const=n_entries_to_print_default, 
        default=n_entries_to_print_default, 
        type=int
    )
    args = parser.parse_args()

    start_word_dict = app.choose_start_word.main()
    start_word_list = list(start_word_dict)
    disp_dict = dict()
    for in_word in range(args.n_entries_to_print):
        disp_dict[start_word_list[in_word]] = \
            start_word_dict[start_word_list[in_word]]

    pp.pprint(disp_dict)
