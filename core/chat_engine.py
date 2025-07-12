import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get token and endpoint
token = os.getenv("GITHUB_TOKEN")  # Or change to GPT_API_KEY if you prefer
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

# Initialize OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Main response function
def get_bot_response(user_input: str, persona_prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": persona_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=1,
            top_p=1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[Error] {str(e)}")  # Optional logging
        return "⚠️ Oops, I couldn't fetch a response. Check your token or model access."
