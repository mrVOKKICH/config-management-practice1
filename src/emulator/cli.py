"""Точка входа эмулятора: параметры командной строки и режимы запуска."""

import sys

from emulator.config import debug_lines, parse_args, vfs_name
from emulator.script import run_script
from emulator.shell import Shell

EXIT_OK = 0
EXIT_ERROR = 1


def _run_script(shell, path):
    """Выполнить стартовый скрипт, вернуть код завершения."""
    try:
        run_script(shell, path)
    except OSError as error:
        print(f"Ошибка чтения скрипта: {error}", file=sys.stderr)
        return EXIT_ERROR
    return EXIT_OK


def main(argv=None):
    """Запустить эмулятор.

    С параметром --script выполняется стартовый скрипт, после чего
    эмулятор завершается. Без него запускается интерактивный режим.
    """
    config = parse_args(argv)
    for line in debug_lines(config):
        print(line)
    shell = Shell(vfs_name(config.vfs_path))
    if config.script_path is None:
        shell.run_interactive()
        return EXIT_OK
    return _run_script(shell, config.script_path)
