import subprocess
import time

from .configs import wait_before_paste

# Dictionary mapping keys to their key codes
KEY_CODES = {
    # Function keys
    "f1": 122,
    "f2": 120,
    "f3": 99,
    "f4": 118,
    "f5": 96,
    "f6": 97,
    "f7": 98,
    "f8": 100,
    "f9": 101,
    "f10": 109,
    "f11": 103,
    "f12": 111,
    # Special keys
    "esc": 53,
    "tab": 48,
    "space": 49,
    "delete": 51,
    "return": 36,
    "enter": 76,
    "caps_lock": 57,
    # Arrow keys
    "left": 123,
    "right": 124,
    "up": 126,
    "down": 125,
    # Navigation keys
    "home": 115,
    "end": 119,
    "page_up": 116,
    "page_down": 121,
    # Modifier keys (left and right when applicable)
    "shift": 56,
    "right_shift": 60,
    "control": 59,
    "right_control": 62,
    "option": 58,
    "right_option": 61,
    "command": 55,
    # Letter keys
    "a": 0,
    "s": 1,
    "d": 2,
    "f": 3,
    "h": 4,
    "g": 5,
    "z": 6,
    "x": 7,
    "c": 8,
    "v": 9,
    "b": 11,
    "q": 12,
    "w": 13,
    "e": 14,
    "r": 15,
    "y": 16,
    "t": 17,
    "u": 32,
    "i": 34,
    "o": 31,
    "p": 35,
    "j": 38,
    "k": 40,
    "l": 37,
    "m": 46,
    "n": 45,
    # Number and symbol keys
    "1": 18,
    "2": 19,
    "3": 20,
    "4": 21,
    "5": 23,
    "6": 22,
    "7": 26,
    "8": 28,
    "9": 25,
    "0": 29,
    "`": 50,
    "[": 33,
    "]": 30,
    "\\": 42,
    ";": 41,
    "'": 39,
    "-": 27,
    "=": 24,
    ",": 43,
    ".": 47,
    "/": 44,
    # Numpad keys
    "numpad_0": 82,
    "numpad_1": 83,
    "numpad_2": 84,
    "numpad_3": 85,
    "numpad_4": 86,
    "numpad_5": 87,
    "numpad_6": 88,
    "numpad_7": 89,
    "numpad_8": 91,
    "numpad_9": 92,
    "numpad_decimal": 65,
    "numpad_multiply": 67,
    "numpad_plus": 69,
    "numpad_divide": 75,
    "numpad_minus": 78,
    "numpad_equals": 81,
    "numpad_clear": 71,
}

# Dictionary mapping modifier keys to their AppleScript names
MODIFIER_MAP = {
    "command": "command",
    "shift": "shift",
    "option": "option",
    "alt": "option",  # alias for option
    "control": "control",
    "ctrl": "control",  # alias for control
}


def copy_to_clipboard(text: str) -> None:
    """
    Copy text to clipboard.

    Args:
        text (str): Text to copy to clipboard
    """
    subprocess.run(["pbcopy"], input=text, text=True)


def get_clipboard_text() -> str:
    """
    Get text from clipboard.

    Returns:
        str: Text content of clipboard
    """
    return subprocess.run(["pbpaste"], capture_output=True, text=True).stdout


def press_keyboard_shortcut(key: str, modifiers: list | None = None) -> None:
    """
    Simulate keyboard shortcut press using either key code or keystroke.

    This function supports both special keys (via key codes) and regular characters (via keystroke).

    Args:
        key (str): Key to press (e.g., "v", "return", "up", "f5")
        modifiers (list, optional): List of modifiers (e.g., ["command", "shift"])
    """
    if modifiers is None:
        modifiers = []

    # Convert modifiers to AppleScript format
    modifier_list = [MODIFIER_MAP.get(mod.lower(), mod) for mod in modifiers]

    # Create the modifier string for AppleScript
    if modifier_list:
        if len(modifier_list) == 1:
            modifier_string = f" using {modifier_list[0]} down"
        else:
            modifier_string = (
                " using {" + ", ".join([f"{mod} down" for mod in modifier_list]) + "}"
            )
    else:
        modifier_string = ""

    # Check if key is a single character or in our key code dictionary
    key_lower = key.lower()

    if key_lower in KEY_CODES:
        # Use key code for special keys
        key_code = KEY_CODES[key_lower]
        applescript = (
            f'tell application "System Events" to key code {key_code}{modifier_string}'
        )
    else:
        # For regular characters, use keystroke
        # If it's a single character, we can use keystroke directly
        applescript = (
            f'tell application "System Events" to keystroke "{key}"{modifier_string}'
        )

    # Execute the AppleScript
    subprocess.run(["osascript", "-e", applescript])


def paste_from_clipboard() -> str:
    """
    Paste content from clipboard using Command+V.

    Returns:
        str: The text that was pasted
    """
    clipboard_text = get_clipboard_text()
    press_keyboard_shortcut("v", ["command"])
    return clipboard_text


def type_text(text: str) -> None:
    """
    Type text character by character using applescript.

    Args:
        text (str): Text to type
    """
    # Escape double quotes and backslashes in the text
    escaped_text = text.replace("\\", "\\\\").replace('"', '\\"')
    applescript = f'tell application "System Events" to keystroke "{escaped_text}"'
    subprocess.run(["osascript", "-e", applescript])


def press_key_combination(keys: list) -> None:
    """
    Press a combination of keys simultaneously.

    Args:
        keys (list): List of keys to press together
    """
    if not keys:
        return

    # The last key is the main key, the rest are modifiers
    main_key = keys[-1]
    modifiers = keys[:-1]

    press_keyboard_shortcut(main_key, modifiers)


def keyboard_flow(
    prompt: str, wait_before_paste: float = wait_before_paste, send_enter: bool = True
) -> str:
    """
    Execute a complete keyboard flow:
    1. Copy prompt to clipboard
    2. Wait specified time
    3. Paste from clipboard
    4. Optionally press Enter

    Args:
        prompt (str): Prompt to paste
        wait_before_paste (float): Seconds to wait before pasting
        send_enter (bool): Whether to press Enter after pasting

    Returns:
        str: The text that was pasted
    """
    # Copy prompt to clipboard
    copy_to_clipboard(prompt)

    # Wait before pasting
    time.sleep(wait_before_paste)

    # Paste from clipboard
    pasted_text = paste_from_clipboard()

    # Press Enter if requested
    if send_enter:
        press_keyboard_shortcut("return")

    return pasted_text
