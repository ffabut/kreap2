"""
How to use OpenAI API to analyze images.

1. We read the image file and encode it in base64 format.
2. We send user message with 2 parts - text and image.
3. The image is sent as a base64 string with a data:image/png;base64 URL prefix.
"""

import base64
from openai import OpenAI

client = OpenAI()

with open("image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You see a picture of conceptual artwork. What is it about?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{b64_image}"
                        # OR we can use a public URL
                        # "url": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)