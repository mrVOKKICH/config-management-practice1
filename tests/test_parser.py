import unittest

from emulator.parser import parse_line


class ParseLineTest(unittest.TestCase):
    """Проверки разбора строки на команду и аргументы."""

    def test_command_and_arguments(self):
        result = parse_line("ls  -l   /tmp")
        self.assertEqual(result, ("ls", ["-l", "/tmp"]))

    def test_command_without_arguments(self):
        self.assertEqual(parse_line("exit"), ("exit", []))

    def test_blank_line(self):
        self.assertEqual(parse_line("   "), (None, []))


if __name__ == "__main__":
    unittest.main()
