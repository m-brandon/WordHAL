import app.config_params as cfg


class GuessInvalidNumLettersError(Exception):
    """Exception raised when the number of letters in the guess is invalid"""
    def __init__(self, message=f"Number of letters must be {cfg.num_letters}"):
        self.message = message
        super().__init__(self.message)


class GuessNonStringError(Exception):
    """Exception raised when the number of letters in the guess is invalid"""
    def __init__(self, message=f"Guess must be a string"):
        self.message = message
        super().__init__(self.message)


class GuessStringInvalidCharactersError(Exception):
    """"Exception raised if characters in the guess are not in the range A-Z"""
    def __init__(self, message=f"Characters must be in range A-Z"):
        self.message = message
        super().__init__(self.message)


class GuessNotInWordListError(Exception):
    """"Exception raised if characters in the guess are not in the range A-Z"""
    def __init__(self, message=f"Guess must be in word list"):
        self.message = message
        super().__init__(self.message)


def main(current_guess, word_list):
    if not isinstance(current_guess, str):
        raise GuessNonStringError()
    if len(current_guess) != cfg.num_letters:
        raise GuessInvalidNumLettersError()
    for curr_letter in current_guess:
        if not (ord(curr_letter) in range(ord("A"), ord("Z")+1)):
            raise GuessStringInvalidCharactersError()
    if not (current_guess in word_list):
        raise GuessNotInWordListError()
