import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/expenses.csv", names=["Tanggal", "Toko", "Kategori", "Total"])
df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

# Rekap mingguan
weekly = df.groupby(pd.Grouper(key="Tanggal", freq="W"))["Total"].sum()

plt.figure(figsize=(8,4))
weekly.plot(kind="bar", title="Pengeluaran Mingguan")
plt.ylabel("Total (Rp)")

plt.tight_layout()
plt.savefig("data/weekly_report.png")
print("📊 Laporan mingguan berhasil dibuat: data/weekly_report.png")
