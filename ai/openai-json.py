from typing import Annotated
from pydantic import BaseModel, Field
from openai import OpenAI

client = OpenAI()

class GenVibes(BaseModel):
    model_config = {
        "json_schema_extra": {
            "description": "A model that captures user vibes according to different generations."
        }
    }

    Boomer: Annotated[float, Field(
        description="How probably the user is a Boomer. [0, 1]"
    )]
    GenX: Annotated[float, Field(
        description="How probably the user is a Gen X. [0, 1]"
    )]
    Millennial: Annotated[float, Field(
        description="How probably the user is a Millennial. [0, 1]"
    )]
    GenZ: Annotated[float, Field(
        description="How probably the user is a Gen Z. [0, 1]"
    )]
    Alpha: Annotated[float, Field(
        description="How probably the user is a Alpha. [0, 1]"
    )]

print(GenVibes.model_json_schema(), "\n\n")

liked_music = input("Which music do you like?")

completion = client.beta.chat.completions.parse(
    model="gpt-4.1-nano",
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

response = completion.choices[0].message.parsed

# Parse into GenVibes model
vibes = GenVibes.model_validate(response)

# Print each field with its value
print("\nGeneration Vibes Analysis:")
print(f"Boomer: {vibes.Boomer:.2f}")
print(f"Gen X: {vibes.GenX:.2f}")
print(f"Millennial: {vibes.Millennial:.2f}")
print(f"Gen Z: {vibes.GenZ:.2f}")
print(f"Alpha: {vibes.Alpha:.2f}")

# Also print the JSON representation
print("\nJSON representation:")
print(vibes.model_dump_json(indent=2))
