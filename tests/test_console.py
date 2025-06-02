import importlib, io
from unittest.mock import patch
from utils.console import error
from rich.console import Console


def test_singleton():
    console_1 = importlib.import_module("utils.console").console
    console_2 = importlib.import_module("utils.console").console
    assert console_1 is console_2, "Console instances are not the same singleton instance."


def test_error():
    message_content = "Test message"
    title_content = "Test title"

    test_console_instance = Console(file=io.StringIO())

    with patch('utils.console.console', test_console_instance):
        error(message_content, title=title_content)

    captured_text = test_console_instance.file.getvalue()

    assert message_content in captured_text
    assert title_content in captured_text
