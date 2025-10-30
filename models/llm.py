import os
from groq import Groq
from config.config import GROQ_API_KEY, DEFAULT_MODEL

def query_groq(prompt):
    """
    Queries Groq's free Mixtral-8x7b model for generating responses.
    """
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": "You are an AI career coach helping users with advice, resumes, and skill growth."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=512,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ Groq API error: {e}"
