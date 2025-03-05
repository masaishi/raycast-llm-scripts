import subprocess
import webbrowser
from urllib.parse import quote

from .configs import default_browser, default_service_name
from .url_utils import format_prompt, get_service_url


def open_in_browser(url: str, browser: str) -> None:
    if browser == "any":
        webbrowser.open(url)
    else:
        subprocess.run(["open", "-a", browser, url])


def open_chat(
    prompt: str,
    service_name: str = default_service_name,
    browser: str = default_browser,
    is_formatted: bool = False,
) -> None:
    """
    Opens an AI chat service with the specified prompt.

    Args:
        prompt (str): The prompt template with format placeholders that will be replaced with sys.argv values
        service_name (str): The AI service to use: "chatgpt", "claude", or "perplexity"
        browser (str): The browser to use for opening the URL
                        - "any": Uses the default system browser
                        - Otherwise: Specifies the browser application name to use (e.g., "Google Chrome")
        is_formatted (bool): Whether the prompt is already formatted with sys.argv values
    """
    if not is_formatted:
        prompt = format_prompt(prompt)
    prompt = quote(prompt)
    url = get_service_url(prompt, service_name)
    print(url)
    open_in_browser(url, browser)


if __name__ == "__main__":
    import sys

    # Simple command-line interface for testing
    if len(sys.argv) < 2:
        print("Usage: python browser_launcher.py 'prompt' [service_name] [browser]")
        sys.exit(1)

    prompt = sys.argv[1]
    service = sys.argv[2] if len(sys.argv) > 2 else "chatgpt"
    browser_choice = sys.argv[3] if len(sys.argv) > 3 else "any"

    open_chat(prompt, service, browser_choice)
