"""
Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022
Ujian Tengah Semester (UTS) - Mata Kuliah Visualisasi Data
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
    page_title="Dashboard COVID-19 Global (2020–2022)",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS untuk tema Biru, Putih, dan Abu-abu yang modern, rapi, dan responsif
st.markdown(
    """
    <style>
    /* Background & Tipografi */
    .stApp {
        background-color: #F8FAFC;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #0F172A;
    }
    
    /* Header Card */
    .header-card {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 60%, #3B82F6 100%);
        border-radius: 16px;
        padding: 24px 30px;
        color: #FFFFFF;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.22);
        margin-bottom: 22px;
    }
    .header-title {
        font-size: 1.85rem;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
    }
    .header-subtitle {
        font-size: 0.96rem;
        opacity: 0.94;
        line-height: 1.5;
        max-width: 950px;
    }
    .badge-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.22);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 8px;
        margin-top: 12px;
    }

    /* KPI Metric Cards */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        border-top: 4px solid #2563EB;
        height: 100%;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px -2px rgba(15, 23, 42, 0.08);
    }
    .kpi-card-danger {
        border-top-color: #475569;
    }
    .kpi-card-info {
        border-top-color: #3B82F6;
    }
    .kpi-card-accent {
        border-top-color: #60A5FA;
    }
    .kpi-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .kpi-value {
        font-size: 1.65rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.2;
    }
    .kpi-subtext {
        font-size: 0.78rem;
        color: #64748B;
        margin-top: 6px;
    }

    /* Chart Box Container */
    .chart-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px 20px 10px 20px;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.04);
        margin-bottom: 18px;
    }
    .chart-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 3px;
    }
    .chart-desc {
        font-size: 0.81rem;
        color: #64748B;
        margin-bottom: 10px;
    }

    /* Insight Narrative Box */
    .insight-box {
        background: #EFF6FF;
        border-left: 5px solid #2563EB;
        border-radius: 0 12px 12px 0;
        padding: 18px 22px;
        margin: 18px 0;
        border-top: 1px solid #DBEAFE;
        border-right: 1px solid #DBEAFE;
        border-bottom: 1px solid #DBEAFE;
    }
    .insight-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 10px;
    }
    .insight-item {
        font-size: 0.88rem;
        color: #1E293B;
        line-height: 1.6;
        margin-bottom: 6px;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        font-size: 0.82rem;
        color: #94A3B8;
        padding: 24px 0 12px 0;
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
# 3. SIDEBAR: FILTER INTERAKTIF
# ==============================================================================
st.sidebar.markdown(
    """
    <div style='text-align: center; padding-bottom: 8px;'>
        <h2 style='color:#1E3A8A; margin-bottom: 2px;'>📊 Panel Filter</h2>
        <span style='font-size:0.82rem; color:#64748B;'>Konfigurasi Analisis COVID-19</span>
    </div>
    <hr style='margin-top:0; margin-bottom:16px; border-color:#E2E8F0;'>
    """,
    unsafe_allow_html=True,
)

min_dataset_date = df_daily["date"].min().date()
max_dataset_date = df_daily["date"].max().date()

st.sidebar.markdown("### 📅 1. Filter Rentang Tanggal")

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

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌍 2. Filter Wilayah & Negara")

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
    help="Centang untuk menyertakan seluruh negara.",
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

# Info box di sidebar
with st.sidebar.expander("ℹ️ Sumber & Integritas Data", expanded=False):
    st.markdown(
        """
        - **Sumber:** [Kaggle COVID-19 Global Dataset](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset)
        - **Rentang Asli:** 22 Jan 2020 – 14 Mei 2022
        - **Total Cakupan:** 226 Negara/Wilayah
        - **Penanganan Missing Values:** Nilai kosong (NaN) dipertahankan sesuai format aslinya tanpa imputasi nol sembarangan.
        - **Nilai Negatif:** Merefleksikan koreksi data retrospektif resmi dari otoritas kesehatan terkait.
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
# 5. HEADER DASHBOARD
# ==============================================================================
st.markdown(
    f"""
    <div class="header-card">
        <div class="header-title">Dashboard Analisis Perkembangan COVID-19 Global Tahun 2020–2022</div>
        <div class="header-subtitle">
            Platform visualisasi interaktif untuk menganalisis perkembangan kasus terkonfirmasi, angka kematian, dinamika
            kasus aktif, serta perbandingan regional secara objektif berbasis data Worldometer.
        </div>
        <div>
            <span class="badge-tag">🎓 UTS Visualisasi Data</span>
            <span class="badge-tag">📅 Periode: {start_date.strftime('%d %b %Y')} – {end_date.strftime('%d %b %Y')}</span>
            <span class="badge-tag">🌐 Cakupan: {count_countries:,} Negara Terpilih</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. KPI METRIC CARDS (Minimal 3 KPI Cards)
# ==============================================================================
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Terkonfirmasi</div>
            <div class="kpi-value">{total_confirmed_cases:,.0f}</div>
            <div class="kpi-subtext">+{total_new_cases_period:,.0f} kasus baru pada periode ini</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col2:
    st.markdown(
        f"""
        <div class="kpi-card kpi-card-danger">
            <div class="kpi-label">Total Kematian</div>
            <div class="kpi-value">{total_deaths:,.0f}</div>
            <div class="kpi-subtext">+{total_new_deaths_period:,.0f} kematian baru pada periode ini</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col3:
    st.markdown(
        f"""
        <div class="kpi-card kpi-card-info">
            <div class="kpi-label">Case Fatality Rate (CFR)</div>
            <div class="kpi-value">{cfr_rate:.2f}%</div>
            <div class="kpi-subtext">Rasio kematian kumulatif terhadap kasus</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col4:
    st.markdown(
        f"""
        <div class="kpi-card kpi-card-accent">
            <div class="kpi-label">Jumlah Negara Terpantau</div>
            <div class="kpi-value">{count_countries:,}</div>
            <div class="kpi-subtext">Dari total 226 negara dalam basis data</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# 7. VISUALISASI UTAMA (Minimal 4 Jenis Visualisasi Berbeda)
# ==============================================================================

# Agregasi harian untuk grafik deret waktu
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
            <div class="chart-title">📈 1. Line Chart: Perkembangan Kasus dari Waktu ke Waktu</div>
            <div class="chart-desc">Menampilkan dinamika penambahan kasus harian beserta kurva 7-Day Moving Average untuk mengidentifikasi gelombang pandemi.</div>
        """,
        unsafe_allow_html=True,
    )

    line_metric = st.radio(
        "Pilih Jenis Data Tren:",
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
                opacity=0.65,
                hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kasus Harian:</b> %{y:,.0f}<extra></extra>",
            )
        )
        fig_line.add_trace(
            go.Scatter(
                x=timeline_df["date"],
                y=timeline_df["cases_7d_ma"],
                mode="lines",
                name="7-Day Moving Average",
                line=dict(color="#1D4ED8", width=2.8),
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
                line=dict(color="#1E3A8A", width=3),
                hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kumulatif:</b> %{y:,.0f}<extra></extra>",
            )
        )
        y_axis_label = "Total Kasus Kumulatif"

    fig_line.update_layout(
        template="plotly_white",
        height=380,
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
            <div class="chart-title">🌊 2. Area Chart: Perkembangan Kasus Aktif</div>
            <div class="chart-desc">Menggambarkan dinamika beban pasien yang sedang dirawat atau menjalani isolasi aktif sepanjang rentang waktu terpilih.</div>
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
            line=dict(color="#2563EB", width=2.2),
            fill="tozeroy",
            fillcolor="rgba(37, 99, 235, 0.22)",
            hovertemplate="<b>Tanggal:</b> %{x|%d %b %Y}<br><b>Kasus Aktif:</b> %{y:,.0f}<extra></extra>",
        )
    )

    fig_area.update_layout(
        template="plotly_white",
        height=425,
        margin=dict(l=15, r=15, t=10, b=15),
        xaxis=dict(
            title="",
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#CBD5E1",
        ),
        yaxis=dict(
            title="Jumlah Pasien Kasus Aktif",
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
            <div class="chart-title">📊 3. Bar Chart: Negara dengan Kasus Tertinggi</div>
            <div class="chart-desc">Peringkat negara dengan akumulasi kasus terkonfirmasi terbesar dalam filter yang sedang aktif.</div>
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
                    [0.5, "#3B82F6"],
                    [1.0, "#1E3A8A"],
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
        height=400,
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
            <div class="chart-title">🍩 4. Pie Chart: Perbandingan Kasus Berdasarkan Benua</div>
            <div class="chart-desc">Proporsi persebaran kasus terkonfirmasi antar benua atau antar negara terpilih secara proporsional.</div>
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
        "#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA",
        "#93C5FD", "#64748B", "#94A3B8", "#CBD5E1", "#475569"
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
        height=450,
        margin=dict(l=15, r=15, t=10, b=15),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.18, xanchor="center", x=0.5),
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
            <span>💡 Ringkasan Analisis & Insight Berdasarkan Data Aktual</span>
        </div>
        <div class="insight-item">
            • <b>Puncak Lonjakan Kasus:</b> Pada rentang filter terpilih, lonjakan penambahan kasus harian tertinggi terjadi pada 
            <b>{peak_date_str}</b> dengan pertambahan sebanyak <b>{peak_cases_val:,.0f} kasus baru</b> dalam satu hari.
        </div>
        <div class="insight-item">
            • <b>Episentrum Kasus Terbesar:</b> Negara <b>{highest_c_name}</b> mencatatkan total kasus tertinggi dengan 
            akumulasi mencapai <b>{highest_c_cases:,.0f} kasus</b>, merepresentasikan 
            <b>{highest_c_share:.1f}%</b> dari total kasus terkonfirmasi pada subset wilayah terpilih.
        </div>
        <div class="insight-item">
            • <b>Tingkat Fatalitas Kasus (CFR):</b> Rata-rata rasio fatalitas kumulatif tercatat sebesar <b>{cfr_rate:.2f}%</b> 
            (total <b>{total_deaths:,.0f} kematian</b> berbanding <b>{total_confirmed_cases:,.0f} kasus</b>).
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
# 11. FOOTER
# ==============================================================================
st.markdown(
    """
    <div class="footer-text">
        Proyek Ujian Tengah Semester (UTS) — Visualisasi Data Analisis COVID-19 Global (2020–2022)<br>
        Dibangun menggunakan Python, Streamlit, Pandas, dan Plotly.
    </div>
    """,
    unsafe_allow_html=True,
)
