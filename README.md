# 🤖 Raycast LLM Scripts Template

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <img src="https://i.gyazo.com/253d6c561112b0840ed6179d4248e52a.gif" alt="Basic Usage Demo" width="100%"><br />
        <strong>Basic usage</strong>
      </td>
      <td align="center" width="50%">
        <img src="https://i.gyazo.com/2d900b4cf909059667bc423442626e28.gif" alt="Create New Script Demo" width="100%"><br />
        <strong>Create New Script</strong>
      </td>
    </tr>
  </table>
</div>

## 🌟 Overview

This repository provides a template for creating Raycast scripts that integrate with popular LLMs (ChatGPT, Claude, and Perplexity) **without requiring API keys**. Simply write Python scripts with prompt templates, and launch your favorite LLM in the browser with pre-filled prompts.

### ✨ Key Benefits

- **No API Keys Required**: Just opens the browser with your prompt as the query - no API credentials needed
- **Browser-Based**: Works with web interfaces you're already familiar with
- **Quick Access**: Launch saved prompts directly from Raycast
- **Fully Customizable**: Create and modify scripts to suit your specific needs

## 📋 Features

- **📚 Example Scripts**: Collection of practical scripts for common tasks
- **🎯 Script Generator**: Create new LLM scripts with a simple command
- **🔄 Multi-Service Support**: Seamlessly switch between ChatGPT, Claude, and Perplexity

## 🚀 Getting Started

### Use This Template

1. Click the "Use this template" button above
2. Name your repository
3. Clone your new repository:
```bash
git clone https://github.com/yourusername/raycast-llm-scripts.git
```

### Setup

![setup](https://i.gyazo.com/7daab3fcb350face8debe5f37f6dccb9.gif)

1. Install [Raycast](https://raycast.com/) if you haven't already
2. Import the scripts in Raycast:
   - Open Raycast
   - Go to Extensions
   - Click the "+" button
   - Choose "Import Script Command"
   - Select scripts from your repository

## 📚 Usage Examples

```
> Summarize Text [Your long text here]
```
```
> Perplexity [Query]
```
```
> Improve Prompt [Prompt]
```

## 🛠️ Creating Your Scripts

### Using the Script Generator

The fastest way to create new scripts:

1. Run the Create LLM Script command
    ```
    > Create LLM Script
    Script purpose: Create a script that translates text between languages
    ```
2. Describe what you want the script to do
3. Get a complete script with:
   - Raycast parameters
   - Prompt template
   - Proper formatting

### Manual Creation

Create scripts manually using this template:

```python
#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Your Script Title
# @raycast.argument1 { "type": "text", "placeholder": "your placeholder" }

# Optional parameters:
# @raycast.icon 🔍
# @raycast.packageName Category Name

from utils import open_chat  # Clean import from utils package

prompt = """Your prompt template here:

{1}"""

open_chat(prompt)  # Uses default_service_name from configs.py
# or specify service: open_chat(prompt, "claude")
# or specify both: open_chat(prompt, "perplexity", "Google Chrome")
```

## 📚 Developer Documentation

For detailed information about utilities and script writing guidelines, check out our [Developer Guide](docs/developer-guide.md).

## 🤝 Contributing

If you create useful scripts with this template, please consider contributing them back to the community! 

**Send your pull requests to: https://github.com/masaishi/raycast-llm-scripts**

Most contributions will be merged as long as they don't present ethical or security concerns. Your scripts can help others enhance their productivity with LLMs!

## 📄 License

This template is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Raycast](https://raycast.com/) for the amazing launcher
- OpenAI, Anthropic, and Perplexity for their LLM services
