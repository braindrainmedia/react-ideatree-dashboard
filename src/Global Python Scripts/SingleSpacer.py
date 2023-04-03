import re
import os

green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
magenta = "\033[35m"
red = "\033[31m"
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

folder_path = "/Users/tre/Documents/Jeremi_Exp/GPT_Experiment/IdeaMap_Outputs"

def single_space_file(file_path):
    with open(file_path, "r") as file:
        text = file.read().strip()

    single_spaced_text = re.sub(r'\n\s*\n', '\n', text)

    with open(file_path, "w") as file:
        file.write(single_spaced_text)

    print(" ")
    print(blue + "Single Spaced |" + "\033[0m", file_name)

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        single_space_file(file_path)

print(" ")