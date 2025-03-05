# 📘 Developer Guide

This guide provides detailed information about the utilities and how to write scripts for the Raycast LLM Scripts Template.

## 🔧 Utility Modules

The template provides several utility modules to simplify script creation and ensure consistent behavior:

### [browser_launcher.py](../scripts/utils/browser_launcher.py)

The core module for launching LLM services in your browser.

```python
from utils import open_chat

# Basic usage with defaults (ChatGPT in Google Chrome)
open_chat(prompt)

# Specify LLM service
open_chat(prompt, "claude")

# Specify both service and browser
open_chat(prompt, "perplexity", "Safari")
```

**Key Functions:**
- `open_chat(prompt, service_name="chatgpt", browser="Google Chrome")`: Main function to launch an LLM service
- Supports multiple browsers through the `browser` parameter:
  - `"any"`: Uses system default browser
  - Specific browser names: "Google Chrome", "Safari", "Firefox", etc.

### [url_utils.py](../scripts/utils/url_utils.py)

Handles prompt formatting and URL generation for different LLM services.

```python
# Prompt formatting example
prompt = """Translate this text to {1}:

{2}"""

# {1} and {2} will be replaced with Raycast arguments
# If your script has @raycast.argument1 and @raycast.argument2,
# {1} refers to argument1's value, {2} to argument2's value
```

**Key Features:**
- Automatic URL encoding of prompts
- Service-specific URL generation
- Raycast argument integration

### [configs.py](../scripts/utils/configs.py)

Central configuration for default settings.

```python
# Default settings (can be overridden in individual scripts)
default_service_name = "chatgpt"  # Options: "chatgpt", "claude", "perplexity"
default_browser = "Google Chrome"
```

## 📋 Raycast Script Metadata

For detailed information about Raycast script metadata and arguments, refer to these resources:

- [Raycast Script Commands Metadata Documentation](https://github.com/raycast/script-commands?tab=readme-ov-file#metadata)
- [Raycast Script Commands Arguments Documentation](https://github.com/raycast/script-commands/blob/master/documentation/ARGUMENTS.md)
