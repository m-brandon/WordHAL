import config_params as cfg


def read_flat_text_file(filename_in):
    word_list = []
    with open(filename_in, "r") as fid_in:
        for currword in fid_in:
            word_list.append(currword.strip())

    return word_list


def main(filename_in, ftype_in):
    if ftype_in == "text":
        word_list = read_flat_text_file(filename_in)
    else:
        raise ValueError(f"File type not in known list, received: {ftype_in}")

    return word_list


if __name__ == "__main__":
    lst_words = main(cfg.filename_wordlist, cfg.ftype_wordlist)
    print(lst_words)
    print(f"Read {len(lst_words)} words")
