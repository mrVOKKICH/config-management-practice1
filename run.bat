@echo off
rem Запуск эмулятора: run.bat [--vfs-path ПУТЬ] [--script СКРИПТ]
set PYTHONPATH=%~dp0src
python -m emulator %*
