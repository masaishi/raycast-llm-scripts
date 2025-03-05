#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Create LLM Script
# @raycast.shortcut cls
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "What should the script do? (e.g., 'translate text between languages')" }

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Developer Tools

from utils import open_chat

prompt = """Please create a Python script for Raycast that implements an LLM-based tool based on this prompt: {1}

The script should follow this format and style, similar to these examples:

Example 1 - Summarize Text:
```python
#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Summarize Text
# @raycast.mode silent
# @raycast.argument1 {{ "type": "text", "placeholder": "text to summarize" }}

# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName Text Tools

from utils import open_chat

prompt = \"\"\"Please provide a concise summary of the following text:

{{1}}

Please include:
1. Main points
2. Key takeaways
3. Important details\"\"\"

open_chat(prompt, "ChatGPT")
```

Example 2 - Grammar Check:
```python
#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Grammar Check
# @raycast.shortcut gc
# @raycast.mode silent
# @raycast.argument1 {{ "type": "text", "placeholder": "text to check" }}

# Optional parameters:
# @raycast.icon ✍️
# @raycast.packageName Text Tools

from utils import open_chat

prompt = \"\"\"Please check the following text for grammar, spelling, and style improvements.
Provide the corrected version and explain any changes made:

{{1}}\"\"\"

open_chat(prompt, "Claude", "Google Chrome")
```

Requirements:
1. Follow the exact same format as the examples above
2. Use appropriate Raycast parameters and comments
3. Use the utils.open_chat function
4. Create a clear and effective prompt template
5. Choose an appropriate icon emoji
6. Use "Text Tools" or "Developer Tools" for packageName based on functionality

Please provide the complete script ready to be saved and used in Raycast."""

open_chat(prompt, "Claude")
