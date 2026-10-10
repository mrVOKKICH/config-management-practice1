@echo off
chcp 65001 >nul
rem Проверка всех параметров командной строки (этап 2).
cd /d "%~dp0.."

echo === 1. Без параметров (интерактивный режим, ввод закрыт) ===
call run.bat < NUL

echo.
echo === 2. Только --vfs-path ===
call run.bat --vfs-path examples\demo < NUL

echo.
echo === 3. Только --script ===
call run.bat --script examples\scripts\stage2.emu

echo.
echo === 4. Оба параметра ===
call run.bat --vfs-path examples\demo --script examples\scripts\stage2.emu

echo.
echo === 5. Несуществующий скрипт (ошибка) ===
call run.bat --script examples\scripts\missing.emu
echo код завершения: %ERRORLEVEL%
