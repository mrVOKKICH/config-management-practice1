#!/usr/bin/env sh
# Запуск эмулятора: ./run.sh [--vfs-path ПУТЬ] [--script СКРИПТ]
ROOT="$(cd "$(dirname "$0")" && pwd)"
PYTHONPATH="$ROOT/src" exec python3 -m emulator "$@"
