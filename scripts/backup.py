#!/usr/bin/env python3

import os
import tarfile
from datetime import datetime

# CONFIGURABLE
SOURCE_DIR = '/app/dist'  # or wherever the frontend is built
BACKUP_DIR = '/opt/backups'

def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

    print(f"Backup created: {backup_path}")

if __name__ == "__main__":
    create_backup()