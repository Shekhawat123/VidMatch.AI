# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types

def generate():
    # Load API key from environment securely
    api_key = "AIzaSyDYxYfBJhOYXH23KdHXwbWCKv-DjBTR2l0"
    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-pro"

    # ✅ Read video bytes correctly
    video_path = r"C:\VickyJD\Tools\imagedetection\video\dubai.mp4"
    with open(video_path, "rb") as vid_file:
        video_bytes = vid_file.read()

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="video/mp4",
                    data=video_bytes,
                ),
                types.Part.from_text(text="describe this video"),
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