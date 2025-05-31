from unittest import TestCase, main
from yaml import safe_load
from unrun.cli import parse_command, parse_filename
from os import environ


class TestUnrun(TestCase):
    def setUp(self):
        self.file = "unrun.yaml"
        with open(self.file, 'r') as f:
            self.scripts = safe_load(f)

    def test_parse_command_None(self):
        key = 'nonexistent_key'
        command = parse_command(key, "", self.scripts)
        self.assertIsNone(command)

    def test_parse_command_single(self):
        key = "hello"
        command = parse_command(key, "", self.scripts)
        self.assertEqual(command, "echo \"Hello, world!\"")

    def test_parse_command_nesting(self):
        key = "foo.bar"
        command = parse_command(key, "", self.scripts)
        self.assertEqual(command, "echo \"This is foo bar\"")

    def test_parse_command_list(self):
        key = "baz"
        command = parse_command(key, "", self.scripts)
        self.assertEqual(command, "echo \"This is baz item 1\" && echo \"This is baz item 2\"")

    def test_parse_filename_default(self):
        filename = parse_filename(None)
        self.assertEqual(filename, "unrun.yaml")

    def test_parse_filename_env(self):
        environ["UNRUN_FILE"] = "test.yaml"
        filename = parse_filename(None)
        self.assertEqual(filename, "test.yaml")
        del environ["UNRUN_FILE"]


if __name__ == '__main__':
    main()
