import app.config_params as cfg
from app.guess_validation import GuessInvalidNumLettersError, \
    GuessNonStringError, GuessStringInvalidCharactersError, \
    GuessNotInWordListError
import app.load_word_list
import pytest
from app.wordle_puzzle import WordlePuzzle


def initialize_random_puzzle():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    return WordlePuzzle(
        word_list, 
        f_use_debug_word=False, 
        f_debug_console=False
    )


def initialize_fixed_puzzle(solution_in):
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    return WordlePuzzle(
        word_list, 
        f_use_debug_word=True,
        debug_word=solution_in, 
        f_debug_console=False
    )


def test_evalute_guess_valid_input():
    curr_puzzle = initialize_random_puzzle()
    curr_guess = "HELLO"

    try:
        curr_puzzle.evaluate_guess(curr_guess)
    except Exception as exc:
        assert False, f"Input of '{curr_guess}' produced exception {exc}"


def test_evalute_improper_num_chars_input():
    curr_puzzle = initialize_random_puzzle()
    curr_guess = "HELLOTHERE"

    with pytest.raises(GuessInvalidNumLettersError):
        curr_puzzle.evaluate_guess(curr_guess)


def test_evalute_improper_input_type():
    curr_puzzle = initialize_random_puzzle()
    curr_guess = 101

    with pytest.raises(GuessNonStringError):
        curr_puzzle.evaluate_guess(curr_guess)


def test_evalute_improper_char_input():
    curr_puzzle = initialize_random_puzzle()
    curr_guess = "HELL0"

    with pytest.raises(GuessStringInvalidCharactersError):
        curr_puzzle.evaluate_guess(curr_guess)


def test_evalute_word_not_in_list():
    curr_puzzle = initialize_random_puzzle()
    curr_guess = "HELLX"

    with pytest.raises(GuessNotInWordListError):
        curr_puzzle.evaluate_guess(curr_guess)


def test_perfect_guess():
    curr_solution = "HELLO"
    curr_guess = "HELLO"
    curr_puzzle = initialize_fixed_puzzle(curr_solution)

    correct_letters, incorrect_letters, letters_wrong_pos = \
        curr_puzzle.evaluate_guess(curr_guess)

    assert correct_letters == ["H", "E", "L", "L", "O"]
    assert not incorrect_letters
    assert not letters_wrong_pos


def test_guess_with_mixed_result_1():
    curr_solution = "HELLO"
    curr_guess = "YELPS"
    curr_puzzle = initialize_fixed_puzzle(curr_solution)

    correct_letters, incorrect_letters, letters_wrong_pos = \
        curr_puzzle.evaluate_guess(curr_guess)

    assert correct_letters == [None, "E", "L", None, None]
    assert set(incorrect_letters) == set(["Y", "P", "S"])
    assert not letters_wrong_pos


def test_guess_with_mixed_result_2():
    curr_solution = "RAISE"
    curr_guess = "ARISE"
    curr_puzzle = initialize_fixed_puzzle(curr_solution)

    correct_letters, incorrect_letters, letters_wrong_pos = \
        curr_puzzle.evaluate_guess(curr_guess)

    assert correct_letters == [None, None, "I", "S", "E"]
    assert not incorrect_letters
    assert letters_wrong_pos == {"A": [0], "R": [1]}
