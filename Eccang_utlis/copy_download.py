import os
import shutil
from pathlib import Path


def copy_latest_download():
    # Configs
    download_dir = Path.home() / 'Downloads'
    target_dir = Path(r"C:\Frank\原始数据\易仓下载")
    keywords = ["库存查询（库位）", "产品库存"]

    # Dictionary to store latest file for each keyword
    latest_files = {}

    for root, _, files in os.walk(download_dir):
        for file in files:
            if file.endswith((".csv", ".xls")):
                full_path = Path(root) / file
                for keyword in keywords:
                    if keyword in file:
                        mtime = full_path.stat().st_mtime
                        if (keyword not in latest_files or 
                                mtime > latest_files[keyword][1]):
                            latest_files[keyword] = (full_path, mtime)

    if latest_files:
        for keyword, (file_path, _) in latest_files.items():
            dest_path = target_dir / file_path.name
            shutil.copy2(file_path, dest_path)
            print(f"✅ Copied latest '{keyword}': {file_path.name}")
    else:
        print(f"⚠️ No matching files found for keywords: {keywords}")
