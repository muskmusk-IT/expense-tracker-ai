import csv
import sys
from datetime import datetime

"""
Cara pakai:
python scripts/add_expense.py "2025-08-25" "Kopi Kenangan" "Makan & Minum" 32000
"""

# Ambil argumen dari terminal
tanggal = sys.argv[1]
toko = sys.argv[2]
kategori = sys.argv[3]
total = sys.argv[4]

# Simpan ke CSV
with open("data/expenses.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([tanggal, toko, kategori, total])

print(f"✅ Data tersimpan: {tanggal}, {toko}, {kategori}, {total}")

