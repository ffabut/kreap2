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
- LiteLLM (https://github.com/BerriAI/litellm) - open source, je možné si hostovat vlastní instance
- OpenRouter (https://openrouter.ai/) - komerční služba

### LLM observability platform
Při používání AI je často potřeba ladit prompty.
Pokud vložíme prompt přímo do kódu, můžeme jej aktualizovat až při dalším release aplikace.
Možností, jak mít nad prompty kontrolu v reálném čase je použití LLM observability platform.
Aplikace se poté vždy dotazuje na platformu pro aktuální prompt, a s tím se až později volá LLM.
Například:
- Arize Phoenix (https://github.com/ArizeAI/phoenix) - open source, umožňuje také monitoring promptů - vhodné pro ladění







