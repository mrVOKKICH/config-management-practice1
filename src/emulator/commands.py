"""Реализации команд эмулятора."""

from emulator.errors import CommandError


def _stub_text(name, args):
    """Собрать строку из имени команды и её аргументов."""
    return " ".join([name, *args])


def cmd_ls(shell, args):
    """Заглушка ls: выводит своё имя и аргументы."""
    shell.write(_stub_text("ls", args))


def cmd_cd(shell, args):
    """Заглушка cd: выводит своё имя и аргументы."""
    shell.write(_stub_text("cd", args))


def cmd_exit(shell, args):
    """Завершить работу эмулятора (аргументы не допускаются)."""
    if args:
        raise CommandError("лишние аргументы")
    shell.running = False


COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "exit": cmd_exit,
}
