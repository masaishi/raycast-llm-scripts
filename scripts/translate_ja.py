#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Translate to Japanese
# @raycast.shortcut trj
# @raycast.mode silent

# @raycast.argument1 { "type": "text", "placeholder": "text" }
# Optional parameters:
# @raycast.icon 🗾
# @raycast.packageName ChatGPT Tools

from utils import open_chat

prompt = "Translate the following to Japanese:\n\n{1}"

open_chat(prompt, "chatgpt", "Google Chrome")
