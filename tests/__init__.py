"""Тесты эмулятора: добавляют каталог src в путь поиска модулей.

Благодаря этому тесты запускаются просто командой python -m unittest
из корня репозитория, без настройки PYTHONPATH.
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)