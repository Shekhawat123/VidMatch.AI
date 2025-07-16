# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types

def generate():
    client = genai.Client(
        api_key="AIzaSyDYxYfBJhOYXH23KdHXwbWCKv-DjBTR2l0",  # Consider loading this securely from env or file
    )

    model = "gemini-2.5-pro"

    # ✅ FIXED: Load image bytes correctly
    image_path = r"C:\VickyJD\Tools\imagedetection\video\girl.png"
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="image/png",  # Adjust if your image is jpeg
                    data=image_bytes,
                ),
                types.Part.from_text(text="describe this"),
            ],
        ),
    ]

    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()