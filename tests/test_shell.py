import io
import unittest

from emulator.shell import Shell


def make_shell():
    """Создать оболочку, пишущую в буфер в памяти."""
    buffer = io.StringIO()
    return Shell(out=buffer), buffer


class ShellTest(unittest.TestCase):
    """Проверки REPL и команд-заглушек."""

    def test_prompt_contains_vfs_name(self):
        shell = Shell("myvfs")
        self.assertIn("myvfs", shell.prompt())

    def test_ls_stub_prints_name_and_arguments(self):
        shell, buffer = make_shell()
        self.assertTrue(shell.execute("ls -l /home"))
        self.assertEqual(buffer.getvalue(), "ls -l /home\n")

    def test_cd_stub_prints_name_and_arguments(self):
        shell, buffer = make_shell()
        shell.execute("cd /tmp")
        self.assertEqual(buffer.getvalue(), "cd /tmp\n")

    def test_unknown_command(self):
        shell, buffer = make_shell()
        self.assertFalse(shell.execute("foo"))
        self.assertEqual(buffer.getvalue(), "foo: команда не найдена\n")

    def test_exit_stops_shell(self):
        shell, _ = make_shell()
        shell.execute("exit")
        self.assertFalse(shell.running)

    def test_exit_with_arguments_is_error(self):
        shell, buffer = make_shell()
        self.assertFalse(shell.execute("exit now"))
        self.assertTrue(shell.running)
        self.assertIn("лишние аргументы", buffer.getvalue())

    def test_blank_line_is_ignored(self):
        shell, buffer = make_shell()
        self.assertTrue(shell.execute("   "))
        self.assertEqual(buffer.getvalue(), "")

    def test_interactive_loop_reads_until_exit(self):
        shell, buffer = make_shell()
        lines = iter(["ls a b", "exit", "ls never"])
        shell.run_interactive(lambda prompt: next(lines))
        self.assertEqual(buffer.getvalue(), "ls a b\n")


if __name__ == "__main__":
    unittest.main()
