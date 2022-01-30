import app.config_params as cfg
import app.disp_intro_string
import app.load_word_list
from app.wordle_player import WordlePlayer


if __name__ == "__main__":
    app.disp_intro_string.main("Run Wordle Game")
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )

    curr_player = WordlePlayer(
        word_list,
        f_auto_play=True,
        f_debug_puzzle=False,
        f_debug_console=False)
