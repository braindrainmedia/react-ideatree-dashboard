import os
import sys
import openai

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

# Read input data from stdin
dirty_data = sys.stdin.read().strip()

# Define the prompt
prompt_clean = f"""
Please convert the following data sample to the format suitable for the schema,
correct the format and fill the gaps with the correct values, where possible,mark invalid rows with the "invalid" flag.:

{dirty_data}

The schema is as follows: 
first_name: string, first letter capitalized, required
last_name: string, first letter capitalized, required
email: string, plain email format (foo@bar.com), required
gender: string, M or F, required
date_of_birth: string, YYYY-MM-DD, optional

email,first_name,last_name,gender,date_of_birth,invalid
"""

def gen_clean_data(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = prompt_clean,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main(input_text):
    clean_data = gen_clean_data(input_text)
    result = f"Cleaned Data:\n{clean_data}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
