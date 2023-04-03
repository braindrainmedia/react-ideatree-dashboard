import os
import sys
import openai

green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
magenta = "\033[35m"
red = "\033[31m"
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

folder_path = "/Users/tre/Documents/Jeremi_Exp/GPT_Experiment/IdeaMap_Outputs"

def generate_CompetitorList(information_file_path):
    with open(information_file_path, "r") as file:
        information = file.read().strip()

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please generate a highly detailed expansion on this information.  Follow the format of the info to make the new data blend in better.  If the info is in a numbered or bulleted list then add the new info as sub-bullet under the item it is expanding on.  Here's the info: {information}",
        temperature=0.9,
        max_tokens=3000,
        top_p=.1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def save_expansion(input_file_path):
    output_file_path = input_file_path.replace(".txt", "_EXP.txt")
    with open(output_file_path, "w") as file:
        expanded_text = generate_CompetitorList(input_file_path)
        file.write(expanded_text)

    print(magenta + f"Expansion saved to {output_file_path}" + "\033[0m")

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        save_expansion(file_path)
