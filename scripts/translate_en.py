#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Translate to English
# @raycast.shortcut tre
# @raycast.mode silent

# @raycast.argument1 { "type": "text", "placeholder": "text" }
# Optional parameters:
# @raycast.icon 🌐
# @raycast.packageName ChatGPT Tools

from utils import open_chat

prompt = "Translate the following to English:\n\n{1}"
open_chat(prompt, "ChatGPT", "Google Chrome")
