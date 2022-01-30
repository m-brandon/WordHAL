from inspect import currentframe
import app.config_params as cfg
import app.guess_validation
from random import randint


class WordlePuzzle:
    def __init__(
        self, 
        word_list, 
        f_use_debug_word=False, 
        debug_word="", 
        f_debug_console=False
    ):
        self.word_list = word_list
        if f_use_debug_word:
            app.guess_validation.main(debug_word, self.word_list)
            self.solution = debug_word
        else:
            num_words_in_list = len(self.word_list)
            self.solution = \
                self.word_list[randint(0, num_words_in_list-1)].upper()
        
        self.f_debug_console = f_debug_console
        if self.f_debug_console:
            print(f"Initializing puzzle with solution: {self.solution}")

    def evaluate_guess(self, curr_guess):
        if self.f_debug_console:
            print("-"*20)
            print(f"Current solution is:  {self.solution}")
            print(f"Current guess is:  {curr_guess}")
        app.guess_validation.main(curr_guess, self.word_list)
        if self.f_debug_console:
            print("Passed validation")

        correct_letters = [None] * cfg.num_letters
        incorrect_letters = []
        letters_wrong_pos = dict()
        for in_letter, curr_letter in enumerate(curr_guess):
            if curr_letter in self.solution:
                if self.f_debug_console:
                    print(
                        f"Letter {curr_letter} was found in solution "
                        f"{self.solution}"
                    )
                if self.solution[in_letter] == curr_letter:
                    correct_letters[in_letter] = curr_letter
                    if self.f_debug_console:
                        print(f"The letter was in the correct position")
                else:
                    if curr_letter in letters_wrong_pos:
                        letters_wrong_pos[curr_letter].append(in_letter)
                    else:
                        letters_wrong_pos[curr_letter] = [in_letter]
                    if self.f_debug_console:
                        print(f"The letter was not in the correct position")
            else:
                incorrect_letters.append(curr_letter)
                incorrect_letters = list(set(incorrect_letters)) 
                if self.f_debug_console:
                    print(
                        f"Letter {curr_letter} was not in the solution "
                        f"{self.solution}"
                    )

        if self.f_debug_console:
            print(f"Correct letters:  {correct_letters}")
            print(f"Incorrect letters:  {incorrect_letters}")
            print(f"Letters in wrong position:  {letters_wrong_pos}")

        return correct_letters, incorrect_letters, letters_wrong_pos  

    def display_solution(self):
        print(f"The puzzle's solution is:  {self.solution}")
