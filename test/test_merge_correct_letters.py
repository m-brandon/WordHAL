import app.config_params as cfg
from app.wordle_player import merge_correct_letters


def test_no_prev_letters():
    prev_letters = [None]*cfg.num_letters
    new_letters = ["A"] * cfg.num_letters

    out_letters = merge_correct_letters(prev_letters, new_letters)

    assert out_letters == new_letters


def test_no_new_letters():
    prev_letters = ["A"] * cfg.num_letters
    new_letters = [None]*cfg.num_letters

    out_letters = merge_correct_letters(prev_letters, new_letters)

    assert out_letters == prev_letters


def test_same_old_and_new():
    prev_letters = ["A"] * cfg.num_letters
    new_letters = ["A"] * cfg.num_letters

    out_letters = merge_correct_letters(prev_letters, new_letters)

    assert out_letters == prev_letters


def test_some_unique_new():
    prev_letters = ["A", None, None, "D", None]
    new_letters = ["A", "B", None, None, "E"]

    out_letters = merge_correct_letters(prev_letters, new_letters)

    assert out_letters == ["A", "B", None, "D", "E"]
