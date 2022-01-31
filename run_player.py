import app.config_params as cfg
import app.disp_intro_string
import app.load_word_list
from app.wordle_player import WordlePlayer
from tqdm import tqdm


if __name__ == "__main__":
    app.disp_intro_string.main("Run Wordle Game")
    word_list = app.load_word_list.main(
        cfg.filename_wordlist, 
        cfg.ftype_wordlist
    )

    num_success = 0
    aggregate_turns = 0
    for in_test in tqdm(range(cfg.num_test_iterations)):
        curr_player = WordlePlayer(
            word_list,
            f_debug_puzzle=False,
            f_debug_console=False)
        f_success, num_turns = curr_player.auto_play()

        if f_success:
            num_success += 1
            aggregate_turns += num_turns

    print(
        f"Out of {cfg.num_test_iterations} games, won {num_success} and "
        f"took an average of {round(aggregate_turns/num_success, 2)} "
        f"turns per success"
    )