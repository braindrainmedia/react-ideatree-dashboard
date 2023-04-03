import os
import sys
import openai

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

def generate_summary(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please do a logline summary on the following text into 2 sentences or fewer: {prompt}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def generate_keywords(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please extract 20 keywords from the prompt: {prompt}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=.8,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main(input_text):
    summary = generate_summary(input_text)
    keywords = generate_keywords(summary)

    result = f"\nSummary:\n{summary}\n\nKeywords:\n{keywords}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
