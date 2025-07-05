#!/usr/bin/env python3

import os
import datetime

# ✅ Configurable paths
LOG_DIR = '/home/mamahmarcus792/logs'
ARCHIVE_DIR = os.path.join(LOG_DIR, "archived")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

print(f"🔁 Rotating logs in: {LOG_DIR}")


rotated = False

for filename in os.listdir(LOG_DIR):
    if filename.endswith(".log"):
        log_path = os.path.join(LOG_DIR, filename)

        if os.path.isfile(log_path):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_name = f"{filename}.{timestamp}.gz"
            archive_path = os.path.join(ARCHIVE_DIR, archive_name)

            # Compress the log file
            os.system(f"gzip -c {log_path} > {archive_path}")
            # Clear original log file
            open(log_path, 'w').close()

            print(f"✅ Rotated: {filename} → {archive_name}")
            rotated = True

if not rotated:
    print("⚠️ No .log files found to rotate.")