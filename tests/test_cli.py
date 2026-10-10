import contextlib
import io
import os
import tempfile
import unittest

from emulator.cli import EXIT_ERROR, EXIT_OK, main
from emulator.config import Config, debug_lines, parse_args, vfs_name
from emulator.script import run_script, strip_comment
from emulator.shell import Shell


def run_main(argv):
    """Запустить main и вернуть (код, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


def write_script(text):
    """Записать скрипт во временный файл и вернуть путь к нему."""
    handle = tempfile.NamedTemporaryFile(
        "w", suffix=".emu", delete=False, encoding="utf-8"
    )
    with handle:
        handle.write(text)
    return handle.name


class ConfigTest(unittest.TestCase):
    """Проверки параметров командной строки."""

    def test_defaults(self):
        self.assertEqual(parse_args([]), Config(None, None))

    def test_both_parameters(self):
        config = parse_args(["--vfs-path", "/a/b", "--script", "s.emu"])
        self.assertEqual(config, Config("/a/b", "s.emu"))

    def test_vfs_name_from_path(self):
        self.assertEqual(vfs_name("/data/my_vfs/"), "my_vfs")
        self.assertEqual(vfs_name(None), "vfs")

    def test_debug_lines_show_all_parameters(self):
        text = "\n".join(debug_lines(Config("/a", "s.emu")))
        self.assertIn("/a", text)
        self.assertIn("s.emu", text)


class ScriptTest(unittest.TestCase):
    """Проверки выполнения стартового скрипта."""

    def test_strip_comment(self):
        self.assertEqual(strip_comment("ls -l # список"), "ls -l")
        self.assertEqual(strip_comment("# только комментарий"), "")

    def test_script_echoes_input_and_output(self):
        path = write_script("# коммент\nls a\n\ncd b # хвост\n")
        self.addCleanup(os.remove, path)
        buffer = io.StringIO()
        run_script(Shell("v", buffer), path)
        expected = "v$ ls a\nls a\nv$ cd b\ncd b\n"
        self.assertEqual(buffer.getvalue(), expected)

    def test_script_continues_after_error_and_stops_on_exit(self):
        path = write_script("foo\nls ok\nexit\nls skipped\n")
        self.addCleanup(os.remove, path)
        buffer = io.StringIO()
        run_script(Shell("v", buffer), path)
        self.assertIn("foo: команда не найдена", buffer.getvalue())
        self.assertIn("ls ok", buffer.getvalue())
        self.assertNotIn("skipped", buffer.getvalue())


class MainTest(unittest.TestCase):
    """Проверки режимов запуска main."""

    def test_script_mode_prints_debug_and_dialog(self):
        path = write_script("ls x\n")
        self.addCleanup(os.remove, path)
        code, out, _ = run_main(["--vfs-path", "/d/demo", "--script", path])
        self.assertEqual(code, EXIT_OK)
        self.assertIn("[debug]   vfs-path = /d/demo", out)
        self.assertIn("demo$ ls x", out)

    def test_missing_script_is_error(self):
        code, _, err = run_main(["--script", "/no/such/script.emu"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("Ошибка чтения скрипта", err)


if __name__ == "__main__":
    unittest.main()
