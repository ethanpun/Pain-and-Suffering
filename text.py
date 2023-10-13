"""text.py

Module to help with formatting and displaying text, and prompting for text input
"""
from typing import Any


def prompt_valid_choice(
    options: list[str],
    cancel: bool = False,
    prompt: str = "Pick an option",
    errmsg: str = "Invalid option, try again.",
    prelude: str = "",
) -> str:
    if cancel:
        prompt += " (or 'b' to go back)"
    prompt += ": "
    if prelude:
        print(prelude)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print('')
    choice = input(prompt)
    while not (choice.isdecimal() and 1 <= int(choice) <= len(options)):
        print(errmsg)
        choice = input(prompt)
        if cancel and choice.lower() == 'b':
            return None
    print('')
    return choice

