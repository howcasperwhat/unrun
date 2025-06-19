import importlib, io
from unittest.mock import patch
from unrun.utils.console import template
from rich.console import Console


def test_singleton():
    console_1 = importlib.import_module("unrun.utils.console").console
    console_2 = importlib.import_module("unrun.utils.console").console
    assert console_1 is console_2, "Console instances are not the same singleton instance."


def test_template():
    message_content = "Test message"
    title_content = "Test title"

    test_console_instance = Console(file=io.StringIO())

    with patch('unrun.utils.console.console', test_console_instance):
        template(message_content, title=title_content, color="blue")

    captured_text = test_console_instance.file.getvalue()

    assert message_content in captured_text
    assert title_content in captured_text
