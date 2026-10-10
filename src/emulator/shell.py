"""Оболочка эмулятора: выполнение команд и интерактивный цикл (REPL)."""

import sys

from emulator.commands import COMMANDS
from emulator.errors import CommandError
from emulator.parser import parse_line

DEFAULT_VFS_NAME = "vfs"


class Shell:
    """Состояние и поведение эмулятора оболочки."""

    def __init__(self, vfs_name=DEFAULT_VFS_NAME, out=None):
        """Создать оболочку.

        Args:
            vfs_name: имя VFS, показываемое в приглашении к вводу.
            out: поток вывода (по умолчанию sys.stdout).
        """
        self.vfs_name = vfs_name
        self.out = out if out is not None else sys.stdout
        self.running = True

    def prompt(self):
        """Вернуть приглашение к вводу, содержащее имя VFS."""
        return f"{self.vfs_name}$ "

    def write(self, text=""):
        """Вывести строку текста с переводом строки."""
        self.out.write(text + "\n")

    def execute(self, line):
        """Выполнить одну введённую строку.

        Returns:
            True, если команда выполнена без ошибок (или строка пуста).
        """
        name, args = parse_line(line)
        if name is None:
            return True
        handler = COMMANDS.get(name)
        if handler is None:
            self.write(f"{name}: команда не найдена")
            return False
        try:
            handler(self, args)
        except CommandError as error:
            self.write(f"{name}: {error}")
            return False
        return True

    def run_interactive(self, input_func=input):
        """Запустить интерактивный диалог до команды exit или EOF."""
        while self.running:
            try:
                line = input_func(self.prompt())
            except EOFError:
                self.write()
                break
            except KeyboardInterrupt:
                self.write()
                continue
            self.execute(line)
