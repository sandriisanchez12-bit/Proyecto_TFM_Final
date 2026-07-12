from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analizar_evento(evento):
    prompt = f"""
Eres un analista financiero experto.

Explica el impacto en bolsa del siguiente evento:

{evento}

Devuelve:
- Si el impacto es alcista, bajista o neutral.
- Una explicación breve.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
