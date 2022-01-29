import app.analyze_letter_frequency
import app.disp_intro_string
import pprint


if __name__ == "__main__":
    app.disp_intro_string.main("Letter Frequency Analyzer")
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    scaled_letter_dict = app.analyze_letter_frequency.main()
    pp.pprint(scaled_letter_dict)
