"""
Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022
Ujian Tengah Semester (UTS) - Mata Kuliah Visualisasi Data
Penyusun: HERLINDA ARTIKA SARI (NIM: 241041011) - D3 Manajemen Informatika
Teknologi: Python, Streamlit, Pandas, Plotly
"""

from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ==============================================================================
# 1. KONFIGURASI HALAMAN & TEMA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="COVID-19 Global Analytics (2020–2022) | UTS Visdat",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS: Tema Clean Corporate / Medical (Deep Navy, Slate Grey, Crisp White)
st.markdown(
    """
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Settings */
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Hide default Streamlit padding on top slightly for a cleaner look */
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 2.5rem;
    }

    /* Hero Header Card (Medical & Corporate Deep Navy) */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 55%, #1D4ED8 100%);
        border-radius: 18px;
        padding: 30px 36px;
        color: #FFFFFF;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.35);
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hero-container::after {
        content: "";
        position: absolute;
        top: -40px;
        right: -40px;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, rgba(255, 255, 255, 0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-title {
        font-size: 1.95rem;
        font-weight: 800;
        margin-bottom: 6px;
        letter-spacing: -0.025em;
        line-height: 1.25;
        color: #FFFFFF;
    }
    .hero-subtitle {
        font-size: 0.98rem;
        color: #E2E8F0;
        line-height: 1.55;
        max-width: 980px;
        margin-bottom: 14px;
    }
    .hero-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        align-items: center;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.14);
        backdrop-filter: blur(8px);
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #F8FAFC;
        border: 1px solid rgba(255, 255, 255, 0.22);
    }
    .hero-badge-highlight {
        background: #2563EB;
        color: #FFFFFF;
        border: 1px solid #60A5FA;
    }

    /* Student Identity Card in Sidebar */
    .student-card {
        background: linear-gradient(145deg, #0F172A 0%, #1E293B 100%);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 18px 20px;
        color: #F8FAFC;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    }
    .student-badge-role {
        display: inline-block;
        background: #2563EB;
        color: #FFFFFF;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .student-name {
        font-size: 1.05rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 4px;
        letter-spacing: -0.01em;
    }
    .student-meta {
        font-size: 0.8rem;
        color: #94A3B8;
        line-height: 1.45;
    }
    .student-meta strong {
        color: #E2E8F0;
    }

    /* Sidebar Section Headers */
    .sidebar-section-title {
        font-size: 0.86rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #475569;
        letter-spacing: 0.06em;
        margin-top: 14px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* KPI Cards (Modern Corporate / Medical Accent Styling) */
    .kpi-wrapper {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 22px 20px;
        box-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.06), 0 1px 3px rgba(15, 23, 42, 0.04);
        border: 1px solid #E2E8F0;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }
    .kpi-wrapper:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px -4px rgba(15, 23, 42, 0.12);
    }
    .kpi-indicator-bar {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
    }
    
    /* Distinct Colors for KPI Cards */
    .kpi-blue {
        border-top: 4px solid #2563EB;
        background: linear-gradient(180deg, rgba(37, 99, 235, 0.035) 0%, #FFFFFF 35%);
    }
    .kpi-red {
        border-top: 4px solid #E11D48;
        background: linear-gradient(180deg, rgba(225, 29, 72, 0.035) 0%, #FFFFFF 35%);
    }
    .kpi-amber {
        border-top: 4px solid #D97706;
        background: linear-gradient(180deg, rgba(217, 119, 6, 0.035) 0%, #FFFFFF 35%);
    }
    .kpi-teal {
        border-top: 4px solid #0D9488;
        background: linear-gradient(180deg, rgba(13, 148, 136, 0.035) 0%, #FFFFFF 35%);
    }

    .kpi-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
    }
    .kpi-title {
        font-size: 0.8rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-icon-pill {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
    }
    .kpi-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.15;
        letter-spacing: -0.02em;
        margin-bottom: 8px;
    }
    .kpi-subtext-pill {
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 600;
        border-radius: 6px;
        padding: 3px 8px;
    }
    .pill-blue {
        background: #EFF6FF;
        color: #1D4ED8;
    }
    .pill-red {
        background: #FFF1F2;
        color: #BE123C;
    }
    .pill-amber {
        background: #FFFBEB;
        color: #B45309;
    }
    .pill-teal {
        background: #F0FDFA;
        color: #0F766E;
    }

    /* Chart Box Containers */
    .chart-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 22px 22px 14px 22px;
        box-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.05);
        margin-bottom: 20px;
        transition: box-shadow 0.2s ease;
    }
    .chart-box:hover {
        box-shadow: 0 8px 20px -2px rgba(15, 23, 42, 0.08);
    }
    .chart-header {
        margin-bottom: 12px;
    }
    .chart-title {
        font-size: 1.05rem;
        font-weight: 750;
        color: #0F172A;
        letter-spacing: -0.015em;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .chart-desc {
        font-size: 0.82rem;
        color: #64748B;
        line-height: 1.45;
    }

    /* Insight Box (Medical & Corporate Alert) */
    .insight-box {
        background: linear-gradient(135deg, #F0FDF4 0%, #EFF6FF 100%);
        border-left: 5px solid #2563EB;
        border-radius: 0 14px 14px 0;
        padding: 22px 26px;
        margin: 22px 0;
        border-top: 1px solid #DBEAFE;
        border-right: 1px solid #DBEAFE;
        border-bottom: 1px solid #DBEAFE;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.06);
    }
    .insight-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .insight-item {
        font-size: 0.89rem;
        color: #1E293B;
        line-height: 1.65;
        margin-bottom: 8px;
    }

    /* Academic Footer */
    .academic-footer {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 20px 24px;
        margin-top: 28px;
        color: #64748B;
        font-size: 0.82rem;
        text-align: center;
        line-height: 1.6;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
    }
    .academic-footer strong {
        color: #0F172A;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def safe_plotly_chart(fig):
    """Fungsi pembungkus render plotly chart untuk kompatibilitas lintas versi Streamlit."""
    try:
        st.plotly_chart(fig, width="stretch")
    except TypeError:
        st.plotly_chart(fig, use_container_width=True)


def safe_dataframe(df):
    """Fungsi pembungkus render dataframe untuk kompatibilitas lintas versi Streamlit."""
    try:
        st.dataframe(df, width="stretch")
    except TypeError:
        st.dataframe(df, use_container_width=True)


# ==============================================================================
# 2. RESOLUSI PATH & PEMBACAAN DATASET
# ==============================================================================
def resolve_data_path(filename: str) -> Path:
    """Mencari file dataset di berbagai kemungkinan direktori secara otomatis."""
    candidates = [
        Path("data") / filename,
        Path(__file__).resolve().parent / "data" / filename,
        Path(__file__).resolve().parent / "covid19_uts_dataset_rapi" / "data" / filename,
        Path.cwd() / "data" / filename,
        Path.cwd() / "covid19_uts_dataset_rapi" / "data" / filename,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"File dataset '{filename}' tidak ditemukan di folder data.")


@st.cache_data(show_spinner=True)
def load_datasets():
    """
    Membaca dataset utama (covid19_daily_clean.csv) dan pendukung (covid19_summary_clean.csv).
    Menghubungkan data benua ke dataset harian untuk kebutuhan segmentasi regional.
    """
    daily_file = resolve_data_path("covid19_daily_clean.csv")
    summary_file = resolve_data_path("covid19_summary_clean.csv")

    df_daily = pd.read_csv(daily_file)
    df_daily["date"] = pd.to_datetime(df_daily["date"])

    df_summary = pd.read_csv(summary_file)

    # Pemetaan negara -> benua
    continent_map = df_summary.set_index("country")["continent"].to_dict()
    df_daily["continent"] = df_daily["country"].map(continent_map).fillna("Lainnya")

    return df_daily, df_summary


try:
    df_daily, df_summary = load_datasets()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()

# ==============================================================================
# 3. SIDEBAR: IDENTITAS MAHASISWA & FILTER INTERAKTIF
# ==============================================================================

# Kartu Identitas Mahasiswa di Sidebar
st.sidebar.markdown(
    """
    <div class="student-card">
        <span class="student-badge-role">UTS Visualisasi Data</span>
        <div class="student-name">HERLINDA ARTIKA SARI</div>
        <div class="student-meta">
            NIM: <strong>241041011</strong><br>
            Prodi: <strong>D3 Manajemen Informatika</strong><br>
            Tahun Ajaran: <strong>2026/2027</strong>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

min_dataset_date = df_daily["date"].min().date()
max_dataset_date = df_daily["date"].max().date()

# SECTION 1: FILTER RENTANG WAKTU
st.sidebar.markdown(
    """
    <div class="sidebar-section-title">
        <span>📅 1. Rentang Waktu Analisis</span>
    </div>
    """,
    unsafe_allow_html=True,
)

preset_option = st.sidebar.selectbox(
    "Pilihan Periode Cepat:",
    options=[
        "Seluruh Periode (2020 - 2022)",
        "Tahun 2020 (Awal Pandemi Global)",
        "Tahun 2021 (Gelombang Alpha & Delta)",
        "Tahun 2022 (Gelombang Omicron)",
        "Kustom (Pilih Bebas)",
    ],
    index=0,
)

if preset_option == "Tahun 2020 (Awal Pandemi Global)":
    default_start = pd.to_datetime("2020-01-22").date()
    default_end = pd.to_datetime("2020-12-31").date()
elif preset_option == "Tahun 2021 (Gelombang Alpha & Delta)":
    default_start = pd.to_datetime("2021-01-01").date()
    default_end = pd.to_datetime("2021-12-31").date()
elif preset_option == "Tahun 2022 (Gelombang Omicron)":
    default_start = pd.to_datetime("2022-01-01").date()
    default_end = max_dataset_date
else:
    default_start = min_dataset_date
    default_end = max_dataset_date

# Date Input interaktif
date_range = st.sidebar.date_input(
    "Tentukan Rentang Tanggal:",
    value=(default_start, default_end),
    min_value=min_dataset_date,
    max_value=max_dataset_date,
    key=f"date_selector_{preset_option}",
)

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start_date, end_date = date_range
    if start_date > end_date:
        st.sidebar.error("Tanggal awal tidak boleh melebihi tanggal akhir!")
        st.stop()
else:
    start_date = default_start
    end_date = default_end

st.sidebar.markdown("<hr style='margin: 14px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)

# SECTION 2: FILTER WILAYAH & NEGARA
st.sidebar.markdown(
    """
    <div class="sidebar-section-title">
        <span>🌍 2. Filter Wilayah & Negara</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Filter Benua
all_continents = sorted(df_daily["continent"].unique().tolist())
selected_continents = st.sidebar.multiselect(
    "Filter Berdasarkan Benua:",
    options=all_continents,
    default=all_continents,
    help="Pilih satu atau beberapa benua untuk memfilter daftar negara.",
)

if not selected_continents:
    selected_continents = all_continents

# Daftar negara yang tersedia sesuai benua terpilih
available_countries = sorted(
    df_daily[df_daily["continent"].isin(selected_continents)]["country"].unique().tolist()
)

select_all_countries = st.sidebar.checkbox(
    "Pilih Semua Negara yang Tersedia",
    value=True,
    help="Centang untuk menyertakan seluruh negara pada benua yang dipilih.",
)

if select_all_countries:
    selected_countries = available_countries
else:
    selected_countries = st.sidebar.multiselect(
        "Pilih Negara Tertentu:",
        options=available_countries,
        default=available_countries[:5] if len(available_countries) >= 5 else available_countries,
        help="Pilih satu atau lebih negara spesifik untuk perbandingan mendalam.",
    )

if not selected_countries:
    st.warning("Silakan pilih minimal satu negara pada sidebar filter untuk menampilkan visualisasi.")
    st.stop()

# Info Box Sumber Data di Sidebar
with st.sidebar.expander("ℹ️ Sumber & Integritas Data", expanded=False):
    st.markdown(
        """
        - **Sumber:** [Kaggle COVID-19 Global Dataset](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset)
        - **Data Asli:** Worldometer Coronavirus Tracking
        - **Rentang Asli:** 22 Jan 2020 – 14 Mei 2022
        - **Total Cakupan:** 226 Negara/Wilayah
        - **Missing Values:** Nilai kosong (`NaN`) dipertahankan sesuai format aslinya tanpa imputasi nol sembarangan.
        - **Nilai Negatif:** Merefleksikan koreksi data retrospektif resmi dari otoritas kesehatan dunia.
        """
    )

# ==============================================================================
# 4. FILTERING & AGREGASI DATA
# ==============================================================================
mask_date = (df_daily["date"].dt.date >= start_date) & (df_daily["date"].dt.date <= end_date)
mask_country = df_daily["country"].isin(selected_countries)
df_filtered = df_daily[mask_date & mask_country].copy()

if df_filtered.empty:
    st.error("Tidak ada data yang ditemukan untuk kombinasi tanggal dan negara yang dipilih.")
    st.stop()

# Mengambil status terakhir yang valid per negara dalam rentang waktu yang dipilih
latest_per_country = df_filtered.sort_values("date").groupby("country").last().reset_index()

total_confirmed_cases = latest_per_country["cumulative_total_cases"].sum()
total_deaths = latest_per_country["cumulative_total_deaths"].sum()
active_cases_latest = latest_per_country["active_cases"].sum(skipna=True)
count_countries = len(selected_countries)

# Penambahan kasus dan kematian baru selama periode
total_new_cases_period = df_filtered["daily_new_cases"].sum(skipna=True)
total_new_deaths_period = df_filtered["daily_new_deaths"].sum(skipna=True)

# Case Fatality Rate (CFR)
cfr_rate = (total_deaths / total_confirmed_cases * 100) if total_confirmed_cases > 0 else 0.0

# ==============================================================================
# 5. HERO HEADER DASHBOARD (Corporate & Academic Styling)
# ==============================================================================
st.markdown(
    f"""
    <div class="hero-container">
        <div class="hero-title">Dashboard Analisis Perkembangan COVID-19 Global (2020–2022)</div>
        <div class="hero-subtitle">
            Platform intelijen data komprehensif untuk mengevaluasi dinamika kasus terkonfirmasi, mortalitas global, 
            beban kasus aktif, serta perbandingan epidemiologi lintas wilayah berdasarkan data resmi Worldometer.
        </div>
        <div class="hero-badges">
            <span class="hero-badge hero-badge-highlight">🩺 Visualisasi Data</span>
            <span class="hero-badge">📅 Periode: {start_date.strftime('%d %b %Y')} – {end_date.strftime('%d %b %Y')}</span>
            <span class="hero-badge">🌐 Cakupan: {count_countries:,} Negara Terpilih</span>
            <span class="hero-badge">👤 HERLINDA ARTIKA SARI (241041011)</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. KPI METRIC CARDS (Clean Corporate & Medical Accent)
# ==============================================================================
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(
        f"""
        <div class="kpi-wrapper kpi-blue">
            <div>
                <div class="kpi-header">
                    <span class="kpi-title">Total Terkonfirmasi</span>
                    <div class="kpi-icon-pill" style="background: #EFF6FF; color: #2563EB;">🦠</div>
                </div>
                <div class="kpi-value">{total_confirmed_cases:,.0f}</div>
            </div>
            <div>
                <span class="kpi-subtext-pill pill-blue">+{total_new_cases_period:,.0f} kasus pada periode ini</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col2:
    st.markdown(
        f"""
        <div class="kpi-wrapper kpi-red">
            <div>
                <div class="kpi-header">
                    <span class="kpi-title">Total Kematian</span>
                    <div class="kpi-icon-pill" style="background: #FFF1F2; color: #E11D48;">✝️</div>
                </div>
                <div class="kpi-value" style="color: #BE123C;">{total_deaths:,.0f}</div>
            </div>
            <div>
                <span class="kpi-subtext-pill pill-red">+{total_new_deaths_period:,.0f} kematian pada periode ini</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col3:
    st.markdown(
        f"""
        <div class="kpi-wrapper kpi-amber">
            <div>
                <div class="kpi-header">
                    <span class="kpi-title">Case Fatality Rate (CFR)</span>
                    <div class="kpi-icon-pill" style="background: #FFFBEB; color: #D97706;">⚠️</div>
                </div>
                <div class="kpi-value" style="color: #B45309;">{cfr_rate:.2f}%</div>
            </div>
            <div>
                <span class="kpi-subtext-pill pill-amber">Rasio kematian kumulatif terhadap kasus</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col4:
    st.markdown(
        f"""
        <div class="kpi-wrapper kpi-teal">
            <div>
                <div class="kpi-header">
                    <span class="kpi-title">Negara Terpantau</span>
                    <div class="kpi-icon-pill" style="background: #F0FDFA; color: #0D9488;">🌐</div>
                </div>
                <div class="kpi-value" style="color: #0F766E;">{count_countries:,}</div>
            </div>
            <div>
                <span class="kpi-subtext-pill pill-teal">Dari total 226 negara dalam basis data</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# 7. VISUALISASI UTAMA (Minimal 4 Jenis Visualisasi Berbeda)
# ==============================================================================

# Agregasi harian untuk deret waktu
timeline_df = (
    df_filtered.groupby("date")
    .agg(
        {
            "daily_new_cases": "sum",
            "cumulative_total_cases": "sum",
            "active_cases": "sum",
            "daily_new_deaths": "sum",
        }
    )
    .reset_index()
)

# Menghitung Moving Average 7 Hari
timeline_df["cases_7d_ma"] = timeline_df["daily_new_cases"].rolling(window=7, min_periods=1).mean()

# BARIS 1: Line Chart & Area Chart
col_vis1, col_vis2 = st.columns([1, 1])

# ------------------------------------------------------------------------------
# VISUALISASI 1: Line Chart Perkembangan Kasus dari Waktu ke Waktu
# ------------------------------------------------------------------------------
with col_vis1:
    st.markdown(
        """
        <div class="chart-box">
            <div class="chart-header">
                <div class="chart-title">📈 1. Tren Perkembangan Kasus dari Waktu ke Waktu</div>
                <div class="chart-desc">Fluktuasi harian dan kurva 7-Day Moving Average untuk menganalisis puncak gelombang transmisi.</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    line_metric = st.radio(
        "Pilih Metrik Visualisasi Tren:",
        options=["Kasus Baru Harian (+ 7-Day MA)", "Kasus Kumulatif Terkonfirmasi"],
        horizontal=True,
        key="radio_line_metric",
    )

    fig_line = go.Figure()

    if line_metric == "Kasus Baru Harian (+ 7-Day MA)":
        fig_line.add_trace(
            go.Scatter(
                x=timeline_df["date"],
                y=timeline_df["daily_new_cases"],
                mode="lines",
                name="Kasus Harian",
                line=dict(color="#93C5FD", width=1.2),
                opacity=0.60,
                hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kasus Harian:</b> %{y:,.0f}<extra></extra>",
            )
        )
        fig_line.add_trace(
            go.Scatter(
                x=timeline_df["date"],
                y=timeline_df["cases_7d_ma"],
                mode="lines",
                name="7-Day Moving Average",
                line=dict(color="#1D4ED8", width=3),
                hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>7-Day MA:</b> %{y:,.0f}<extra></extra>",
            )
        )
        y_axis_label = "Kasus Baru Harian"
    else:
        fig_line.add_trace(
            go.Scatter(
                x=timeline_df["date"],
                y=timeline_df["cumulative_total_cases"],
                mode="lines",
                name="Total Kasus Kumulatif",
                line=dict(color="#0F172A", width=3.2),
                fill="tozeroy",
                fillcolor="rgba(15, 23, 42, 0.05)",
                hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kumulatif:</b> %{y:,.0f}<extra></extra>",
            )
        )
        y_axis_label = "Total Kasus Kumulatif"

    fig_line.update_layout(
        template="plotly_white",
        height=385,
        margin=dict(l=15, r=15, t=10, b=15),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(
            title="",
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
        ),
        yaxis=dict(
            title=y_axis_label,
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
            tickformat=",.0f",
        ),
        hovermode="x unified",
    )
    safe_plotly_chart(fig_line)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# VISUALISASI 2: Area Chart Perkembangan Kasus Aktif
# ------------------------------------------------------------------------------
with col_vis2:
    st.markdown(
        """
        <div class="chart-box">
            <div class="chart-header">
                <div class="chart-title">🌊 2. Dinamika Kasus Aktif (Active Cases)</div>
                <div class="chart-desc">Beban pasien dalam perawatan atau isolasi aktif sepanjang rentang waktu terpilih.</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    fig_area = go.Figure()
    fig_area.add_trace(
        go.Scatter(
            x=timeline_df["date"],
            y=timeline_df["active_cases"],
            mode="lines",
            name="Kasus Aktif",
            line=dict(color="#0284C7", width=2.4),
            fill="tozeroy",
            fillcolor="rgba(2, 132, 199, 0.20)",
            hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kasus Aktif:</b> %{y:,.0f}<extra></extra>",
        )
    )

    fig_area.update_layout(
        template="plotly_white",
        height=430,
        margin=dict(l=15, r=15, t=10, b=15),
        xaxis=dict(
            title="",
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
        ),
        yaxis=dict(
            title="Jumlah Pasien Aktif",
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
            tickformat=",.0f",
        ),
        hovermode="x",
    )
    safe_plotly_chart(fig_area)
    st.markdown("</div>", unsafe_allow_html=True)


# BARIS 2: Bar Chart & Pie Chart
col_vis3, col_vis4 = st.columns([1, 1])

# ------------------------------------------------------------------------------
# VISUALISASI 3: Bar Chart Negara dengan Kasus Tertinggi
# ------------------------------------------------------------------------------
with col_vis3:
    st.markdown(
        """
        <div class="chart-box">
            <div class="chart-header">
                <div class="chart-title">📊 3. Peringkat Negara Kasus Tertinggi (Top Ranking)</div>
                <div class="chart-desc">Perbandingan akumulasi kasus terkonfirmasi terbesar dalam filter yang aktif.</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    top_n = st.slider(
        "Tampilkan Jumlah Negara Teratas:",
        min_value=5,
        max_value=min(25, max(5, count_countries)),
        value=min(10, count_countries),
        step=1,
        key="slider_top_n",
    )

    top_countries_df = (
        latest_per_country.nlargest(top_n, "cumulative_total_cases")
        .sort_values("cumulative_total_cases", ascending=True)
    )

    fig_bar = go.Figure(
        go.Bar(
            x=top_countries_df["cumulative_total_cases"],
            y=top_countries_df["country"],
            orientation="h",
            marker=dict(
                color=top_countries_df["cumulative_total_cases"],
                colorscale=[
                    [0.0, "#93C5FD"],
                    [0.4, "#3B82F6"],
                    [1.0, "#0F172A"],
                ],
                showscale=False,
            ),
            text=top_countries_df["cumulative_total_cases"].apply(lambda v: f"{v:,.0f}"),
            textposition="auto",
            hovertemplate="<b>Negara:</b> %{y}<br><b>Kasus Terkonfirmasi:</b> %{x:,.0f}<extra></extra>",
        )
    )

    fig_bar.update_layout(
        template="plotly_white",
        height=410,
        margin=dict(l=15, r=15, t=10, b=15),
        xaxis=dict(
            title="Total Kasus Terkonfirmasi",
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
            tickformat=",.0f",
        ),
        yaxis=dict(
            title="",
            linecolor="#CBD5E1",
        ),
    )
    safe_plotly_chart(fig_bar)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# VISUALISASI 4: Pie / Donut Chart Perbandingan Kasus Berdasarkan Benua / Negara
# ------------------------------------------------------------------------------
with col_vis4:
    st.markdown(
        """
        <div class="chart-box">
            <div class="chart-header">
                <div class="chart-title">🍩 4. Proporsi Kasus Berdasarkan Wilayah / Benua</div>
                <div class="chart-desc">Persentase kontribusi kasus terkonfirmasi antar benua atau negara terpilih.</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    if len(selected_continents) > 1 and count_countries > 8:
        dist_df = (
            latest_per_country.groupby("continent")["cumulative_total_cases"]
            .sum()
            .reset_index()
            .sort_values("cumulative_total_cases", ascending=False)
        )
        cat_column = "continent"
    else:
        sorted_countries = latest_per_country.sort_values("cumulative_total_cases", ascending=False)
        if len(sorted_countries) > 8:
            top8 = sorted_countries.head(8)[["country", "cumulative_total_cases"]]
            others_sum = sorted_countries.iloc[8:]["cumulative_total_cases"].sum()
            others_row = pd.DataFrame([{"country": "Lainnya", "cumulative_total_cases": others_sum}])
            dist_df = pd.concat([top8, others_row], ignore_index=True)
        else:
            dist_df = sorted_countries[["country", "cumulative_total_cases"]]
        cat_column = "country"

    custom_colors = [
        "#0F172A", "#1E3A8A", "#2563EB", "#0284C7",
        "#0D9488", "#64748B", "#94A3B8", "#CBD5E1", "#E2E8F0"
    ]

    fig_pie = go.Figure(
        go.Pie(
            labels=dist_df[cat_column],
            values=dist_df["cumulative_total_cases"],
            hole=0.48,
            marker=dict(colors=custom_colors),
            textinfo="percent+label",
            textposition="outside",
            hovertemplate="<b>%{label}</b><br>Kasus: %{value:,.0f} (%{percent})<extra></extra>",
        )
    )

    fig_pie.update_layout(
        template="plotly_white",
        height=460,
        margin=dict(l=15, r=15, t=10, b=15),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.22, xanchor="center", x=0.5),
    )
    safe_plotly_chart(fig_pie)
    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 8. INSIGHT & NARASI ANALITIS (Dihitung Dinamis dari Data Riil)
# ==============================================================================
peak_idx = timeline_df["daily_new_cases"].idxmax()
peak_row = timeline_df.loc[peak_idx]
peak_date_str = peak_row["date"].strftime("%d %B %Y")
peak_cases_val = peak_row["daily_new_cases"]

highest_c_idx = latest_per_country["cumulative_total_cases"].idxmax()
highest_c_row = latest_per_country.loc[highest_c_idx]
highest_c_name = highest_c_row["country"]
highest_c_cases = highest_c_row["cumulative_total_cases"]
highest_c_share = (
    (highest_c_cases / total_confirmed_cases * 100) if total_confirmed_cases > 0 else 0
)

# Analisis tren kasus aktif pada fase akhir rentang terpilih
if len(timeline_df) >= 14:
    active_early = timeline_df["active_cases"].iloc[:7].mean()
    active_recent = timeline_df["active_cases"].iloc[-7:].mean()
    if active_recent > active_early * 1.05:
        active_trend_desc = "mengalami tren kenaikan beban kasus aktif"
    elif active_recent < active_early * 0.95:
        active_trend_desc = "mengalami tren penurunan beban kasus aktif (fase pemulihan)"
    else:
        active_trend_desc = "cenderung stabil atau berada pada kondisi plateau"
else:
    active_trend_desc = "menunjukkan dinamika fluktuatif harian"

st.markdown(
    f"""
    <div class="insight-box">
        <div class="insight-title">
            <span>💡 Ringkasan Analisis & Temuan Epidemiologis Berdasarkan Data Aktual</span>
        </div>
        <div class="insight-item">
            • <b>Puncak Lonjakan Kasus:</b> Pada rentang filter terpilih, lonjakan penambahan kasus harian tertinggi tercatat pada 
            <b>{peak_date_str}</b> dengan pertambahan sebanyak <b>{peak_cases_val:,.0f} kasus baru</b> dalam satu hari.
        </div>
        <div class="insight-item">
            • <b>Episentrum Kasus Terbesar:</b> Negara <b>{highest_c_name}</b> mencatatkan total kasus tertinggi dengan 
            akumulasi mencapai <b>{highest_c_cases:,.0f} kasus</b>, merepresentasikan 
            <b>{highest_c_share:.1f}%</b> dari total kasus terkonfirmasi pada subset wilayah terpilih.
        </div>
        <div class="insight-item">
            • <b>Tingkat Fatalitas Kasus (CFR):</b> Rata-rata rasio fatalitas kumulatif tercatat sebesar <b>{cfr_rate:.2f}%</b> 
            (total <b>{total_deaths:,.0f} kematian</b> berbanding <b>{total_confirmed_cases:,.0f} kasus terkonfirmasi</b>).
        </div>
        <div class="insight-item">
            • <b>Dinamika Pasien Aktif:</b> Kurva kasus aktif pada fase akhir periode terpilih <b>{active_trend_desc}</b> 
            dengan total kasus aktif tercatat sebesar <b>{active_cases_latest:,.0f}</b> pasien.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 9. INTEGRITAS DATA & METODOLOGI
# ==============================================================================
with st.expander("🔍 Catatan Metodologi, Missing Values, dan Integritas Angka", expanded=False):
    st.markdown(
        """
        #### 1. Penanganan Nilai Kosong (Missing Values / NaN)
        - Dataset harian memiliki nilai kosong pada beberapa kolom seperti `daily_new_cases` (10.458 baris), `active_cases` (18.040 baris), dan `daily_new_deaths` (26.937 baris).
        - **Prinsip Integritas Data:** Nilai kosong **tidak diganti secara otomatis menjadi nol**. Mengisi nilai kosong dengan nol akan menyebabkan distorsi artifisial, seolah-olah terjadi penghentian pandemi atau nihilnya kematian pada hari tersebut.
        - Dalam dashboard ini, agregasi penjumlahan dilakukan dengan mengabaikan nilai NaN (`skipna=True`), dan perhitungan kumulatif per negara mengambil observasi valid terakhir (*last valid observation*) pada rentang tanggal terkait.

        #### 2. Penanganan Nilai Negatif
        - Terdapat sejumlah baris dengan angka negatif pada `daily_new_cases` (20 baris) dan `daily_new_deaths` (9 baris) pada negara tertentu (seperti El Salvador, Jordan, Ghana, dan Afghanistan).
        - **Alasan Epidemiologis:** Nilai negatif dalam data pelaporan resmi COVID-19 (WHO/Worldometer) mencerminkan **koreksi data retrospektif** oleh kementerian kesehatan setempat (misal: eliminasi kasus *false-positive* atau penghapusan data ganda), bukan kekeliruan acak. Nilai tersebut dipertahankan agar tidak mendistorsi total kumulatif riil.

        #### 3. Pencegahan Visualisasi Menyesatkan (Anti-Misleading Visuals)
        - Sumbu bar chart dimulai dari titik nol untuk mempertahankan proporsi skala yang jujur.
        - Moving Average 7-hari disediakan guna mereduksi bias pola pelaporan berkala (seperti *weekend reporting delay*).
        """
    )

# ==============================================================================
# 10. EKSPLORASI DATA & UNDUH CSV
# ==============================================================================
with st.expander("📋 Tabel Data Terfilter & Ekspor CSV", expanded=False):
    st.markdown("Berikut adalah sampel data harian sesuai dengan filter rentang tanggal dan negara yang aktif:")
    display_df = df_filtered[
        [
            "date",
            "country",
            "continent",
            "cumulative_total_cases",
            "daily_new_cases",
            "active_cases",
            "cumulative_total_deaths",
            "daily_new_deaths",
        ]
    ].sort_values(["date", "country"], ascending=[False, True])

    safe_dataframe(display_df.head(500))
    
    csv_data = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Unduh Data Terfilter (.csv)",
        data=csv_data,
        file_name=f"covid19_filtered_{start_date}_{end_date}.csv",
        mime="text/csv",
    )

# ==============================================================================
# 11. FOOTER AKADEMIS
# ==============================================================================
st.markdown(
    """
    <div class="academic-footer">
        <strong>Proyek Ujian Tengah Semester (UTS) — Mata Kuliah Visualisasi Data</strong><br>
        Disusun oleh: <strong>HERLINDA ARTIKA SARI</strong> (NIM: <strong>241041011</strong>) — Program Studi <strong>D3 Manajemen Informatika</strong><br>
        Sumber Data: <em>Worldometer Coronavirus Dataset via Kaggle</em> | Dibangun menggunakan Python, Streamlit, Pandas, dan Plotly.
    </div>
    """,
    unsafe_allow_html=True,
)
