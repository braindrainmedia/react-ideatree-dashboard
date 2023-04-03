import os
import sys
import openai

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

def generate_CompetitorList(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Come up with 10 alternate names for my business idea.  Feel free to be creative in naming.  Here's my business idea: {prompt}",
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
    Competitors = generate_CompetitorList(input_text)

    result = f"Alternate Names:\n{Competitors}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
