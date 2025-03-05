import sys


def format_prompt(prompt: str) -> str:
    """
    Formats a prompt template by replacing placeholders with command line arguments.

    Note: This function uses sys.argv directly to match Raycast's argument indexing.
    Raycast's # @raycast.argument starts with 1, so the format indices in the prompt
    should match the argument numbers used in the Raycast script.

    Example:
        With prompt = "Translate {1} to {2}"
        Raycast: Translate {1} {2}

    Args:
        prompt (str): The prompt template with format placeholders

    Returns:
        str: The formatted prompt with placeholders replaced by command line arguments
    """
    f_prompt = prompt.format(*sys.argv)
    return f_prompt


def get_service_url(formatted_prompt: str, service_name: str = "chatgpt") -> str:
    """
    Generates the appropriate URL for the specified AI chat service.

    Args:
        formatted_prompt (str): The formatted prompt to send to the AI service
        service_name (str): The AI service to use: "chatgpt", "claude", or "perplexity"

    Returns:
        str: The URL to open in a browser
    """
    if service_name.lower() == "perplexity":
        return f"https://www.perplexity.ai/search?q={formatted_prompt}"
    elif service_name.lower() == "claude":
        return f"https://claude.ai/new?q={formatted_prompt}"
    else:  # Default to ChatGPT
        return f"https://chatgpt.com/?q={formatted_prompt}"
