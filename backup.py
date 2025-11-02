import shutil
import os
from datetime import datetime
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config

def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"D:\\AI-Projects\\Backups\\backup_{timestamp}"
    
    print(f"📦 Backing up to: {backup_path}")
    
    # Backup data
    if os.path.exists(config.DATA_PATH):
        shutil.copytree(
            config.DATA_PATH,
            os.path.join(backup_path, "data"),
            ignore=shutil.ignore_patterns('*.pyc', '__pycache__', '*.tmp')
        )
    
    # Backup projects
    if os.path.exists(config.PROJECTS_PATH):
        shutil.copytree(
            config.PROJECTS_PATH,
            os.path.join(backup_path, "projects")
        )
    
    print("✅ Backup เสร็จ!")
    
    # ลบ backup เก่า > 7 วัน
    cleanup_old_backups(7)

def cleanup_old_backups(days=7):
    import time
    backup_dir = "D:\\AI-Projects\\Backups"
    
    if not os.path.exists(backup_dir):
        return
    
    now = time.time()
    
    for folder in os.listdir(backup_dir):
        folder_path = os.path.join(backup_dir, folder)
        if os.path.isdir(folder_path):
            age = now - os.path.getmtime(folder_path)
            if age > days * 86400:
                shutil.rmtree(folder_path)
                print(f"🗑️ ลบ backup เก่า: {folder}")

if __name__ == "__main__":
    backup()