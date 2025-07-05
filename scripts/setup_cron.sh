#!/bin/bash

# === Determine script directory ===
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# === Paths ===
BACKUP_SCRIPT="$SCRIPT_DIR/backup.py"
LOGROTATE_SCRIPT="$SCRIPT_DIR/logrotate.py"
PYTHON_BIN="/usr/bin/python3"

# === Ensure cron is installed ===
if ! command -v crontab &> /dev/null; then
    echo "Cron is not installed. Installing..."
    sudo apt update && sudo apt install cron -y
    sudo systemctl enable cron
    sudo systemctl start cron
fi

# === Define the cron job entries ===
CRON_ENTRIES="
0 2 * * * $PYTHON_BIN $BACKUP_SCRIPT >> $SCRIPT_DIR/backup.log 2>&1
0 0 * * 0 $PYTHON_BIN $LOGROTATE_SCRIPT >> $SCRIPT_DIR/logrotate.log 2>&1
"

# === Install without duplicating ===
( crontab -l 2>/dev/null | grep -v "$BACKUP_SCRIPT" | grep -v "$LOGROTATE_SCRIPT" ; echo "$CRON_ENTRIES" ) | crontab -

echo "✅ Cron jobs set up from: $SCRIPT_DIR"