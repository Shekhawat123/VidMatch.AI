Project: GemVision — Cross-modal Identity Detection with Gemini Pro
GemVision is a lightweight Python tool that uses Google's Gemini 2.5 Pro model to compare visual identity across media formats. It accepts both image and video inputs, analyzes their content, and determines if a person depicted in the image appears in the video — all via multimodal prompts powered by Google GenAI SDK.
🎯 Key Features
- Multimodal Input: Seamlessly combines image, video, and natural language in a single prompt.
- Real-time Streaming Output: Streams descriptive model responses chunk-by-chunk for better feedback control.
- Flexible Content Formatting: Works with types.Part.from_bytes() for direct media input.
- Tool Integration: Includes optional Google Search tool to enrich Gemini’s reasoning capability.
- Modular Design: Easily adaptable for batch processing, frame-level comparison, or embedding agents.
🧠 Ideal Use Cases
- Face verification across media files
- Surveillance or timestamp validation (can be extended)
- AI-assisted content tagging and classification
- Experimental agentic workflows using Gemini models
🚀 Quick Start
pip install google-genai
python finder.py


Ensure your media files and API key are correctly configured — see README.md for setup tips.

If you'd like, I can help generate the full README.md with badges, setup instructions, and licensing. Want to give it a cool tagline or prep it for public visibility? I’m your wingman. 🛫
