from inspect import currentframe
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


class WordlePlayer:
    def __init__(
        self,
        word_list, 
        f_auto_play=False,
        f_debug_puzzle=False, 
        debug_solution="", 
        f_debug_console=False
    ):
        self.word_list = word_list
        self.f_auto_play = f_auto_play
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

        if self.f_auto_play:
            while self.guesses < cfg.max_num_guesses:
                curr_guess = self.select_new_guess()
                self.execute_guess(curr_guess)
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
                print("SUCCESS:  Word was correctly guessed")
            else:
                print("FAILURE:  Word was not correctly guessed")

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
        return self.word_list[randint(0, len(self.word_list)-1)].upper()
