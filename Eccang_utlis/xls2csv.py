import os
from pathlib import Path


def xls2csv():
    folder_path = Path.home() / "Downloads"

    matched_files = []
    for filename in os.listdir(folder_path):
        if "库存查询（库位）" in filename and filename.lower().endswith('.xls'):
            full_path = os.path.join(folder_path, filename)
            matched_files.append((full_path, os.path.getmtime(full_path)))

    if matched_files:

        matched_files.sort(key=lambda x: x[1], reverse=True)
        latest_file = matched_files[0][0]

        # Construct new file path with .csv extension
        new_path = os.path.splitext(latest_file)[0] + '.csv'

        try:
            os.rename(latest_file, new_path)
            print(f"✅ The latest file has been renamed to CSV:\n{latest_file} → {new_path}")
        except Exception as e:
            print(f"❌ Failed to rename the file: {e}")
    else:
        print("📌 No .xls file found containing '库存查询（库位）' in the name.")


'''
if __name__ == "__main__":
    rename()
'''