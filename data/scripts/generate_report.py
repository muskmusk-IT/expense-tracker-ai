import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = "data/expenses.csv"
output_path = "data/weekly_report.png"

if not os.path.exists(csv_path):
    print("⚠️ File data/expenses.csv tidak ditemukan, skip generate report.")
    exit(0)

try:
    df = pd.read_csv(csv_path, names=["Tanggal", "Toko", "Kategori", "Total"])
    df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
    df = df.dropna()

    if df.empty:
        print("⚠️ Tidak ada data valid di CSV, skip generate report.")
        exit(0)

    # Rekap mingguan
    weekly = df.groupby(pd.Grouper(key="Tanggal", freq="W"))["Total"].sum()

    plt.figure(figsize=(8,4))
    weekly.plot(kind="bar", title="Pengeluaran Mingguan")
    plt.ylabel("Total (Rp)")

    plt.tight_layout()
    plt.savefig(output_path)
    print(f"📊 Laporan mingguan berhasil dibuat: {output_path}")

except Exception as e:
    print(f"❌ Gagal generate report: {e}")
    exit(1)
