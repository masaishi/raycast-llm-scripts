#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Analyze Code
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "Analysis type (format/explain/refactor)", "optional": false }
# @raycast.argument2 { "type": "text", "placeholder": "File path", "optional": false }

# Optional parameters:
# @raycast.icon 🖥️
# @raycast.packageName Code Tools
# @raycast.description Format, explain, or refactor code by Claude

import re
import sys
from pathlib import Path

from utils import open_chat

# Get file path and make it absolute
analysis_type = sys.argv[1].lower()
file_path = Path(sys.argv[2]).resolve()

# Read file content
if not file_path.exists():
    print(f"File does not exist: {file_path}")
code = file_path.read_text()

# Simple prompt templates
prompt = f"""Please {analysis_type} the code in the file: {str(file_path)}
{code}
"""
# Regex to replace all \n with \\n
prompt = re.sub(r"\n", r"\\n", prompt)
print(prompt)
open_chat(prompt, "ChatGPT", "Google Chrome", is_formatted=True)
