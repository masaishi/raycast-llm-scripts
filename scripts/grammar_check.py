#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Grammar Check
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "text to check" }

# Optional parameters:
# @raycast.icon ✍️
# @raycast.packageName Text Tools

from utils import open_chat

prompt = """Please check the following text for grammar, spelling, and style improvements. 
Provide the corrected version and explain any changes made:

{1}"""

open_chat(prompt, "ChatGPT")
