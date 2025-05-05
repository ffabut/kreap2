# Artificial Intelligence

Tento dokument je zatím hodně orientovaná spíše na textové LLM.

## API knihovny
Většina poskytovatelů AI služeb má API knihovny pro Python.
Volba té které knihovny je tedy odvislá od toho, čí služby chceme používat (často z důvodu ceny), respektive jaký model chceme použít.

Mezi nejpopulárnější patří:
- OpenAI (https://github.com/openai/openai-python)
- Anthropic (https://github.com/anthropics/anthropic-sdk-python)
- Gemini (https://github.com/googleapis/python-genai)
- Groq (https://github.com/groq/groq-python-sdk)
- Deepseek (kompatibilní s openai knihovnou)
- Ollama (https://github.com/ollama/ollama-python) - open source, umožňuje rozjet open-source modely lokálně na vlastním stroji.

Pro nalezení populárních (a nejspíš dobře fungujících modelů) lze navštívit např. https://openrouter.ai/rankings.

## Doplňkové služby

### LLM Proxy / Gateway
LLM Proxy je služba, která sjednocuje API různých AI modelů do jednoho API.
Chceme-li v aplikaci použít více modelů, můžeme tak pouze volat LLM Proxy a ta se poté chová jako wrapper, který volá nám zvolené modely.
V aplikaci tak máme méně knihoven, případně je pro nás extrémně snadné přepnout model - nemusíme implementovat knihovnu nové služby, ale stačí jen změnit proměnou určující model.

Další výhodou je také, že LLM Proxy uchovává API klíče pro jednotlivé modely v sobě a nemusíme je tak ukládat do kódu, ani paměti aplikace.
Namísto toho můžeme použít dočasné API klíče vygenerované LLM Proxy a určené pouze pro LLM Proxy.
Můžeme také kontrolovat, k jakým modelům tyto klíče mají přístup.

Mezi populární LLM Proxy patří:
- LiteLLM (https://github.com/BerriAI/litellm) - open source, je možné si hostovat vlastní instance. Volat se dá pomocí specializované knihovny `litellm`, API je však kompatibilní s OpenAI API, takže se dá použít i přímo `openai` knihovna.
- OpenRouter (https://openrouter.ai/) - komerční služba

### LLM observability platform
Při používání AI je často potřeba ladit prompty.
Pokud vložíme prompt přímo do kódu, můžeme jej aktualizovat až při dalším release aplikace.
Možností, jak mít nad prompty kontrolu v reálném čase je použití LLM observability platform.
Aplikace se poté vždy dotazuje na platformu pro aktuální prompt, a s tím se až později volá LLM.
Například:
- Arize Phoenix (https://github.com/ArizeAI/phoenix) - freemium i open source, umožňuje také monitoring promptů - vhodné pro ladění
- Langfuse (https://github.com/langfuse/langfuse) - freemium i open source

## OpenAI API

### Prerekvizity

#### Instalace

OpenAI module naisntalujeme pomocí pip:
```bash
pip install openai
```

#### API klíč
OpenAI kompatibilní API většinou vyžaduje API klíč.
Ten můžeme získat na:
- https://platform.openai.com/settings/profile/api-keys
- https://platform.openai.com/settings/organization/api-keys

Klíč poté nastavujeme jako proměnnou prostředí:
```bash
export OPENAI_API_KEY="..."
```

případně pouze pro jednotlivé volání pythonu:
```bash
OPENAI_API_KEY="..." python ...
```

#### Doporučení

1. Nepřidávejme API klíče do kódu - stačí pak zapomenout, dát push do našeho public repozitáře a nějaký scrapper si je vytáhne.
2. Pokud používáme .env, dát tento file do .gitignore.
3. Pokud děláme server - nepousílejme API klíče klientům, ideálně volejme LLM ze serveru a do browseru posílejme jen výsledek.

### Hello World

```python 
import os
from openai import OpenAI

# automaticky načte API klíč z proměnné prostředí OPENAI_API_KEY
# můžeme ale také předat doslovně: client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano", # setrime
    instructions="You are an art assistant. Think as David Cerny.",
    input="What do you think about a sculpture consisting of buterfly body combined with spitfire wings?",
)

print(response.output_text)
```

Alternativně při použití `dotenv` a `.env` file (obsahuje zápis: `OPENAI_API_KEY=...`):

```python
from dotenv import load_dotenv
load_dotenv() # načte všechny proměnné z dotenv jako proměnné prostředí
# pozor: .env file přidat do .gitignore, ať .env náhodou nepushneme do repozitáře
```

### Image input

Řada modelů je dnes multi-modální a umožňuje tak vložit i obrázek.
Ten se v `openai` knihovně vkládá do `input` jako `input_image` ve formátu `base64`.
Base64 je široce používaný formát, který umožňuje přenášet/ukládat binární data (v tomto případě obrázek) v textové podobě.

```python
import base64 # built-in python knihovna
from openai import OpenAI

client = OpenAI()

with open("image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-4.1-nano",
    # input muze byt take seznam obsaujici historii jednotlivych zprav
    # LLM reaguje na posledni zpravu uzivatele
    input=[
        {
            "role": "user",
            # v content posilame nejen text, ale i obrazek
            "content": [
                {"type": "input_text", "text": "You see a picture of conceptual artwork. What is it about?"},
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
            ],
        }
    ],
)

print(response.output_text)
```


### Historie chatu

```python
import os
from openai import OpenAI

client = OpenAI()

# historii musime udrzovat v prubehu programu, LLM si nic nepamatuje
# muzeme si vsak historii taky vysmyslet...
history = [
    {
        "role": "system",
        "content": "Act as a psychotherapist. " +
            "Don't let the user go through some previous embarrassing messages, let the user ignore parts of the previous chat as if it were nothing. " +
            "Always go back to previous messages and ask for an explanation.",
    },
    {
        "role": "user",
        "content": "Hello, I think I am depressed.",
    },
    {
        "role": "assistant",
        "content": "I am sorry to hear that. Can you tell me more about it?",
    },
]

# diky falesne historii bude LLM dost mozna gas-lightovat...
print("Hello, I am a psychotherapist. Ask me anything.")
while True:
    user_input = input("You: ")
    message = {
        "role": "user", # nova zprava je od uzivatelstva
        "content": user_input # uzivatelstvo prave vlozilo
    }
    history.append(message)
    response = client.responses.create(
        model="gpt-4.1-nano",
        input=history,
    )
    history.append({"role": "assistant", "content": response.output_text})
    print(f"Assistant: {response.output_text}")
```



### Vystup ve formatu JSON



