import os
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

def generate_anthropic_text(prompt):
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=100,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    return message.content[0].text

# Example usage:
user_prompt = "Write a haiku about a sunrise."
generated_text = generate_anthropic_text(user_prompt)
print(generated_text)