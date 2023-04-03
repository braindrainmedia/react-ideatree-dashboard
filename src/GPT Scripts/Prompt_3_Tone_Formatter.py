import os
import sys
import openai
import random

# Set up the OpenAI API client
api_key = "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"
openai.api_key = api_key

tones = ["Professor", "Evil Villian", "Silly Girlfriend", "British King", "Little Kid", "Angry Pastor", "Comedian"]

def generate_tone(prompt):
    tone = random.choice(tones)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please rewrite the following text in the tone of {tone} so that the text will have the new tone applied throughout: {prompt}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip(), tone

def main(input_text):
    formatted_text, tone = generate_tone(input_text)
    result = f"* New text in {tone} Tone *\nText with New Tone:\n{formatted_text}\n"
    return result

if __name__ == "__main__":
    input_text = sys.stdin.read()
    output = main(input_text)
    sys.stdout.write(output)
