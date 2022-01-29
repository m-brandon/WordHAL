import app.analyze_letter_frequency
import app.config_params as cfg
import app.load_word_list as load_word_list


def check_repeat_letter(word_in):
    return len(list(word_in)) != len(set(list(word_in)))


def remove_words_with_repeats(list_in):
    list_out = []
    for currword in list_in:
        if not check_repeat_letter(currword):
            list_out.append(currword)

    return list_out


def get_word_scores(list_in, letter_freq_dict):
    scores_out = dict()
    for curr_word in list_in:
        word_score = 0
        for curr_letter in list(curr_word):
            word_score += letter_freq_dict[curr_letter.upper()]
        scores_out[curr_word] = round(word_score, 2)

    scores_out = dict(sorted(
        scores_out.items(), 
        key=lambda item: item[1], 
        reverse=True
    ))

    return scores_out


def main():
    word_list = load_word_list.main(cfg.filename_wordlist, cfg.ftype_wordlist)
    word_list_no_repeats = remove_words_with_repeats(word_list)
    scaled_letter_dict = app.analyze_letter_frequency.main()
    word_scores = get_word_scores(word_list_no_repeats, scaled_letter_dict)

    return word_scores
