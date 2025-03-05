#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Code Review
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "paste your code here" }

# Optional parameters:
# @raycast.icon 👨‍💻
# @raycast.packageName Code Tools

from utils import open_chat

prompt = """Please review this code and provide:
1. Potential bugs or issues
2. Performance improvements
3. Best practices suggestions
4. Security concerns if any

Code to review:
{1}"""

open_chat(prompt, "Claude")
