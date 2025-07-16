# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types

def generate():
    # 🔐 Hardcoded API key for testing (secure this later!)
    client = genai.Client(
        api_key="AIzaSyDYxYfBJhOYXH23KdHXwbWCKv-DjBTR2l0",
    )

    model = "gemini-2.5-pro"

    # ✅ Load image bytes correctly
    image_path = r"C:\VickyJD\Tools\imagedetection\video\girl.png"
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    # ✅ Load video bytes correctly
    video_path = r"C:\VickyJD\Tools\imagedetection\video\dubai.mp4"
    with open(video_path, "rb") as vid_file:
        video_bytes = vid_file.read()

    # 🧠 Multimodal prompt combining video and image with question
    contents = [
        types.Content(
                    role="user",
                    parts=[
                        types.Part.from_bytes(
                            mime_type="video/mp4",
                            data=video_bytes,
                        )
                    ],
                ),

        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="image/jpeg",  # or "image/png" if needed
                    data=image_bytes,
                ),
                types.Part.from_text(
                    text="Is this person present anywhere in the video?"
                ),
            ],
        ),
    ]

    # 🛠️ Optional tools like Google Search if model wants external info
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

    # 🪄 Streaming the response
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()