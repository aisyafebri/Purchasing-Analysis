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

## 📊 Hasil Analisis & Visualisasi Dashboard

### 1. Visualisasi Distribusi Anggaran Pengadaan
![Distribusi Anggaran](purchasing_dashboard_chart.png)

### 2. Status Monitoring Stok & Action Plan (Purchase Order)

<table>
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th>Kode Barang</th>
      <th>Nama Barang</th>
      <th>Supplier</th>
      <th style="text-align:center;">Stok Saat Ini</th>
      <th style="text-align:center;">ROP</th>
      <th style="text-align:center;">Rekomendasi Pesan</th>
      <th style="text-align:right;">Estimasi Biaya PO</th>
      <th style="text-align:center;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>BRG-001</strong></td>
      <td>Kardus Box A1</td>
      <td>PT Packindo Utama</td>
      <td align="center">150</td>
      <td align="center">275</td>
      <td align="center"><strong>600</strong></td>
      <td align="right">Rp 3.000.000</td>
      <td align="center">🔴 PESAN SEKARANG</td>
    </tr>
    <tr>
      <td><strong>BRG-002</strong></td>
      <td>Lakban Bening</td>
      <td>CV Mitra Kemasan</td>
      <td align="center">450</td>
      <td align="center">120</td>
      <td align="center">0</td>
      <td align="right">Rp 0</td>
      <td align="center">🟢 STOK AMAN</td>
    </tr>
    <tr>
      <td><strong>BRG-003</strong></td>
      <td>Plastik Bubble Wrap</td>
      <td>PT Packindo Utama</td>
      <td align="center">80</td>
      <td align="center">210</td>
      <td align="center"><strong>370</strong></td>
      <td align="right">Rp 31.450.000</td>
      <td align="center">🔴 PESAN SEKARANG</td>
    </tr>
    <tr>
      <td><strong>BRG-004</strong></td>
      <td>Label Stiker Resi</td>
      <td>UD Sarana Cetak</td>
      <td align="center">600</td>
      <td align="center">260</td>
      <td align="center">0</td>
      <td align="right">Rp 0</td>
      <td align="center">🟢 STOK AMAN</td>
    </tr>
    <tr>
      <td><strong>BRG-005</strong></td>
      <td>Tali Strapping</td>
      <td>PT Packindo Utama</td>
      <td align="center">40</td>
      <td align="center">75</td>
      <td align="center"><strong>110</strong></td>
      <td align="right">Rp 4.950.000</td>
      <td align="center">🔴 PESAN SEKARANG</td>
    </tr>
    <tr>
      <td><strong>BRG-006</strong></td>
      <td>Kertas A4 80gr</td>
      <td>UD Sarana Cetak</td>
      <td align="center">20</td>
      <td align="center">74</td>
      <td align="center"><strong>220</strong></td>
      <td align="right">Rp 12.100.000</td>
      <td align="center">🔴 PESAN SEKARANG</td>
    </tr>
  </tbody>
</table>

<br>

> 💡 **Key Takeaway:** Total anggaran pengadaan yang dibutuhkan untuk 4 barang kritis adalah **Rp 51.500.000,-** dengan alokasi terbesar pada pengadaan bahan proteksi packaging di *PT Packindo Utama*.

<br>
> 💡 **Key Takeaway:** Total anggaran pengadaan yang dibutuhkan untuk 4 barang kritis adalah **Rp 51.500.000,-** dengan alokasi terbesar pada pengadaan bahan proteksi packaging di *PT Packindo Utama*.

---

## 🚀 Struktur Direktori

```text
├── Purchasing_data.csv        # Dataset operasional inventaris & supplier
├── Purchasing_data_analys.py  # Script otomasi analisis data menggunakan Pandas
├── purchasing_dashboard_chart.png # Visualisasi grafik anggaran per supplier
└── README.md                  # Dokumentasi proyek