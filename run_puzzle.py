import app.config_params as cfg
import app.disp_intro_string
import app.load_word_list
from app.wordle_puzzle import WordlePuzzle


if __name__ == "__main__":
    app.disp_intro_string.main("Puzzle Generator")
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )
    curr_puzzle = WordlePuzzle(word_list, f_debug_console=cfg.f_debug_console)

    curr_puzzle.evaluate_guess("HELLO")
    curr_puzzle.display_solution()
