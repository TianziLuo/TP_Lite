from openpyxl import load_workbook
import pandas as pd
from pathlib import Path

def generate_tp_csv(source_path, sheet_name, template_path, output_path):
    df = pd.read_excel(source_path, sheet_name=sheet_name, header=None, skiprows=1, usecols="A:F")
    df = df.dropna(how='all')

    if df.shape[1] >= 2:
        df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: f"'{x}" if pd.notna(x) else x)

    with open(template_path, "r", encoding="utf-8") as f:
        header = f.readline().strip()

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(header + "\n")
        df.to_csv(f, index=False, header=False)

    print(f"✅ TP CSV 已生成: {output_path}")


'''
if __name__ == "__main__":
    downloads = Path.home() / "Downloads"

    update_inventory_excel(
    source_path=r"C:\Frank\2.2_店小秘.xlsx",
    sheet_name="盘点",
    template_path=r"C:\Template\店小秘 更新库存.xlsx",
    output_path=downloads / "店小秘 更新库存.xlsx"
)
'''