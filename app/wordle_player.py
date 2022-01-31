import app.analyze_letter_frequency
import app.config_params as cfg
from app.wordle_puzzle import WordlePuzzle
from random import randint


def merge_correct_letters(prev_correct_letters, new_correct_letters):
    correct_letters_out = prev_correct_letters.copy()

    for in_letter in range(len(prev_correct_letters)):
        if not prev_correct_letters[in_letter]:
            if new_correct_letters[in_letter]:
                correct_letters_out[in_letter] = \
                    new_correct_letters[in_letter]

    return correct_letters_out


def merge_letter_in_wrong_pos(prev_dict, new_dict):
    dict_out = prev_dict.copy()

    for currkey in new_dict:
        if currkey in dict_out:
            dict_out[currkey].extend(
                new_dict[currkey]
            )                    
            dict_out[currkey] = \
                list(set(dict_out[currkey]))
        else:
            dict_out[currkey] = new_dict[currkey]

    return dict_out


def check_candidate_for_correct_letters(correct_letters, candidate_word):
    f_word_passes = True
    for in_letter in range(cfg.num_letters):
        if correct_letters[in_letter]:
            if candidate_word[in_letter] != correct_letters[in_letter]:
                f_word_passes = False
                break

    return f_word_passes


def check_candidate_for_incorrect_letters(incorrect_letters, candidate_word):
    f_word_passes = True
    for in_letter in range(cfg.num_letters):
        if candidate_word[in_letter] in incorrect_letters:
            f_word_passes = False
            break

    return f_word_passes


def check_candidate_for_wrongpos_letters(letters_wrongpos, candidate_word):
    f_word_passes = True
    for currkey in letters_wrongpos:
        if not currkey in candidate_word:
            f_word_passes = False
            break
        else:
            for in_pos in letters_wrongpos[currkey]:
                if candidate_word[in_pos] == currkey:
                    f_word_passes = False
                    break

    return f_word_passes


def select_word_by_letter_freq(word_list_in, letter_freq):
    curr_max_score = 0
    curr_best_word = ""

    for curr_word in word_list_in:
        curr_score = sum([letter_freq[x] for x in curr_word])
        if curr_score > curr_max_score:
            curr_max_score = curr_score
            curr_best_word = curr_word
    
    if not curr_best_word:
        raise ValueError("Didn't select a new word")

    return curr_best_word


def select_random_word(word_list_in):
    in_rand_guess = randint(0, len(word_list_in)-1)
    return word_list_in[in_rand_guess]


class WordlePlayer:
    def __init__(
        self,
        word_list, 
        f_debug_puzzle=False, 
        debug_solution="", 
        f_debug_console=False
    ):
        self.word_list = word_list
        self.letter_frequency = app.analyze_letter_frequency.main()
        self.f_debug_console = f_debug_console

        if f_debug_puzzle:
            self.curr_puzzle = WordlePuzzle(
                self.word_list,
                f_use_debug_word=True,
                debug_word=debug_solution,
                f_debug_console=False
            )
        else:
            self.curr_puzzle = WordlePuzzle(
                self.word_list,
                f_use_debug_word=False,
                f_debug_console=self.f_debug_console
            )

        self.history = []
        self.guesses = 0

        self.correct_letters = [None] * cfg.num_letters
        self.incorrect_letters = []
        self.letters_in_wrong_pos = dict()

    def auto_play(self):
        while self.guesses < cfg.max_num_guesses:
            curr_guess = self.select_new_guess()
            self.execute_guess(curr_guess)
            if all(self.correct_letters):
                break
            if self.f_debug_console:
                print("-"*20)
                print(f"GUESS NUMBER {self.guesses}")
                print(f"Current Guess: {curr_guess}")
                self.curr_puzzle.display_solution()
                print(f"Correct Letters: {self.correct_letters}")
                print(f"Incorrect Letters: {self.incorrect_letters}")
                print(f"Letters in Wrong Position: {self.letters_in_wrong_pos}")
                print("-"*20)

        if all(self.correct_letters):
            f_success = True
            num_turns = self.guesses
        else:
            f_success = False
            num_turns = 0

        return f_success, num_turns

    def execute_guess(self, curr_guess):
        self.guesses += 1
        correct_letters, incorrect_letters, letters_wrong_pos = \
            self.curr_puzzle.evaluate_guess(curr_guess)

        if any(correct_letters):
            self.correct_letters = merge_correct_letters(
                self.correct_letters, 
                correct_letters
            )

        if incorrect_letters:
            self.incorrect_letters.extend(incorrect_letters)
            self.incorrect_letters = list(set(self.incorrect_letters))

        if letters_wrong_pos:
            self.letters_in_wrong_pos = merge_letter_in_wrong_pos(
                self.letters_in_wrong_pos, 
                letters_wrong_pos
            )

    def select_new_guess(self):
        candidate_word_list = []

        for curr_word in self.word_list:
            f_correct_pass = check_candidate_for_correct_letters(
                self.correct_letters, 
                curr_word
            )

            f_incorrect_pass = check_candidate_for_incorrect_letters(
                self.incorrect_letters, 
                curr_word
            )
            
            f_wrong_pos_pass = check_candidate_for_wrongpos_letters(
                self.letters_in_wrong_pos, 
                curr_word
            )

            if f_correct_pass and f_incorrect_pass and f_wrong_pos_pass:
                candidate_word_list.append(curr_word)

        if not candidate_word_list:
            raise ValueError("Failed to find matching word")

        new_guess = select_random_word(
            candidate_word_list
        )

        return new_guess
