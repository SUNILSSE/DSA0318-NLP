import openai

# Set up your OpenAI API key
openai.api_key = "mjjqq08NEIwHtyz6SRLa4CkbjzLmas9n"

def generate_text(prompt, max_tokens=100):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
    )
    return response.choices[0].text

# Test the function
prompt = "Write a short story about a character who discovers a hidden world."
print(generate_text(prompt))
