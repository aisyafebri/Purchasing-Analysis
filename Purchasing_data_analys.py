import pandas as pd

# 1. Load Data
df = pd.read_csv("Purchasing_data.csv")

# 2. Hitung Reorder Point (ROP)
# ROP = (Konsumsi Harian * Lead Time) + Stok Minimal
df["Reorder_Point"] = (df["Daily_Usage"] * df["Lead_Time_Days"]) + df["Min_Stock"]

# 3. Tentukan Status Pemesanan (Actionable Alert)
df["Order_Status"] = df.apply(
    lambda x: (
        "PESAN SEKARANG"
        if x["Stock_On_Hand"] <= x["Reorder_Point"]
        else "STOK AMAN"
    ),
    axis=1,
)

# 4. Hitung Jumlah Rekomendasi Pembelian (Pengisian Stok untuk 30 Hari)
df["Suggested_Order_Qty"] = df.apply(
    lambda x: (
        (x["Daily_Usage"] * 30) - x["Stock_On_Hand"]
        if x["Order_Status"] == "PESAN SEKARANG"
        else 0
    ),
    axis=1,
)

# 5. Hitung Estimasi Total Biaya PO per Barang
df["Estimated_PO_Cost"] = df["Suggested_Order_Qty"] * df["Unit_Cost"]

# 6. Tampilkan Hasil Analisis Kritis (Barang yang Wajib Dipesan)
items_to_order = df[df["Order_Status"] == "PESAN SEKARANG"][
    [
        "Item_Code",
        "Item_Name",
        "Supplier_Name",
        "Stock_On_Hand",
        "Reorder_Point",
        "Suggested_Order_Qty",
        "Estimated_PO_Cost",
    ]
]

print("=== DAFTAR BARANG YANG HARUS DIPESAN (PURCHASE ORDER NEEDED) ===")
print(items_to_order.to_string(index=False))

# 7. Summary untuk Dashboard Executive/Manajemen
total_budget = df["Estimated_PO_Cost"].sum()
total_items_to_buy = len(items_to_order)

print("\n=== RINGKASAN EKSEKUTIF PURCHASING ===")
print(f"Total Jenis Barang Harus Dipesan : {total_items_to_buy} Item")
print(f"Total Estimasi Anggaran Pengadaan: Rp {total_budget:,.2f}")