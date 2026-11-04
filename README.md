# 🌍 DASHBOARD ANALISIS PERKEMBANGAN COVID-19 GLOBAL TAHUN 2020–2022

### Interactive Global COVID-19 Data Analytics & Visualization Dashboard

**Proyek Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data**

Dashboard interaktif untuk menganalisis perkembangan kasus COVID-19 di berbagai negara selama periode **22 Januari 2020 hingga 14 Mei 2022**. Proyek ini dikembangkan menggunakan Python dan Streamlit dengan dukungan Pandas, NumPy, serta Plotly untuk mengolah, menganalisis, dan memvisualisasikan data COVID-19 secara informatif dan interaktif.

Dashboard ini menyajikan informasi mengenai total kasus terkonfirmasi, jumlah kematian, kasus aktif, Case Fatality Rate (CFR), serta perbandingan perkembangan COVID-19 antarnegara dan benua.

---

## 👩‍🎓 1. IDENTITAS MAHASISWA & AKADEMIK

| Keterangan | Informasi |
|---|---|
| Nama | HERLINDA ARTIKA SARI |
| NIM | 241041011 |
| Program Studi | D3 Manajemen Informatika |
| Mata Kuliah | Visualisasi Data |
| Semester | 5 |
| Jenis Proyek | Ujian Tengah Semester (UTS) |
| Tahun | 2026 |

---

## 📌 2. DESKRIPSI PROYEK

COVID-19 merupakan pandemi global yang memberikan dampak besar terhadap berbagai aspek kehidupan masyarakat. Penyebaran virus yang terjadi di berbagai negara menghasilkan data dalam jumlah besar dan terus mengalami perubahan dari waktu ke waktu.

Melalui proyek ini, data COVID-19 diolah menjadi dashboard visualisasi interaktif untuk membantu pengguna memahami perkembangan pandemi berdasarkan waktu, negara, dan benua.

**Tujuan pengembangan dashboard:**

- Menampilkan perkembangan kasus COVID-19 secara global.
- Menganalisis perubahan jumlah kasus harian dan kumulatif.
- Membandingkan jumlah kasus antarnegara.
- Mengetahui distribusi kasus berdasarkan benua.
- Menganalisis hubungan antara jumlah kasus dan kematian melalui CFR.
- Menyajikan informasi melalui visualisasi data yang mudah dipahami.

### Informasi Dataset

| Informasi | Keterangan |
|---|---|
| Sumber Dataset | Kaggle |
| Periode Data | 22 Januari 2020 – 14 Mei 2022 |
| Jumlah Negara/Wilayah | 226 |
| Jumlah Benua | 6 |
| Jumlah Baris Data Harian | 184.787 |
| Jumlah Baris Data Ringkasan | 226 |
| Format Data | CSV |

**Sumber dataset:**

https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset

---

## 📊 3. FITUR UTAMA DASHBOARD

Dashboard dikembangkan dengan tampilan modern bertema navy dan dilengkapi berbagai fitur analisis data.

### A. Global Overview — Indikator Utama

Dashboard menampilkan empat indikator utama dalam bentuk KPI Cards:

1. **Total Confirmed Cases** — Jumlah keseluruhan kasus COVID-19 terkonfirmasi.
2. **Total Deaths** — Jumlah keseluruhan kematian akibat COVID-19.
3. **Case Fatality Rate (CFR)** — Persentase kematian dibandingkan dengan jumlah kasus terkonfirmasi.
4. **Countries Monitored** — Jumlah negara atau wilayah yang tercakup dalam dataset.

### B. Interactive Data Visualization

Dashboard menyediakan empat visualisasi utama:

**1. Global Daily Cases Trend**

Grafik garis untuk memperlihatkan perkembangan kasus baru COVID-19 setiap hari. Dilengkapi dengan 7-Day Moving Average untuk membantu melihat kecenderungan tren dengan lebih jelas. Pengguna juga dapat memilih tampilan kasus harian atau kumulatif.

**2. Global Active Cases Trend**

Grafik area untuk menggambarkan perubahan jumlah kasus aktif COVID-19 selama periode pengamatan.

**3. Top Countries by Confirmed Cases**

Grafik batang horizontal untuk membandingkan negara dengan jumlah kasus terkonfirmasi tertinggi. Pengguna dapat mengatur jumlah negara yang ditampilkan melalui pilihan Top 5 hingga Top 25.

**4. COVID-19 Cases Distribution by Continent**

Grafik donat atau pie untuk memperlihatkan distribusi kasus COVID-19 berdasarkan enam benua. Pengguna juga dapat melihat perbandingan negara ketika memilih benua tertentu.

### C. Interactive Filters

Dashboard menyediakan beberapa filter untuk mempermudah analisis:

- **Date Range:** Memilih rentang tanggal pengamatan.
- **Period Selection:** Memilih periode keseluruhan, tahun 2020, 2021, 2022, atau periode khusus.
- **Continent Filter:** Memilih benua yang ingin dianalisis.
- **Country Filter:** Memilih satu atau beberapa negara untuk dibandingkan.

### D. Analytical Summary

Dashboard juga menyajikan ringkasan hasil analisis, seperti:

- Tanggal dengan lonjakan kasus harian tertinggi.
- Negara dengan jumlah kasus terkonfirmasi terbanyak.
- Perbandingan tingkat CFR.
- Perubahan tren kasus aktif.
- Perkembangan kasus berdasarkan periode pengamatan.

### E. Export Data

Pengguna dapat mengunduh data dalam format CSV untuk mendukung pengolahan dan analisis lebih lanjut.

---

## 🔎 4. KEY ANALYTICAL INSIGHTS

Bagian ini menyajikan lima fokus analisis utama berdasarkan dataset COVID-19 global.

**1. Lonjakan Kasus COVID-19 Global**

Perkembangan kasus harian menunjukkan adanya periode peningkatan dan penurunan jumlah kasus selama pandemi. Salah satu periode yang perlu diperhatikan adalah awal tahun 2022, ketika peningkatan kasus terjadi seiring penyebaran varian Omicron.

**Insight:** Perubahan kasus harian dapat digunakan untuk mengidentifikasi periode lonjakan penyebaran COVID-19 dan memahami dinamika pandemi.

**2. Negara dengan Jumlah Kasus Tertinggi**

Analisis perbandingan antarnegara digunakan untuk mengetahui negara dengan jumlah kasus terkonfirmasi tertinggi selama periode pengamatan.

Negara yang menjadi perhatian dalam analisis ini meliputi:

- Amerika Serikat (USA)
- India
- Brasil (Brazil)

**Insight:** Perbandingan antarnegara membantu memperlihatkan perbedaan skala penyebaran COVID-19 di berbagai wilayah dunia.

**3. Distribusi Kasus Berdasarkan Benua**

Data COVID-19 dikelompokkan ke dalam enam benua untuk mengetahui distribusi kasus secara geografis:

- Asia
- Eropa
- Amerika Utara
- Amerika Selatan
- Afrika
- Australia/Oseania

**Insight:** Distribusi berdasarkan benua memberikan gambaran mengenai persebaran kasus dan perbedaan jumlah kasus antarwilayah.

**4. Analisis Case Fatality Rate (CFR)**

Case Fatality Rate digunakan untuk mengetahui perbandingan jumlah kematian terhadap jumlah kasus terkonfirmasi.

Rumus:

CFR = (Total Kematian / Total Kasus Terkonfirmasi) × 100%

**Insight:** CFR membantu memberikan gambaran mengenai proporsi kematian pada kasus COVID-19 yang tercatat. Nilai ini tidak secara langsung menunjukkan risiko kematian individu karena dipengaruhi oleh berbagai faktor, termasuk pengujian dan pelaporan kasus.

**5. Perkembangan Kasus Aktif**

Kasus aktif digunakan untuk melihat jumlah kasus yang masih tercatat aktif pada suatu periode berdasarkan data yang tersedia.

**Insight:** Perubahan jumlah kasus aktif dapat membantu mengidentifikasi periode ketika beban kasus meningkat atau menurun.

> Catatan: Lima bagian di atas merupakan fokus analisis. Angka, tanggal puncak, persentase, dan peringkat negara perlu dicocokkan kembali dengan hasil pengolahan dataset sebelum dijadikan kesimpulan statistik final. Hindari menganggap uraian tren sebagai angka hasil perhitungan yang sudah tervalidasi.

---

## 🛠️ 5. TEKNOLOGI & LIBRARY

Proyek ini dikembangkan menggunakan beberapa teknologi dan pustaka Python.

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Streamlit | Framework untuk membangun dashboard interaktif |
| Pandas | Pengolahan dan manipulasi data |
| NumPy | Operasi numerik dan perhitungan statistik |
| Plotly | Pembuatan grafik dan visualisasi interaktif |
| CSV | Format penyimpanan dataset |
| GitHub | Penyimpanan dan pengelolaan source code |
| Streamlit Community Cloud | Deployment dashboard secara online |

---

## 📁 6. STRUKTUR DIREKTORI

Struktur proyek yang digunakan:

```text
dashboard-covid19-global-uts/
│
├── data/
│   ├── covid19_daily_clean.csv
│   └── covid19_summary_clean.csv
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

**Keterangan:**

- `data/` : Menyimpan dataset COVID-19 yang telah melalui proses pengolahan.
- `covid19_daily_clean.csv` : Dataset perkembangan COVID-19 harian.
- `covid19_summary_clean.csv` : Dataset ringkasan COVID-19 berdasarkan negara.
- `app.py` : File utama yang menjalankan dashboard Streamlit.
- `requirements.txt` : Daftar library Python yang dibutuhkan.
- `README.md` : Dokumentasi proyek.

---

## 🧹 7. METODOLOGI DATA CLEANING & PREPROCESSING

Sebelum digunakan dalam dashboard, dataset COVID-19 melalui beberapa tahapan pengolahan data.

### A. Data Cleaning

Tahapan pembersihan data meliputi:

- Memeriksa struktur dan tipe data setiap kolom.
- Mengubah kolom tanggal ke format datetime.
- Memeriksa data kosong atau missing values.
- Memeriksa kemungkinan data duplikat.
- Memeriksa nilai negatif pada kasus harian.
- Menyesuaikan format data agar dapat digunakan dalam visualisasi.

### B. Missing Values

Beberapa variabel memiliki nilai kosong, antara lain:

| Variabel | Jumlah Missing Values |
|---|---:|
| Daily New Cases | 10.458 |
| Active Cases | 18.040 |
| Daily New Deaths | 26.937 |

Nilai kosong tidak secara otomatis diganti dengan angka nol karena nilai kosong belum tentu berarti tidak terdapat kasus. Penggunaan nilai nol tanpa dasar dapat menghasilkan interpretasi yang keliru.

### C. Penanganan Nilai Negatif

Nilai negatif pada data kasus harian dapat muncul akibat koreksi atau penyesuaian laporan historis dari sumber data.

Oleh karena itu, nilai negatif tidak langsung dihapus atau diubah menjadi nol tanpa mempertimbangkan konteks data.

### D. Data Preprocessing

Tahapan preprocessing meliputi:

- Pengelompokan data berdasarkan tanggal.
- Pengelompokan data berdasarkan negara dan benua.
- Pengolahan data harian dan kumulatif.
- Perhitungan indikator statistik.
- Perhitungan 7-Day Moving Average.
- Penyiapan data untuk kebutuhan visualisasi.

---

## 💻 8. CARA MENJALANKAN PROYEK SECARA LOKAL

Ikuti langkah berikut untuk menjalankan dashboard pada komputer.

### A. Clone Repository

```bash
git clone https://github.com/herlindaarts/dashboard-covid19-global-uts.git
```

### B. Masuk ke Folder Proyek

```bash
cd dashboard-covid19-global-uts
```

### C. Install Library

```bash
pip install -r requirements.txt
```

### D. Jalankan Dashboard

```bash
python -m streamlit run app.py
```

### E. Buka Dashboard

Setelah aplikasi berhasil dijalankan, buka alamat berikut melalui browser:

```text
http://localhost:8501
```

---

## 🚀 9. GITHUB & STREAMLIT DEPLOYMENT

Proyek ini disimpan pada GitHub dan dipublikasikan menggunakan Streamlit Community Cloud.

### GitHub Repository

Source code dan dokumentasi proyek dapat diakses melalui:

https://github.com/herlindaarts/dashboard-covid19-global-uts

### Streamlit Dashboard

Dashboard dapat diakses secara online melalui:

https://dashboard-covid19-global-uts-jjhjphkik97kkvgjfghbs8.streamlit.app/

### Teknologi Deployment

- GitHub digunakan untuk menyimpan source code.
- Streamlit Community Cloud digunakan untuk menjalankan dashboard secara online.
- `requirements.txt` digunakan untuk memasang library yang dibutuhkan saat deployment.

---

## 🖥️ 10. DASHBOARD PREVIEW

Dashboard dapat diakses dan digunakan secara langsung melalui tautan berikut:

**[🌐 Buka Dashboard Analisis COVID-19 Global](https://dashboard-covid19-global-uts-jjhjphkik97kkvgjfghbs8.streamlit.app/)**

Fitur yang dapat dieksplorasi:

- Melihat indikator utama perkembangan COVID-19.
- Mengamati tren kasus harian dan kumulatif.
- Membandingkan jumlah kasus antarnegara.
- Melihat distribusi kasus berdasarkan benua.
- Mengubah rentang tanggal dan filter analisis.
- Mengunduh data dalam format CSV.

---

## 📚 11. LICENSE & DATA SOURCE

### Data Source

Dataset yang digunakan dalam proyek ini berasal dari Kaggle:

**COVID-19 Global Dataset**

https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset

Dataset digunakan sebagai sumber data untuk pengolahan, analisis, dan visualisasi perkembangan COVID-19 global.

### License

Proyek ini dibuat untuk memenuhi tugas akademik Ujian Tengah Semester (UTS) Mata Kuliah Visualisasi Data.

Seluruh hak atas dataset tetap mengikuti ketentuan lisensi dan atribusi dari sumber dataset aslinya.

---

**Dibuat oleh HERLINDA ARTIKA SARI**

D3 Manajemen Informatika

**UTS — Visualisasi Data | 2026**

*Global COVID-19 Data Analytics & Visualization Dashboard*
