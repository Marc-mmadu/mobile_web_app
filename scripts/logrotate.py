#!/usr/bin/env python3

import os
import time
from datetime import datetime, timedelta

# CONFIGURABLE
LOG_DIR = '/home/mamahmarcus792/mobile_web_app/logs'
DAYS_TO_KEEP = 2

def rotate_logs():
    now = time.time()
    cutoff = now - (DAYS_TO_KEEP * 86400)

    if not os.path.exists(LOG_DIR):
        print(f"Log directory {LOG_DIR} does not exist.")
        return

    for root, _, files in os.walk(LOG_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_mtime = os.path.getmtime(file_path)
                if file_mtime < cutoff:
                    os.remove(file_path)
                    print(f"Deleted old log: {file_path}")

if __name__ == "__main__":
    rotate_logs()