from app.choose_start_word import check_repeat_letter


def test_no_repeats():
    assert check_repeat_letter("TEARS") == False


def test_repeat():
    assert check_repeat_letter("HELLO") == True
