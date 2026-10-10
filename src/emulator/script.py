"""Выполнение стартового скрипта с командами эмулятора."""

COMMENT_MARK = "#"


def strip_comment(line):
    """Убрать из строки комментарий (от символа # до конца) и пробелы."""
    return line.split(COMMENT_MARK, 1)[0].strip()


def run_script(shell, path):
    """Выполнить скрипт, имитируя диалог с пользователем.

    На экран выводятся и введённые команды (после приглашения),
    и результат их выполнения. Строки-комментарии пропускаются,
    ошибки команд не прерывают выполнение скрипта.

    Args:
        shell: оболочка, выполняющая команды.
        path: путь к файлу скрипта.

    Raises:
        OSError: если файл скрипта не удалось прочитать.
    """
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    for raw_line in lines:
        command = strip_comment(raw_line)
        if not command:
            continue
        shell.write(shell.prompt() + command)
        shell.execute(command)
        if not shell.running:
            break
