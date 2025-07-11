from tkinter import messagebox
import time
from pathlib import Path
from Eccang_utlis.unzip import unzip
from Eccang_utlis.xls2csv import xls2csv
from Eccang_utlis.rename import rename
from Eccang_utlis.copy_download import copy_latest_download

from TP_utils.open_excel_utils import open_excel_file
from TP_utils.copy_file_utils import copy_file_to_dirs
from TP_utils.create_file_utils import generate_tp_csv
from TP_utils.TP_upload_utils import teapplix_upload

def step_1_all():
    print("🍉 Running: Unzip ➜ Convert ➜ Rename")
    try:
        unzip()
        print("✔ Step Unzip completed")
        
        xls2csv()
        print("✔ Step Convert completed")
        
        rename()
        print("✔ Step Rename completed")
        
        time.sleep(1)
        copy_latest_download
        print("✔ Step Copy completed")

        messagebox.showinfo("Done", "Eccang completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Eccang error:\n{e}")


downloads = Path.home() / "Downloads"

# === Step 1 ===
def step_2_all(): open_excel_file(r"C:\Frank\1.1_核心.xlsx")

# === Step 2 ===
def step_3_1(): open_excel_file(r"C:\Frank\2.1_易仓管理.xlsx")
def step_3_2():
    generate_tp_csv(
        source_path=r"C:\Frank\2.1_易仓管理.xlsx",
        sheet_name="易仓进TP",
        template_path=r"C:\Template\TP-Upload.csv",
        output_path=downloads / "TP-Upload.csv"
    )

    time.sleep(1)

    teapplix_upload(
        username="wayfaircolourtree",
        email="wayfair.colourtree@gmail.com",
        password="Colourtree168!!",
        csv_path=str(downloads / "TP-Upload.csv")
    )

    time.sleep(1)  

    # old TP
    teapplix_upload(
        username="colourtree",
        email="colourtreeusa@gmail.com",
        password="Colourtree168!",
        csv_path=str(downloads / "TP-Upload.csv")

    )

    time.sleep(2)

    copy_file_to_dirs(
        str(downloads / "TP-Upload.csv"),
        [
            r"C:\Frank\易仓-TP",
            r"C:\ACT\公用核心\upload_1.1 TP 库存更新"
        ]
    )


def step_3_3():
    open_excel_file(r"C:\Frank\易仓-TP\SKUINV.xlsx")


def step_3_4():
    copy_file_to_dirs(
        r"C:\Frank\易仓-TP\SKUINV.xlsx",
        [r"\\MICHAEL\ctshippingapp\SHIPDOC\INVUPLOAD"]
    )

