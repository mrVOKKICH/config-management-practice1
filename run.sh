#!/usr/bin/env sh
# Запуск эмулятора: ./run.sh [--vfs-path ПУТЬ] [--script СКРИПТ]
ROOT="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    PYTHON=python
fi
PYTHONPATH="$ROOT/src" exec "$PYTHON" -m emulator "$@"