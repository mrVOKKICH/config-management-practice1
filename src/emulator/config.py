"""Параметры запуска эмулятора."""

import argparse
import os
from dataclasses import dataclass
from typing import Optional

DEFAULT_VFS_NAME = "vfs"


@dataclass(frozen=True)
class Config:
    """Параметры командной строки."""

    vfs_path: Optional[str] = None
    script_path: Optional[str] = None


def parse_args(argv=None):
    """Разобрать параметры командной строки.

    Args:
        argv: список аргументов (по умолчанию sys.argv[1:]).

    Returns:
        Объект Config.
    """
    parser = argparse.ArgumentParser(
        prog="emulator",
        description="Эмулятор языка оболочки UNIX-подобной ОС.",
    )
    parser.add_argument(
        "--vfs-path",
        dest="vfs_path",
        help="путь к физическому расположению VFS",
    )
    parser.add_argument(
        "--script",
        dest="script_path",
        help="путь к стартовому скрипту с командами эмулятора",
    )
    namespace = parser.parse_args(argv)
    return Config(namespace.vfs_path, namespace.script_path)


def vfs_name(path):
    """Получить имя VFS по пути к её директории."""
    if not path:
        return DEFAULT_VFS_NAME
    name = os.path.basename(os.path.normpath(os.path.abspath(path)))
    return name or DEFAULT_VFS_NAME


def debug_lines(config):
    """Сформировать строки отладочного вывода всех параметров."""
    shown = ["[debug] Параметры запуска:"]
    shown.append(f"[debug]   vfs-path = {config.vfs_path}")
    shown.append(f"[debug]   script   = {config.script_path}")
    return shown
