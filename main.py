from lib.functions import *
import sys

# path_test = get_files_path(extension=".txt")
# print(path_test)

while __name__ == "__main__":

    try:
        # def str_to_find var as user input made when executing main.py
        str_to_find = sys.argv[1]
        matched_pretty_line = find_word_in_files(str_to_find=str_to_find)
        # print(str_to_find)

        if matched_pretty_line == True:
            print(
                "Cases of user entry --",
                colors["red"],
                str_to_find,
                colors["base"],
                "-- found",
            )

        elif matched_pretty_line == False:
            print(
                "No cases of user entry --",
                colors["red"],
                str_to_find,
                colors["base"],
                "-- found",
            )

    # this exception will occur if the an  IndexError occurs, aka there is no index entry
    except IndexError:
        print("argument required \n" "Example: python main.py your_search_term_here")

    finally:
        break
