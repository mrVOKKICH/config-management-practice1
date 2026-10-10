@echo off
chcp 65001 >nul
rem Запуск эмулятора: run.bat [--vfs-path ПУТЬ] [--script СКРИПТ]
set PYTHONPATH=%~dp0src
set PYTHONUTF8=1
python -m emulator %*
