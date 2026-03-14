# Artificial Intelligence

Tento dokument je zatím hodně orientovaná spíše na textové LLM.

## API knihovny

Většina poskytovatelů LLM má jejich programatické (API) rozhraní kompatibilní s modulem "openai", který se stal faktickým standardem.
- OpenAI (https://github.com/openai/openai-python)

Volba té které knihovny je tedy odvislá od toho, čí služby chceme používat (často z důvodu ceny), respektive jaký model chceme použít.

Mezi nejpopulárnější patří:

- Anthropic (https://github.com/anthropics/anthropic-sdk-python)
- Gemini (https://github.com/googleapis/python-genai)
- Deepseek (primo kompatibilní s openai knihovnou)
- Qwen (primo kompatibilní s openai knihovnou)
- Ollama (https://github.com/ollama/ollama-python) - přímá komunikaci s lokálními open-source LLM skrze program Ollama
- (( Groq (https://github.com/groq/groq-python-sdk) # pozor Muskuv fasismus! ))

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

Klíč poté nastavujeme jako [proměnnou prostředí](https://en.wikipedia.org/wiki/Environment_variable):
```bash
export OPENAI_API_KEY="sk-abcd..."
```

případně pouze pro jednotlivé volání pythonu:
```bash
OPENAI_API_KEY="sk-abcd..." python main.py
```

#### Doporučení

1. Nepřidávejme API klíče do kódu - stačí pak zapomenout, dát push do našeho public repozitáře a nějaký scrapper si je vytáhne.
2. Pokud používáme [.env file a dotenv modul](https://github.com/theskumar/python-dotenv), což je asi nejvíce safe možnost, tak musíme dát .env do .gitignore.
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

completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "user",
            # v content posilame nejen text, ale i obrazek
            "content": [
                {
                    "type": "text",
                    "text": "You see a picture of conceptual artwork. What is it about?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{b64_image}"
                        # nebo taky muzeme poslat public URL
                        # "url": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)
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

Pydantic je knihovna pro validaci a serializaci dat.
Kromě jiného umožňuje také generovat dokumentaci a JSON schema z datových struktur.

Prvně musíme nainstalovat knihovnu:
```bash
pip install pydantic
```

A pak už můžeme použít:

```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class GenVibes(BaseModel):
    Boomers: str
    GenX: str
    Millennials: str
    GenZ: str

liked_music = input("Which music do you like?")

completion = client.beta.chat.completions.parse(
    model="gpt-4.5-nano",
    messages=[
        {
            "role": "system",
            "content": "You are a funny musical psychologist. Based on the user's answer, you return their analysis in JSON format."},
        {
            "role": "user",
            "content": liked_music},
    ],
    response_format=GenVibes,
)

event = completion.choices[0].message.parsed
```


## Ollama API

Ollama je program pro lokální spouštění LLM, který je velmi uživatelsky přátelský - instaluje se jako běžný program a nabízí GUI pro chat i instalaci modelů.
Stáhnout Ollamu pro Windows, MacOS i Linux můžeme z: https://ollama.com/download.

Jakmile mame nainstalovano, muzeme pokracovat s:
1. V terminalu zadame prikaz: `ollama run gemma3` - pripadne jiny model z https://ollama.com/search
2. Pokud model neni stazen, model se zacne stahovat,
3. Pote uvidime `>>> Send a message (/? for help)` a muzeme zacit chatovat.

Ollama nabizi vlastni knihovnu https://github.com/ollama/ollama-python, ktera umoznuje primo z Pythonu [listovat dostupne modely, pullovat nove, pushovat, atd](https://github.com/ollama/ollama-python?tab=readme-ov-file#api).
Soucasne s tim ale Ollama podporuje take openai API, takze muzeme vyuzivat nam uz znamy openai module - na toto pouziti se zamerime, protoze nase skripty pak budou univerzalnejsi.
Snaze se nam bude prepinat mezi Ollama, OpenAI, DeepSeek a jinymi poskytovateli.
Pokud to jde, je lepsi pouzivat univerzalnejsi reseni nez ta limitovana na jeden use case.

### Hello Ollama

Oproti beznemu vyuziti openai knihovny je potreba pri vytvareni clienta specifikovat base_url - vetsinou 'http://localhost:11434/v1/', naopak client_key nemusime resit, staci pouzit jakykoliv neprazdny retezec.
Musime take pouzit model, ktery mame lokalne dostupny - tedy pokud migrujeme z openAI nebo DeepSeek, musime ve volanich client.chat.completions.create() zmenit parametr model.

Jednoduchy priklad najdete v souboru: [openai_to_ollama_simple.py](openai_to_ollama_simple.py).

## Credits

Autor serigrafie v souboru `image.png` je Joseph Wilson, [dílo bylo zveřejněno](https://www.europeana.eu/en/item/91619/SMVK_EM_objekt_1090129) Etnografiska museet pod licencí CC BY.
