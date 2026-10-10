#!/usr/bin/env sh
# Проверка всех параметров командной строки (этап 2).
cd "$(dirname "$0")/.." || exit 1

echo "=== 1. Без параметров (интерактивный режим, ввод закрыт) ==="
sh run.sh < /dev/null

echo
echo "=== 2. Только --vfs-path ==="
sh run.sh --vfs-path examples/demo < /dev/null

echo
echo "=== 3. Только --script ==="
sh run.sh --script examples/scripts/stage2.emu

echo
echo "=== 4. Оба параметра ==="
sh run.sh --vfs-path examples/demo --script examples/scripts/stage2.emu

echo
echo "=== 5. Несуществующий скрипт (ошибка) ==="
sh run.sh --script examples/scripts/missing.emu
echo "код завершения: $?"
