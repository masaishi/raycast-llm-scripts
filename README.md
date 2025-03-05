# 🤖 Raycast LLM Scripts Repository

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

This repository is not a polished template but rather a collection of diverse and experimental Raycast scripts that integrate with popular LLMs (ChatGPT, Claude, and Perplexity) **without requiring API keys**. The scripts here are added organically as new ideas emerge, providing a playground for testing and evolving different use cases.

### ✨ Why This Repository?

- **Experimental Playground**: Expect a mix of ideas, from polished scripts to rough drafts.
- **No API Keys Required**: Scripts work directly with web interfaces, launching queries in the browser.
- **Quick Prototyping**: Ideal for trying out new ideas and building quick tools.
- **Freedom to Customize**: Feel free to modify, extend, or adapt the scripts to your specific needs.

## 📋 What to Expect

- **🛠️ Variety of Scripts**: The repository contains scripts for everything from summarizing text to generating creative prompts.
- **⚡ Quick Additions**: New scripts are added whenever inspiration strikes. This is a dynamic and ever-changing collection.
- **🎲 Unpredictable Content**: Unlike a structured template, you might find experimental or work-in-progress scripts here.

## 🚀 Getting Started

### Clone This Repository

1. Clone the repository directly:
```bash
git clone https://github.com/masaishi/raycast-llm-scripts.git
```

2. Install [Raycast](https://raycast.com/) if you haven't already.
3. Import the scripts in Raycast:
   - Open Raycast
   - Go to Extensions
   - Click the "+" button
   - Choose "Import Script Command"
   - Select scripts from your repository

## 📚 Example Scripts

```
> Summarize Text [Your long text here]
```
```
> Perplexity [Query]
```
```
> Improve Prompt [Prompt]
```

## 🛠️ Adding Your Own Scripts

### Quick Additions

Feel free to add your own scripts directly. There’s no strict format—just make sure the script works and is useful to you!

### Example Script Structure

```python
#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Your Script Title
# @raycast.argument1 { "type": "text", "placeholder": "your placeholder" }

# Optional parameters:
# @raycast.icon 🔍
# @raycast.packageName Category Name

from utils import open_chat

prompt = """Your prompt template here:

{1}"""

open_chat(prompt)
```

## 🤝 Contributing

Since this is not a curated template but a live repository of evolving ideas, contributions are very welcome. Submit a pull request if you have an interesting script to share. There are no formal contribution guidelines—just keep it clean and useful!

**Send your pull requests to: https://github.com/masaishi/raycast-llm-scripts**

## 📄 License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Raycast](https://raycast.com/) for the amazing launcher
- OpenAI, Anthropic, and Perplexity for their LLM services