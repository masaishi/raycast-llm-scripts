#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Summarize Text
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "text to summarize" }

# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName Text Tools


from utils import open_chat

prompt = """Please provide a concise summary of the following text:

{1}

Please include:
1. Main points
2. Key takeaways
3. Important details"""

open_chat(prompt, "ChatGPT")
