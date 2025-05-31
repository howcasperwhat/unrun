from InquirerPy import prompt
from utils.console import error
from utils.constant import REPORT
from typing import Union


def flatten(choices: Union[dict, list, str]) -> list:
    results = []
    if isinstance(choices, str):
        results.append(choices)

    if isinstance(choices, list):
        for value in choices:
            if isinstance(value, (dict, list)):
                results.extend(flatten(value))
            else:
                results.append(str(value))

    if isinstance(choices, dict):
        for value in choices.values():
            if isinstance(value, (dict, list)):
                results.extend(flatten(value))
            else:
                results.append(str(value))

    return results


def select(choices: Union[dict, list, str]) -> str:
    if isinstance(choices, str):
        return choices

    choices = flatten(choices)

    length = len(choices)
    if length == 0:
        error(f"Unexpected empty choices list.\n{REPORT}")
        return ""
    if length == 1:
        if isinstance(choices, dict):
            return list(choices.keys())[0]
        return choices[0]

    question = {
        "type": "list",
        "name": "choice",
        "message": "Ambiguous choices, please select one:",
        "choices": choices
    }
    return prompt([question])["choice"]
