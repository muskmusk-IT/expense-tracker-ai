import csv
import sys

"""
Cara pakai (kalau nanti dijalankan lokal):
python scripts/add_expense.py "2025-06-07" "Shell Serang Cikupa-1 TGR" "Transportasi" 50000
"""

tanggal, toko, kategori, total = sys.argv[1:5] if len(sys.argv) >= 5 else (None, None, None, None)

if not all([tanggal, toko, kategori, total]):
    print("Gunakan: python scripts/add_expense.py <YYYY-MM-DD> <Toko> <Kategori> <Total>")
    raise SystemExit(1)

with open("data/expenses.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([tanggal, toko, kategori, total])

print(f"✅ Data tersimpan: {tanggal}, {toko}, {kategori}, {total}")
