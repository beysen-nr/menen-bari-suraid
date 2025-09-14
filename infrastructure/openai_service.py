import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_gpt(messages: list, max_tokens: int = 200) -> str:
    """Send messages to GPT and return response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ GPT API Error:", e)
        return "⚠️ Sorry, I couldn’t reach GPT."
