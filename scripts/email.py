#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Write Email
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "topic or context" }

# Optional parameters:
# @raycast.icon 📧
# @raycast.packageName Text Tools
# @raycast.description Write a professional email based on a topic or context

from utils import open_chat

prompt = """Please write a professional email based on the following topic or context:

{1}

The email should include:
1. An appropriate subject line
2. Professional greeting
3. Clear and concise body text
4. Appropriate closing
5. My name at the end

Make the tone professional but friendly, and keep it concise."""

open_chat(prompt, "Claude")
