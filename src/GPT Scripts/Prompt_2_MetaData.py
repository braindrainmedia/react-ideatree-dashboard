import os
import sys
import openai

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

def generate_summary(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please do a smart extraction of key meta data on the following text and look for things like names, dates, titles, main points, locations, goals, etc.. Give 10 key points of meta data: {prompt}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main(input_text):
    meta_data = generate_summary(input_text)
    result = f"META_DATA:\n{meta_data}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
