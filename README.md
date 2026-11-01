# Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022

**Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data**

Dashboard interaktif untuk menganalisis perkembangan kasus COVID-19 di berbagai negara selama periode 22 Januari 2020 hingga 14 Mei 2022. Proyek ini menggunakan Python, Streamlit, Pandas, dan Plotly untuk menyajikan data epidemiologi dalam bentuk visualisasi yang informatif dan mudah dipahami.

## 🌐 Akses Dashboard

**Dashboard Online:**  
https://dashboard-covid19-global-uts-jjhjphkik97kkvgjfghbs8.streamlit.app/

**Repository GitHub:**  
https://github.com/herlindaarts/dashboard-covid19-global-uts

**Dataset Kaggle:**  
https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset

## 📌 Identitas Proyek

| Keterangan | Informasi |
|---|---|
| Judul Proyek | Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022 |
| Mata Kuliah | Visualisasi Data |
| Nama Mahasiswa | Herlinda Artika Sari |
| NIM | [241041011] |
| Bahasa Pemrograman | Python |
| Framework | Streamlit |
| Library Visualisasi | Plotly |
| Pengolahan Data | Pandas, NumPy |
| Dataset Utama | 184.787 baris data harian |
| Dataset Pendukung | 226 negara dan pemetaan benua |

## 📖 Latar Belakang

COVID-19 merupakan pandemi global yang memberikan dampak besar terhadap berbagai aspek kehidupan masyarakat. Perkembangan kasus positif, angka kematian, dan kasus aktif berbeda-beda di setiap negara dan mengalami perubahan dari waktu ke waktu.

Banyaknya data yang tersedia membutuhkan proses pengolahan dan penyajian yang tepat agar informasi lebih mudah dipahami. Oleh karena itu, proyek ini dibuat untuk menyajikan perkembangan COVID-19 global melalui dashboard interaktif.

Dashboard ini membantu pengguna melihat pola penyebaran COVID-19, membandingkan jumlah kasus antarnegara, mengetahui perkembangan kasus berdasarkan benua, serta memahami perubahan kasus dari waktu ke waktu.

## 📊 Sumber dan Deskripsi Dataset

Dataset diperoleh dari Kaggle:

**COVID-19 Global Dataset — Joseph Assaker**

Sumber data asli yang tercantum dalam dokumentasi proyek adalah Worldometer Coronavirus Tracking.

| Informasi | Keterangan |
|---|---|
| Periode Data | 22 Januari 2020 – 14 Mei 2022 |
| Jumlah Negara | 226 negara dan wilayah teritori |
| Jumlah Benua | 6 benua |
| Dataset Harian | 184.787 baris |
| Dataset Ringkasan | 226 baris |

Dataset utama berisi informasi perkembangan kasus harian, sedangkan dataset pendukung berisi data ringkasan negara dan pemetaan benua.

### Variabel yang Digunakan

- `date`: tanggal pencatatan data.
- `country`: nama negara.
- `cumulative_total_cases`: total kasus terkonfirmasi kumulatif.
- `daily_new_cases`: penambahan kasus baru harian.
- `active_cases`: jumlah kasus aktif.
- `cumulative_total_deaths`: total kematian kumulatif.
- `daily_new_deaths`: penambahan kematian harian.

## 🗂️ Struktur Direktori Proyek

```text
covid19_uts_dataset_rapi/
│
├── data/
│   ├── covid19_daily_clean.csv
│   └── covid19_summary_clean.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

Keterangan:

- `data/`: menyimpan dataset yang telah melalui proses pembersihan.
- `app.py`: program utama dashboard Streamlit.
- `requirements.txt`: daftar library Python yang dibutuhkan.
- `README.md`: dokumentasi proyek.
- `.gitignore`: mengatur file yang tidak perlu dimasukkan ke GitHub.

## 🚀 Teknologi yang Digunakan

1. **Python** — bahasa pemrograman utama.
2. **Streamlit** — framework untuk membangun dashboard interaktif.
3. **Pandas** — mengolah dan menganalisis dataset.
4. **NumPy** — membantu perhitungan numerik.
5. **Plotly** — membuat grafik dan visualisasi interaktif.

## 📈 Fitur Dashboard

### 1. KPI Metric Cards

Dashboard menyediakan empat indikator utama:

- **Total Kasus Terkonfirmasi:** menampilkan jumlah kasus COVID-19 kumulatif.
- **Total Kematian:** menampilkan jumlah kematian kumulatif.
- **Case Fatality Rate (CFR):** menunjukkan perbandingan jumlah kematian terhadap jumlah kasus terkonfirmasi.
- **Jumlah Negara Terpantau:** menunjukkan banyaknya negara yang masuk dalam filter aktif.

### 2. Visualisasi Data

Dashboard menyediakan empat jenis visualisasi utama:

**A. Line Chart — Perkembangan Kasus COVID-19**

Menampilkan perubahan jumlah kasus baru dari waktu ke waktu serta garis rata-rata bergerak selama tujuh hari (7-Day Moving Average).

**B. Area Chart — Perkembangan Kasus Aktif**

Menampilkan perubahan jumlah kasus aktif selama periode pandemi sehingga pengguna dapat melihat dinamika kasus aktif.

**C. Horizontal Bar Chart — Negara dengan Kasus Tertinggi**

Menampilkan peringkat negara berdasarkan jumlah kasus terkonfirmasi. Pengguna dapat mengatur jumlah negara yang ditampilkan melalui slider Top 5 hingga Top 25.

**D. Donut/Pie Chart — Distribusi Kasus Berdasarkan Wilayah**

Menampilkan perbandingan jumlah kasus berdasarkan benua. Ketika filter dipersempit ke satu benua, visualisasi dapat menampilkan perbandingan antarnegara di wilayah tersebut.

### 3. Filter Interaktif

Dashboard memiliki beberapa filter yang dapat digunakan untuk mengeksplorasi data:

- **Filter Rentang Tanggal:** memilih periode analisis sesuai kebutuhan.
- **Preset Periode:** memilih seluruh periode, tahun 2020, 2021, 2022, atau periode kustom.
- **Filter Benua:** memilih wilayah berdasarkan benua.
- **Filter Negara:** memilih satu atau beberapa negara tertentu.

Seluruh filter digunakan untuk memperbarui informasi dan visualisasi sesuai pilihan pengguna.

### 4. Ringkasan dan Insight

Dashboard menyediakan ringkasan analisis berdasarkan data yang dipilih, meliputi:

- Tanggal dengan lonjakan kasus harian tertinggi.
- Negara dengan jumlah kasus terkonfirmasi terbesar.
- Perbandingan tingkat fatalitas kasus (CFR).
- Perkembangan jumlah kasus aktif.
- Perubahan tren kasus berdasarkan periode yang dipilih.

### 5. Eksplorasi dan Unduh Data

Pengguna dapat melihat tabel data berdasarkan filter yang dipilih dan mengunduh data dalam format CSV untuk analisis lebih lanjut.

## 🔬 Metodologi Pengolahan Data

### 1. Penanganan Missing Values

Dalam dataset ditemukan nilai kosong pada beberapa variabel, antara lain:

- `daily_new_cases`: 10.458 nilai kosong.
- `active_cases`: 18.040 nilai kosong.
- `daily_new_deaths`: 26.937 nilai kosong.

Nilai kosong tidak langsung diganti dengan angka nol karena nilai kosong tidak selalu menunjukkan bahwa tidak ada kasus atau kematian. Penanganan dilakukan dengan mempertahankan nilai NaN agar informasi asli tidak berubah secara sembarangan.

### 2. Penanganan Nilai Negatif

Ditemukan nilai negatif pada beberapa data kasus baru dan kematian baru.

Nilai tersebut dipertahankan karena dapat mencerminkan koreksi retrospektif terhadap laporan sebelumnya. Dengan demikian, data tidak langsung dihapus hanya karena memiliki nilai negatif.

### 3. Pencegahan Visualisasi Menyesatkan

Beberapa pendekatan yang digunakan:

- Sumbu grafik batang dimulai dari angka nol agar perbandingan lebih adil.
- Penggunaan 7-Day Moving Average untuk membantu mengurangi fluktuasi pelaporan harian.
- Filter tanggal dan wilayah digunakan agar analisis dapat dilakukan secara lebih terarah.

## 💡 Temuan dan Insight Analisis

### 1. Puncak Kasus Harian

Berdasarkan grafik perkembangan kasus harian, lonjakan kasus COVID-19 global paling tinggi terlihat pada awal tahun 2022, bertepatan dengan gelombang Omicron. Pada periode tersebut, jumlah kasus harian meningkat tajam hingga mendekati 4 juta kasus sebelum mengalami penurunan.

### 2. Negara dengan Kasus Tertinggi

Berdasarkan visualisasi Bar Chart, Amerika Serikat (USA) merupakan negara dengan jumlah kasus COVID-19 terkonfirmasi tertinggi. Berdasarkan grafik, USA mencatat sekitar 71.955.193 kasus, disusul India sebanyak 38.903.731 kasus dan Brasil sebanyak 23.757.741 kasus.

### 3. Perbandingan Antarbenua

Berdasarkan visualisasi Pie Chart, Eropa memiliki kontribusi kasus terkonfirmasi terbesar, yaitu 32,2%. Selanjutnya, Asia menyumbang 27,1%, Amerika Utara 24,1%, Amerika Selatan sekitar 12,9%, Afrika 3,07%, dan Australia/Oseania 0,636%.

Hasil tersebut menunjukkan bahwa Eropa memiliki proporsi kasus terkonfirmasi paling besar dibandingkan benua lainnya.

### 4. Tingkat Fatalitas (CFR)

Berdasarkan indikator dashboard, Case Fatality Rate (CFR) tercatat sebesar 1,21%, dengan total 6.287.654 kematian dari 520.833.195 kasus terkonfirmasi. Artinya, terdapat sekitar 1,21 kematian untuk setiap 100 kasus terkonfirmasi berdasarkan rasio kumulatif tersebut.

### 5. Perkembangan Kasus Aktif

Grafik kasus aktif menunjukkan beberapa gelombang peningkatan selama pandemi. Lonjakan paling besar terlihat pada awal tahun 2022 saat gelombang Omicron, dengan jumlah kasus aktif mencapai hampir 60 juta. Setelah mencapai puncaknya, jumlah kasus aktif mengalami penurunan hingga akhir periode pengamatan.

## 🎨 Desain Dashboard

Dashboard menggunakan desain modern dengan tampilan bersih dan profesional.

Palet warna utama:

| Warna | Kode |
|---|---|
| Navy | `#1E3A8A` |
| Royal Blue | `#2563EB` |
| Blue | `#1D4ED8` |
| Light Blue | `#60A5FA` |
| Background | `#F8FAFC` |
| White | `#FFFFFF` |
| Text | `#0F172A` |

Desain dibuat agar informasi utama mudah dibaca, grafik terlihat jelas, dan pengguna dapat melakukan eksplorasi data dengan nyaman.

## 💻 Cara Menjalankan Aplikasi Secara Lokal

### 1. Persyaratan

Pastikan Python versi 3.9 atau lebih baru telah terpasang.

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

Akses alamat berikut melalui browser:

```text
http://localhost:8501
```

## 🎯 Tujuan Proyek

Proyek ini dibuat sebagai bentuk penerapan materi Visualisasi Data, mulai dari pengolahan dataset sekunder, pembersihan data, analisis informasi, pembuatan visualisasi, hingga pengembangan dashboard interaktif.

Diharapkan dashboard ini dapat membantu pengguna memahami perkembangan COVID-19 global melalui penyajian informasi yang lebih terstruktur, interaktif, dan mudah dipahami.

---

**Dibuat oleh Herlinda Artika Sari**  
**Ujian Tengah Semester — Visualisasi Data**  
**Tahun 2026**
