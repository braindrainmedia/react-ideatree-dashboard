import openai
import random

green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
magenta = "\033[35m"
red = "\033[31m"
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"


# Set up OpenAI API key and model
openai.api_key = "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"
model_engine = "text-davinci-003" # Or another GPT model that you have access to

# Define list of debate topics
topics = ["Should schools have mandatory uniforms?",
          "Should animals be used for scientific experimentation?",
          "Should the voting age be lowered to 16?",
          "Should the death penalty be abolished?",
          "Should college be tuition-free?",
          "Should marijuana be legalized?",
          "Should social media be regulated?",
          "Should the government provide universal basic income?"]

# Select a topic at random
topic = random.choice(topics)

# Define prompts for Bot A and Bot B
prompt_a = f"Explain why you have a Pro stance on this {topic} for a debate."
prompt_b = f"Explain why you have a Anti stance on this {topic} for a debate."

# Generate initial responses for each bot
response_a = openai.Completion.create(
    engine=model_engine,
    prompt=prompt_a,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5
)

response_b = openai.Completion.create(
    engine=model_engine,
    prompt=prompt_b,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5
)

# Print initial responses
print("Bot_A: ")
print(green + response_a.choices[0].text + "\033[0m")
print(" ")
print(blue + response_b.choices[0].text + "\033[0m")
print("Bot_B: ")

# Continue the debate for 10 cycles
for i in range(10):
    # Generate response for Bot A
    prompt = f"Explain why you disagree with this argument: {response_b.choices[0].text}.  This is the topic being debated {topic}."
    response_a = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5
    )
    print(" ")
    print("Bot_A: ")
    print(green + response_a.choices[0].text + "\033[0m")
    print(" ")

    # Generate response for Bot B
    prompt = f"Explain why you disagree with this argument: {response_a.choices[0].text}.  This is the topic being debated {topic}."
    response_b = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5
    )
    print(" ")
    print("Bot_B: ")
    print(blue + response_b.choices[0].text + "\033[0m")
    print(" ")
