#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Improve Prompt
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "paste your prompt here" }

# Optional parameters:
# @raycast.icon 💡
# @raycast.packageName LLM Tools

from utils import open_chat

prompt = """Please analyze and improve this prompt to make it more effective. Consider:
1. Clarity and precision
2. Structure and organization
3. Specific instructions or constraints
4. Examples or context needed
5. Potential ambiguities to resolve

Provide:
1. The improved version of the prompt
2. A brief explanation of the key improvements made
3. Any additional tips for getting better results

Original prompt:
{1}"""

open_chat(prompt, "ChatGPT")
