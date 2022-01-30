from distutils.log import debug
import app.config_params as cfg
from app.guess_validation import GuessInvalidNumLettersError, \
    GuessNonStringError, GuessStringInvalidCharactersError, \
    GuessNotInWordListError
import app.load_word_list
from app.wordle_puzzle import WordlePuzzle
import pytest


def test_valid_random_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    try:
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=False, 
            f_debug_console=False
        )
    except Exception as exc:
        assert False, "Something went wrong with the random init"


def test_valid_debug_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    try:
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word="TESTS", 
            f_debug_console=False
        )
    except Exception as exc:
        assert False, "Something went wrong with the random init"


def test_debug_word_too_many_letters_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    with pytest.raises(GuessInvalidNumLettersError):
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word="TESTING", 
            f_debug_console=False
        )


def test_debug_word_non_string_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    with pytest.raises(GuessNonStringError):
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word=123.456, 
            f_debug_console=False
        )


def test_debug_word_invalid_chars_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    with pytest.raises(GuessStringInvalidCharactersError):
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word="yelps", 
            f_debug_console=False
        )


def test_debug_word_invalid_chars_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    with pytest.raises(GuessStringInvalidCharactersError):
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word="yelp5", 
            f_debug_console=False
        )


def test_debug_word_not_in_list_init():
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    with pytest.raises(GuessNotInWordListError):
        curr_puzzle = WordlePuzzle(
            word_list, 
            f_use_debug_word=True,
            debug_word="XFIVE", 
            f_debug_console=False
        )
