#!/usr/bin/env python3
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Perplexity Search
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "search query" }

# Optional parameters:
# @raycast.icon 🔍
# @raycast.packageName Perplexity Tools

from utils import open_chat

open_chat("{1}", "Perplexity")
