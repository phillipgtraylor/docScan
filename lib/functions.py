from nis import match
import os

# colors to be used
colors = {"red": "\033[91m", "base": "\033[0m"}
# get .txt files path
def get_files_path(extension=".txt"):
    files_path = os.path.join(os.curdir, "words_directory")
    files_full_path = [
        os.path.join(files_path, f)
        for f in os.listdir(files_path)
        if f.endswith(extension)
    ]
    return files_full_path


# function to find user entry in files
def find_word_in_files(str_to_find):
    all_files = get_files_path()
    match_found = False
    for file in all_files:
        # trying to seperate print out with a space.
        # print("\n")
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                while True:
                    if str_to_find in line:
                        user_match_altered = line.replace(
                            str_to_find, f"{colors['red']}{str_to_find}{colors['base']}"
                        )

                        print(f"{file} : {user_match_altered}")

                        match_found = True
                        break
                    break
    return match_found
