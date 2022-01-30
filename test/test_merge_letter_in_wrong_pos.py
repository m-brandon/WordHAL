import app.config_params as cfg
from app.wordle_player import merge_letter_in_wrong_pos


def test_no_prev_dict():
    prev_dict = dict()
    new_dict = {"A": [1], "B": [4]}

    dict_out = merge_letter_in_wrong_pos(prev_dict, new_dict)

    assert dict_out == new_dict


def test_no_new_dict():
    prev_dict = {"A": [1], "B": [4]}
    new_dict = dict()

    dict_out = merge_letter_in_wrong_pos(prev_dict, new_dict)

    assert dict_out == prev_dict


def test_no_letter_overlap():
    prev_dict = {"A": [1], "B": [4]}
    new_dict = {"C": [0], "D": [4]}

    dict_out = merge_letter_in_wrong_pos(prev_dict, new_dict)

    assert dict_out == {"A": [1], "B": [4], "C": [0], "D": [4]}


def test_letter_overlap():
    prev_dict = {"A": [1], "B": [4]}
    new_dict = {"A": [0], "D": [4]}

    dict_out = merge_letter_in_wrong_pos(prev_dict, new_dict)

    assert dict_out == {"A": [0, 1], "B": [4], "D": [4]}
