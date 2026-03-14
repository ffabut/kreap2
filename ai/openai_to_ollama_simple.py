"""
Simple example showing how to use openai module to communicate with local LLM running on Ollama.

Před spuštěním skriptu je potřeba nastartovat stáhnout model a nastartovat Ollama.
1. Nainstalovat Ollama: https://ollama.com/download
2. V terminalu: `ollama run gemma3` - pripadne jiny model z https://ollama.com/search
3. Pokud model neni stazen, stahne jej
4. Az uvidime `>>> Send a message (/? for help)` znamena to, ze jsme pripraveny

V pristich runech staci jen spustit Ollamu, pripadne dat prikaz `ollama serve`.
"""

from openai import OpenAI

MODEL = "gemma3:4b" # `ollama ls` pro zobrazeni nainstalovanych LLM

client = OpenAI(
    base_url='http://localhost:11434/v1/', # port 11434 je defaultní
    api_key='ollama', # required but ignored
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model=MODEL,
)
print(chat_completion.choices[0].message.content)
