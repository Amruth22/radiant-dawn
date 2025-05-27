import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
  )
  return response.choices[0].text.strip()

# Example usage:
user_prompt = "Write a short story about a robot learning to love:"

generated_text = generate_text(user_prompt)
print(generated_text)