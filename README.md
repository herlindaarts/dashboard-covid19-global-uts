# 🌍 Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022

### Dashboard Analisis Data dan Visualisasi Interaktif Berbasis Python & Streamlit

**Proyek Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data**

Dashboard interaktif untuk menganalisis perkembangan kasus COVID-19 di berbagai negara selama periode 22 Januari 2020 hingga 14 Mei 2022. Proyek ini menggunakan Python, Streamlit, Pandas, NumPy, dan Plotly untuk mengolah, menganalisis, serta menyajikan data epidemiologi dalam bentuk visualisasi interaktif yang informatif dan mudah dipahami.

---

## 🌐 Akses Dashboard

- **Dashboard Online:** https://dashboard-covid19-global-uts-jjhjphkik97kkvgjfghbs8.streamlit.app/
- **Repository GitHub:** https://github.com/herlindaarts/dashboard-covid19-global-uts
- **Dataset Kaggle:** https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset

---

## 📌 Identitas Proyek dan Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama Mahasiswa | HERLINDA ARTIKA SARI |
| NIM | 241041011 |
| Program Studi | D3 Manajemen Informatika |
| Mata Kuliah | Visualisasi Data (UTS) |
| Judul Proyek | Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022 |
| Bahasa Pemrograman | Python |
| Framework | Streamlit |
| Library Visualisasi | Plotly |
| Pengolahan Data | Pandas, NumPy |

---

## 📖 Latar Belakang

COVID-19 merupakan pandemi global yang memberikan dampak besar terhadap berbagai aspek kehidupan masyarakat. Perkembangan kasus positif, angka kematian, dan kasus aktif berbeda-beda di setiap negara serta mengalami perubahan dari waktu ke waktu.

Banyaknya data yang tersedia membutuhkan proses pengolahan dan penyajian yang tepat agar informasi lebih mudah dipahami. Oleh karena itu, proyek ini dikembangkan untuk menyajikan perkembangan COVID-19 global melalui dashboard interaktif.

Dashboard ini memungkinkan pengguna melihat pola penyebaran COVID-19, membandingkan jumlah kasus antarnegara, mengetahui distribusi kasus berdasarkan benua, serta memahami perubahan kasus dari waktu ke waktu.

---

## 📊 Sumber dan Deskripsi Dataset

Dataset yang digunakan dalam proyek ini diperoleh dari Kaggle:

**COVID-19 Global Dataset — Joseph Assaker**

Sumber data asli yang tercantum dalam dokumentasi dataset adalah Worldometer Coronavirus Tracking.

### Informasi Dataset

| Informasi | Keterangan |
|---|---|
| Periode Data | 22 Januari 2020 – 14 Mei 2022 |
| Jumlah Negara dan Wilayah | 226 |
| Jumlah Benua | 6 |
| Dataset Harian | 184.787 baris |
| Dataset Ringkasan | 226 baris |

Dataset utama berisi informasi perkembangan kasus COVID-19 harian, sedangkan dataset pendukung berisi data ringkasan negara dan pemetaan benua.

### Variabel yang Digunakan

| Variabel | Deskripsi |
|---|---|
| `date` | Tanggal pencatatan data |
| `country` | Nama negara |
| `cumulative_total_cases` | Total kasus terkonfirmasi secara kumulatif |
| `daily_new_cases` | Penambahan kasus baru harian |
| `active_cases` | Jumlah kasus aktif |
| `cumulative_total_deaths` | Total kematian secara kumulatif |
| `daily_new_deaths` | Penambahan kematian harian |

---

## 🗂️ Struktur Direktori Proyek

```text
covid19_uts_dataset_rapi/
│
├── data/
│   ├── covid19_daily_clean.csv
│   └── covid19_summary_clean.csv
│
├── scripts/
│   └── clean_data.py
│
├── app.py
├── requirements.txt
├── README.md
├── README_DATASET.md
└── LAPORAN_KUALITAS_DATA.json
```

### Keterangan Direktori

- `data/` : Menyimpan dataset yang telah melalui proses pembersihan.
- `scripts/` : Menyimpan skrip Python untuk proses pembersihan data.
- `app.py` : Program utama untuk menjalankan dashboard Streamlit.
- `requirements.txt` : Daftar library Python yang dibutuhkan.
- `README.md` : Dokumentasi utama proyek.
- `README_DATASET.md` : Dokumentasi proses dan aturan pembersihan dataset.
- `LAPORAN_KUALITAS_DATA.json` : Laporan hasil pemeriksaan kualitas dataset.

---

## 🚀 Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Streamlit | Framework untuk membangun dashboard interaktif |
| Pandas | Mengolah, membersihkan, dan menganalisis dataset |
| NumPy | Mendukung perhitungan dan operasi numerik |
| Plotly | Membuat grafik dan visualisasi data interaktif |

---

## 📈 Fitur Dashboard

Dashboard dikembangkan dengan beberapa fitur utama untuk membantu pengguna melakukan eksplorasi dan analisis data COVID-19.

### 1. KPI Metric Cards

Dashboard menyediakan empat indikator utama:

- **Total Kasus Terkonfirmasi:** Menampilkan jumlah kasus COVID-19 kumulatif.
- **Total Kematian:** Menampilkan jumlah kematian akibat COVID-19.
- **Case Fatality Rate (CFR):** Menunjukkan perbandingan jumlah kematian terhadap jumlah kasus terkonfirmasi.
- **Jumlah Negara Terpantau:** Menunjukkan banyaknya negara yang masuk dalam filter aktif.

### 2. Visualisasi Data

Dashboard menyediakan empat jenis visualisasi utama:

**A. Line Chart — Perkembangan Kasus COVID-19**

Menampilkan perkembangan kasus COVID-19 dari waktu ke waktu. Pengguna dapat memilih tampilan jumlah kasus baru harian beserta garis rata-rata bergerak selama tujuh hari (7-Day Moving Average), maupun perkembangan kasus kumulatif. Visualisasi ini membantu mengidentifikasi pola peningkatan dan penurunan kasus selama pandemi.

**B. Area Chart — Perkembangan Kasus Aktif**

Menampilkan perubahan jumlah kasus aktif selama periode pandemi sehingga pengguna dapat mengamati dinamika kasus aktif dari waktu ke waktu.

**C. Horizontal Bar Chart — Negara dengan Kasus Tertinggi**

Menampilkan peringkat negara berdasarkan jumlah kasus terkonfirmasi. Pengguna dapat mengatur jumlah negara yang ditampilkan melalui slider Top 5 hingga Top 25.

**D. Donut/Pie Chart — Distribusi Kasus Berdasarkan Wilayah**

Menampilkan perbandingan jumlah kasus terkonfirmasi berdasarkan benua. Ketika filter dipersempit ke satu benua, visualisasi dapat menampilkan perbandingan antarnegara di wilayah tersebut.

### 3. Filter Interaktif

Dashboard menyediakan beberapa filter untuk mempermudah eksplorasi data:

- **Filter Rentang Tanggal:** Memilih periode analisis sesuai kebutuhan.
- **Preset Periode:** Memilih seluruh periode, tahun 2020, 2021, 2022, atau periode kustom.
- **Filter Benua:** Memilih wilayah berdasarkan benua.
- **Filter Negara:** Memilih satu atau beberapa negara tertentu.

Seluruh filter dapat digunakan untuk memperbarui KPI, grafik, dan informasi analisis sesuai pilihan pengguna.

### 4. Ringkasan dan Insight

Dashboard menyediakan ringkasan analisis berdasarkan data yang dipilih, meliputi:

- Tanggal dengan lonjakan kasus harian tertinggi.
- Negara dengan jumlah kasus terkonfirmasi terbesar.
- Perbandingan tingkat fatalitas kasus (CFR).
- Perkembangan jumlah kasus aktif.
- Perubahan tren kasus berdasarkan periode yang dipilih.

### 5. Eksplorasi dan Unduh Data (Export CSV)

Dashboard menyediakan fitur tabel data dan Export CSV untuk memudahkan pengguna melihat serta mengunduh data COVID-19.

Pengguna dapat:

- Melihat data berdasarkan hasil filter yang dipilih.
- Mengatur rentang tanggal untuk menentukan periode data yang ingin dianalisis.
- Mengunduh data dalam format CSV.
- Menggunakan data hasil unduhan untuk analisis lebih lanjut melalui Microsoft Excel, Python, atau aplikasi pengolah data lainnya.

Fitur Export CSV membantu pengguna memperoleh data yang lebih spesifik sesuai kebutuhan analisis dan periode yang dipilih.

---

## 🔬 Metodologi Pengolahan Data

Sebelum digunakan dalam dashboard, dataset melalui proses pemeriksaan dan pembersihan untuk menjaga kualitas data serta mengurangi risiko kesalahan interpretasi.

### 1. Penanganan Missing Values

Dalam dataset ditemukan nilai kosong pada beberapa variabel, antara lain:

| Variabel | Jumlah Missing Values |
|---|---:|
| `daily_new_cases` | 10.458 |
| `active_cases` | 18.040 |
| `daily_new_deaths` | 26.937 |

Nilai kosong tidak langsung diganti dengan angka nol karena nilai kosong tidak selalu menunjukkan bahwa tidak ada kasus atau kematian.

Oleh karena itu, nilai kosong dipertahankan sebagai `NaN` agar informasi asli tidak berubah secara sembarangan. Pada proses agregasi, perhitungan dilakukan dengan mengabaikan nilai kosong sesuai kebutuhan analisis.

### 2. Penanganan Nilai Negatif

Ditemukan nilai negatif pada beberapa data kasus baru dan kematian baru.

Nilai tersebut dipertahankan karena dapat mencerminkan koreksi retrospektif terhadap laporan sebelumnya. Dengan demikian, data tidak langsung dihapus hanya karena memiliki nilai negatif.

### 3. Pencegahan Visualisasi Menyesatkan

Beberapa pendekatan yang diterapkan untuk menghasilkan visualisasi yang lebih mudah dipahami:

- Sumbu grafik batang dimulai dari angka nol agar perbandingan lebih adil.
- Penggunaan 7-Day Moving Average untuk membantu mengurangi fluktuasi pelaporan harian.
- Filter tanggal dan wilayah digunakan agar analisis lebih terarah.
- Nilai kosong tidak secara otomatis dianggap sebagai nol.

---

## 💡 Temuan dan Insight Analisis

Berdasarkan hasil eksplorasi dan visualisasi dataset, diperoleh beberapa temuan berikut.

### 1. Puncak Kasus Harian

Berdasarkan grafik perkembangan kasus harian, lonjakan kasus COVID-19 global paling tinggi terlihat pada awal tahun 2022, bertepatan dengan gelombang Omicron.

Pada periode tersebut, jumlah kasus harian meningkat tajam hingga mendekati 4 juta kasus sebelum mengalami penurunan.

### 2. Negara dengan Kasus Tertinggi

Berdasarkan visualisasi Horizontal Bar Chart, Amerika Serikat (USA) merupakan negara dengan jumlah kasus COVID-19 terkonfirmasi tertinggi.

Berdasarkan hasil analisis yang tercantum:

1. Amerika Serikat: sekitar 71.955.193 kasus.
2. India: sekitar 38.903.731 kasus.
3. Brasil: sekitar 23.757.741 kasus.

### 3. Perbandingan Antarbenua

Berdasarkan visualisasi Pie Chart, distribusi kasus terkonfirmasi berdasarkan benua menunjukkan:

| Benua | Persentase Kasus |
|---|---:|
| Eropa | 32,2% |
| Asia | 27,1% |
| Amerika Utara | 24,1% |
| Amerika Selatan | 12,9% |
| Afrika | 3,07% |
| Australia/Oseania | 0,636% |

Hasil tersebut menunjukkan bahwa Eropa memiliki proporsi kasus terkonfirmasi paling besar dibandingkan benua lainnya.

### 4. Tingkat Fatalitas (Case Fatality Rate)

Berdasarkan hasil analisis yang tercantum, Case Fatality Rate (CFR) tercatat sebesar 1,21%, dengan total 6.287.654 kematian dari 520.833.195 kasus terkonfirmasi.

Rumus perhitungan:

\[
CFR = \frac{\text{Total Kematian}}{\text{Total Kasus Terkonfirmasi}} \times 100\%
\]

Artinya, terdapat sekitar 1,21 kematian untuk setiap 100 kasus terkonfirmasi berdasarkan rasio kumulatif tersebut.

### 5. Perkembangan Kasus Aktif

Grafik kasus aktif menunjukkan beberapa gelombang peningkatan selama pandemi.

Lonjakan paling besar terlihat pada awal tahun 2022 saat gelombang Omicron, dengan jumlah kasus aktif mencapai hampir 60 juta. Setelah mencapai puncaknya, jumlah kasus aktif mengalami penurunan hingga akhir periode pengamatan.

**Catatan:** Angka dan temuan pada bagian ini merupakan hasil analisis yang perlu disesuaikan dengan perhitungan dataset, periode, serta filter yang digunakan pada dashboard.

---

## 🎨 Desain Dashboard

Dashboard menggunakan konsep desain modern dengan tampilan bersih, profesional, dan mudah digunakan.

Palet warna utama yang digunakan:

| Warna | Kode Hex |
|---|---|
| Navy | `#1E3A8A` |
| Royal Blue | `#2563EB` |
| Blue | `#1D4ED8` |
| Light Blue | `#60A5FA` |
| Background | `#F8FAFC` |
| White | `#FFFFFF` |
| Text | `#0F172A` |

Desain dibuat untuk memudahkan pengguna membaca informasi utama, memahami grafik, serta melakukan eksplorasi data dengan nyaman.

---

## 💻 Cara Menjalankan Aplikasi Secara Lokal

### 1. Persyaratan

Pastikan perangkat telah memiliki:

- Python versi 3.9 atau lebih baru.
- Git.
- Code Editor seperti Visual Studio Code.

### 2. Clone Repository

```bash
git clone https://github.com/herlindaarts/dashboard-covid19-global-uts.git
```

### 3. Masuk ke Folder Proyek

```bash
cd dashboard-covid19-global-uts
```

### 4. Instalasi Library

```bash
pip install -r requirements.txt
```

### 5. Jalankan Dashboard

```bash
python -m streamlit run app.py
```

### 6. Buka Dashboard

Setelah aplikasi berhasil dijalankan, buka browser dan akses:

```text
http://localhost:8501
```

---

## 🎯 Tujuan Proyek

Proyek ini dibuat sebagai bentuk penerapan materi Visualisasi Data, mulai dari pengumpulan dataset sekunder, pemeriksaan dan pembersihan data, pengolahan informasi, analisis data, hingga pengembangan dashboard interaktif.

Melalui proyek ini, diharapkan pengguna dapat memahami perkembangan COVID-19 global dengan lebih mudah melalui penyajian data yang terstruktur, informatif, dan interaktif.

---

**Dibuat oleh Herlinda Artika Sari**  
Program Studi D3 Manajemen Informatika  
Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data  
Tahun 2026
