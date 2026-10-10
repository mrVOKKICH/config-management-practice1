"""Точка входа эмулятора."""

from emulator.shell import Shell

EXIT_OK = 0


def main():
    """Запустить эмулятор в интерактивном режиме."""
    Shell().run_interactive()
    return EXIT_OK
