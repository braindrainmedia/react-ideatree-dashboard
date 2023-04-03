import os
import sys
import openai

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

def generate_SMContent(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a set of social media posts that promote this company's idea.  Here's the idea: {prompt}.",
        temperature=0.8,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()


def main(input_text):
    SM_Posts = generate_SMContent(input_text)

    result = f"Social Media Posts:\n{SM_Posts}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
