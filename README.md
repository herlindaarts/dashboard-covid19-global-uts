# Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022
**Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data**

---

## 📌 Identitas Proyek
- **Judul Proyek:** Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022
- **Mata Kuliah:** Visualisasi Data
- **Teknologi Utama:** Python, Streamlit, Pandas, Plotly, NumPy
- **Dataset Utama:** `data/covid19_daily_clean.csv` (184.787 baris data harian)
- **Dataset Pendukung:** `data/covid19_summary_clean.csv` (226 negara & pemetaan benua)

---

## 🌐 Sumber Dataset
Dataset bersumber resmi dari Kaggle:
- **Tautan Kaggle:** [COVID-19 Global Dataset by Joseph Assaker](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset)
- **Sumber Data Asli:** Worldometer Coronavirus Tracking
- **Rentang Waktu Data:** 22 Januari 2020 s.d. 14 Mei 2022
- **Cakupan Wilayah:** 226 Negara dan Wilayah Teritori di 6 Benua

---

## 📁 Struktur Direktori
```text
covid19_uts_dataset_rapi/
├── data/
│   ├── covid19_daily_clean.csv       # Dataset utama harian COVID-19 (184.787 baris)
│   └── covid19_summary_clean.csv     # Dataset ringkasan dan pemetaan benua (226 negara)
├── scripts/
│   └── clean_data.py                 # Skrip otomasi pembersihan data awal
├── app.py                            # Aplikasi utama Dashboard Streamlit
├── requirements.txt                  # Daftar pustaka Python yang dibutuhkan
├── README.md                         # Dokumentasi lengkap proyek UTS
├── README_DATASET.md                 # Dokumentasi detail aturan pembersihan dataset
└── LAPORAN_KUALITAS_DATA.json        # Laporan metrik kualitas dataset
```

---

## 🚀 Panduan Instalasi dan Cara Menjalankan

### 1. Prasyarat
Pastikan sistem Anda telah terpasang **Python 3.9** atau versi lebih baru.

### 2. Membuka Terminal / Command Prompt
Buka terminal (PowerShell, Command Prompt, atau Bash) lalu navigasikan ke folder proyek:
```bash
cd c:\Users\HERLINDA\Downloads\covid19_uts_dataset_rapi
```
*(atau masuk ke dalam sub-folder `covid19_uts_dataset_rapi`)*

### 3. Instalasi Dependensi
Jalankan perintah berikut untuk menginstal seluruh pustaka yang diperlukan:
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Dashboard Streamlit
Jalankan aplikasi menggunakan perintah resmi berikut:
```bash
python -m streamlit run app.py
```
*(atau dapat juga menggunakan `streamlit run app.py`)*

### 5. Mengakses Dashboard
Setelah perintah dijalankan, Streamlit akan membuka browser secara otomatis atau Anda dapat mengaksesnya secara manual melalui URL lokal:
```text
http://localhost:8501
```

---

## 📊 Penjelasan Fitur Dashboard

### 1. Panel KPI Metric Cards (Indikator Kinerja Utama)
Dashboard menampilkan indikator metrik kartu modern dengan informasi dinamis:
- **Total Kasus Terkonfirmasi (Kumulatif):** Jumlah total kasus terakumulasi hingga batas akhir tanggal yang dipilih, dilengkapi informasi penambahan kasus baru selama rentang waktu terpilih.
- **Total Kematian (Kumulatif):** Akumulasi angka kematian akibat COVID-19, dilengkapi rincian kematian baru selama periode filter.
- **Case Fatality Rate (CFR Estimasi):** Persentase rasio fatalitas kematian terhadap total kasus terkonfirmasi ($\frac{\text{Kematian}}{\text{Kasus}} \times 100\%$).
- **Jumlah Negara Terpantau:** Total negara/wilayah yang masuk ke dalam filter aktif dari total 226 negara.

### 2. Empat Jenis Visualisasi Interaktif
1. **Line Chart (Perkembangan Kasus dari Waktu ke Waktu):**
   - Menampilkan fluktuasi penambahan kasus harian (`daily_new_cases`) bersama kurva **7-Day Moving Average** (warna biru pekat `#1D4ED8`) untuk mereduksi *noise* pelaporan akhir pekan.
   - Pengguna dapat beralih ke mode **Kasus Kumulatif** untuk melihat pertumbuhan total kasus secara berkelanjutan.
2. **Area Chart (Perkembangan Kasus Aktif / Active Cases):**
   - Menampilkan kurva berisi gradien biru halus (`rgba(37, 99, 235, 0.22)`) yang merefleksikan dinamika beban pasien yang sedang dalam perawatan atau isolasi aktif sepanjang waktu.
   - Memperlihatkan secara jelas gelombang awal 2020, gelombang Delta pertengahan 2021, dan ledakan gelombang Omicron awal 2022.
3. **Horizontal Bar Chart (Negara dengan Kasus Tertinggi):**
   - Memvisualisasikan peringkat negara-negara dengan beban kasus terkonfirmasi terbesar.
   - Dilengkapi *slider* interaktif untuk mengatur jumlah negara yang ingin ditampilkan (Top 5 hingga Top 25).
   - Diurutkan dari yang tertinggi ke terendah dengan gradien warna biru dan label angka eksak.
4. **Donut / Pie Chart (Perbandingan Kasus Berdasarkan Benua / Negara):**
   - Mengelompokkan proporsi kasus berdasarkan benua (Asia, Eropa, Amerika Utara, Amerika Selatan, Afrika, Oseania).
   - Apabila filter dipersempit ke satu benua, grafik secara dinamis menyesuaikan menjadi perbandingan pangsa kasus antar negara pada benua tersebut.

### 3. Filter Interaktif Dinamis
- **Filter Rentang Tanggal:** Kalender interaktif (`date_input`) yang dibatasi mulai 22 Januari 2020 hingga 14 Mei 2022.
- **Preset Periode Cepat:** Shortcut pemilihan rentang waktu populer:
  - *Seluruh Periode (2020 - 2022)*
  - *Tahun 2020 (Awal Pandemi Global)*
  - *Tahun 2021 (Gelombang Alpha & Delta)*
  - *Tahun 2022 (Gelombang Omicron)*
  - *Kustom (Pilihan Bebas)*
- **Filter Wilayah Berdasarkan Benua:** Multi-select benua untuk mempersempit kelompok wilayah.
- **Filter Negara Spesifik:** Memilih satu, beberapa, atau seluruh 226 negara yang tersedia. Seluruh filter saling memengaruhi grafik dan metrik KPI secara *real-time*.

### 4. Kotak Ringkasan & Insight Dinamis
Menghasilkan narasi analitis otomatis berdasarkan hasil perhitungan data riil:
- **Puncak Lonjakan Kasus:** Menentukan tanggal pasti terjadinya lonjakan harian tertinggi serta angka kasus pada hari tersebut.
- **Episentrum Kasus Terbesar:** Negara dengan jumlah kasus terkonfirmasi tertinggi serta persentase kontribusinya terhadap total filter.
- **Analisis Tingkat Fatalitas:** Estimasi rata-rata CFR pada subset data.
- **Dinamika Kasus Aktif:** Meninjau tren beban kasus aktif pada akhir periode (meningkat, menurun/fase pemulihan, atau stabil).

### 5. Eksplorasi Data & Unduh CSV
Tabel interaktif untuk melihat data mentah hasil penyaringan dan tombol unduh file CSV untuk kebutuhan analisis lanjutan.

---

## 🔬 Metodologi dan Integritas Penanganan Data

### 1. Penanganan Missing Values (Nilai Kosong / NaN)
- Berdasarkan hasil audit data (`LAPORAN_KUALITAS_DATA.json`), terdapat nilai kosong pada kolom `daily_new_cases` (10.458 baris), `active_cases` (18.040 baris), dan `daily_new_deaths` (26.937 baris).
- **Prinsip Kejujuran Data:** Nilai kosong **tidak diganti secara otomatis menjadi nol**. Mengisi NaN menjadi 0 akan menciptakan bias serius, seolah-olah penularan atau kematian berhenti total pada hari tersebut.
- Dashboard menggunakan agregasi `skipna=True` dan perhitungan kumulatif per negara berbasis observasi terakhir yang valid (*last valid observation*).

### 2. Penanganan Nilai Negatif
- Ditemukan sejumlah baris bernilai negatif pada kasus baru harian (20 baris) dan kematian baru (9 baris), contohnya pada El Salvador, Afghanistan, dan Jordan.
- **Alasan Ilmiah Epidemiologi:** Nilai negatif dalam data resmi Worldometer/WHO merupakan **koreksi data retrospektif** (*retrospective adjustments*) oleh otoritas kesehatan pemerintah (misalnya pengeluaran kasus negatif palsu atau penghapusan catatan duplikat). Nilai ini dipertahankan agar tidak mendistorsi total kumulatif riil.

### 3. Pencegahan Visualisasi Menyesatkan (Anti-Misleading Visuals)
- Seluruh sumbu bar chart dimulai dari titik dasar 0 untuk mencegah distorsi persepsi perbandingan visual.
- Indikator 7-Day Moving Average disediakan guna mereduksi bias pola pelaporan akhir pekan (*weekend reporting lag*).

---

## 🎨 Desain dan Palet Warna
Dashboard dirancang dengan pendekatan desain analitis modern dan bersih:
- **Biru Primer (Navy & Royal Blue):** `#1E3A8A`, `#2563EB`, `#1D4ED8` (memberikan kesan kredibel, fokus, dan profesional).
- **Biru Aksen & Cyan:** `#3B82F6`, `#60A5FA`, `#93C5FD` (untuk pembeda seri data sekunder dan visualisasi bergerak).
- **Putih & Abu-abu Netral:** `#FFFFFF`, `#F8FAFC`, `#E2E8F0`, `#64748B`, `#0F172A` (menghadirkan kontras teks yang nyaman dibaca dan bebas gangguan visual).
