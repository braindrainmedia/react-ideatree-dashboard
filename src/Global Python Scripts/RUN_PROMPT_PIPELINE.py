import os
import subprocess
import time

# Function to run a script and return its output
def run_script(script_path, input_text):
    result = subprocess.run(
        ['python3', script_path],
        input=input_text,
        text=True,
        capture_output=True,
    )
    return result.stdout


# Read the input text from the file
with open("IDEA.txt", "r") as file:
    input_text = file.read()

# Create the output directory if it doesn't exist
output_dir = "/Users/tre/Documents/Jeremi_Exp/GPT_Experiment/IdeaMap_Outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_time = time.time()

# Define the prompt script paths (change this to change Prompt Pipeline)
script_paths = [
    "Prompt_1_SumKey.py",
    "Prompt_3_Tone_Formatter.py",
    "Prompt_4_ConvertToAd.py",
    "Prompt_6_SWOT.py",
    "Prompt_7_ElevatorPitch.py",
    "Prompt_2_MetaData.py",
    "Prompt_8_SalesScript.py",
    "Prompt_9_CustomerProfiles.py",
    "Prompt_10_SocialMediaContent.py",
    "Prompt_11_PitchDeck.py",
    "Prompt_12_Slogans.py",
    "Prompt_13_Competitors.py",
    "Prompt_14_AltNames.py",
    "Prompt_15_ProductRoadmap.py",
    "Prompt_16_LongDesc.py",
    "Prompt_17_Targets.py",
    "Prompt_18_NewFeatures.py",
]

# Run the input text through each script and collect the results
results = []
for i, path in enumerate(script_paths):
    print(f"Running script {i + 1} of {len(script_paths)}: {path}")
    output = run_script(os.path.join("Prompt Functions", path), input_text)
    results.append(f"{os.path.splitext(path)[0]}:\n{output}\n-------------------------------------------------\n")

    # Save the output of each script to a file in the output directory
    output_file_path = os.path.join(output_dir, f"{os.path.splitext(path)[0]}.txt")
    with open(output_file_path, "w") as output_file:
        output_file.write(output)

# Run SingleSpacer.py
single_spacer_script = "SingleSpacer.py"
print(f"Running {single_spacer_script}")
run_script(single_spacer_script, "")

# Run prompt_EXPANDER.py
prompt_expander_script = "Prompt_EXPANDER.py"
print(f"Running {prompt_expander_script}")
run_script(os.path.join("Prompt Global Functions", prompt_expander_script), "")

# Save the results to a single output file
with open("IdeaMap.txt", "w") as file:
    file.write(input_text)
    file.write("\n".join(results))
    file.write("\n-------------------------------------------------\n")


# print the runtime in a nice format (hours, minutes, seconds)
end_time = time.time()
runtime = end_time - start_time
hours = runtime // 3600
minutes = (runtime % 3600) // 60
seconds = runtime % 60
print(f"Runtime: {hours:.0f}:{minutes:.0f}:{seconds:.0f}")

