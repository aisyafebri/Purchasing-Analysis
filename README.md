# 📦 Inventory Control & Purchase Order (PO) Optimization Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Domain](https://img.shields.io/badge/Domain-Purchasing%20%26%20Supply%20Chain-green)

Proyek ini bertujuan untuk mengoptimalkan manajemen persediaan (*inventory control*) dan otomatisasi alur pemesanan barang (*Purchase Order*) menggunakan Python (Pandas). Analisis ini dirancang untuk mencegah terjadinya *stockout* (kehabisan stok) operasional serta memberikan estimasi kebutuhan anggaran pengadaan secara presisi berbasis data.

---

## 🎯 Latar Belakang & Masalah
Dalam operasional pengadaan barang (*purchasing/procurement*), keterlambatan pemesanan ulang (*reorder*) seringkali menyebabkan proses operasional terhenti. Di sisi lain, pemesanan berlebih dapat mengakibatkan akumulasi *dead stock* dan pemborosan arus kas.

**Tujuan Proyek:**
- Mengotomatisasi penentuan titik pemesanan kembali menggunakan metode **Reorder Point (ROP)**.
- Menghasilkan *actionable alerts* (Status: `PESAN SEKARANG` vs `STOK AMAN`).
- Menghitung rekomendasi kuantitas pemesanan (*Suggested Order Quantity*) untuk siklus 30 hari ke depan.
- Mengestimasi total anggaran pengadaan (*Estimated PO Cost*) per barang dan supplier.

---

## 📊 Metodologi & Formula Perhitungan

1. **Reorder Point (ROP):**
   $$\text{ROP} = (\text{Daily Usage} \times \text{Lead Time Days}) + \text{Safety / Minimum Stock}$$

2. **Status Pemesanan (Order Alert):**
   $$\text{Status} = \begin{cases} \text{"PESAN SEKARANG"}, & \text{jika } \text{Stock On Hand} \le \text{ROP} \\ \text{"STOK AMAN"}, & \text{jika } \text{Stock On Hand} > \text{ROP} \end{cases}$$

3. **Suggested Reorder Quantity (Target Kebutuhan 30 Hari):**
   $$\text{Qty Pesan} = (\text{Daily Usage} \times 30) - \text{Stock On Hand}$$

4. **Estimated PO Cost:**
   $$\text{Total Cost} = \text{Suggested Reorder Quantity} \times \text{Unit Cost}$$

---

## 🚀 Struktur Direktori

```text
├── Purchasing_data.csv       # Dataset operasional inventaris & supplier
├── Purchasing_data_analys.py # Script otomasi analisis data menggunakan Pandas
└── README.md                 # Dokumentasi proyek