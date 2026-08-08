import streamlit as st
import pandas as pd
import math

# --- CONFIG & THEME ---
st.set_page_config(page_title="SOUR Finance x Olivia Vibe", page_icon="💜", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0f0f12; }
    .stApp {
        background: linear-gradient(135deg, #181124 0%, #0d0a14 100%);
        color: #e2d9f3;
    }
    div[data-testid="stMetricValue"] {
        color: #b388ff !important;
        font-size: 28px !important;
        font-weight: bold;
    }
    @keyframes glow {
        0% { text-shadow: 0 0 5px #8c52ff, 0 0 10px #8c52ff; border-color: #8c52ff; }
        50% { text-shadow: 0 0 20px #b388ff, 0 0 30px #b388ff; border-color: #b388ff; }
        100% { text-shadow: 0 0 5px #8c52ff, 0 0 10px #8c52ff; border-color: #8c52ff; }
    }
    .animated-lyric {
        background: rgba(36, 25, 56, 0.8);
        border: 2px solid #8c52ff;
        padding: 20px;
        border-radius: 12px;
        font-style: italic;
        font-size: 20px;
        color: #ffffff;
        text-align: center;
        animation: glow 3s infinite alternate;
        margin-bottom: 15px;
    }
    marquee {
        font-family: 'Courier New', Courier, monospace;
        font-size: 15px;
        color: #d1c4e9;
        background: #181124;
        padding: 6px;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("💜 SOUR & PROFIT: Financial Dashboard")
st.caption("Aplikasi Keuangan Aesthetic Vibes • Olivia Rodrigo Edition")
st.divider()

# --- MUSIC PLAYER ---
st.subheader("🎵 Olivia Rodrigo - Official Music Player")
col_music1, col_music2 = st.columns([2, 1])
with col_music1:
    st.video("https://www.youtube.com/watch?v=cii6ruuycQA")
with col_music2:
    st.markdown("""
    <div style="background: #241938; padding: 15px; border-radius: 10px; border: 1px solid #8c52ff;">
        <h4>🎧 Now Playing:</h4>
        <p><b>Artist:</b> Olivia Rodrigo<br>
        <b>Track:</b> deja vu / good 4 u<br>
        <b>Vibe Check:</b> Drop dead aesthetic ✨</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- ANIMATED LYRIC ---
st.markdown("""
<div class="animated-lyric">
    ✨ "Play the songs that you used to play for me..." ✨<br>
    <span style="font-size: 14px; color: #b388ff;">— <b>Olivia Rodrigo (deja vu)</b></span>
</div>
<marquee behavior="scroll" direction="left">
    💜 NOW PLAYING: Olivia Rodrigo - deja vu • Keep tracking your profit • Don't let your business go BROKE! 💜
</marquee>
""", unsafe_allow_html=True)

st.write("")

# --- SIDEBAR INPUT ---
st.sidebar.header("🔮 Business Inputs")
nama_produk    = st.sidebar.text_input("Nama Produk", value="Kopi Susuh x Olivia")
modal_per_unit = st.sidebar.number_input("Modal / HPP (Rp)", min_value=0.0, value=8000.0, step=1000.0)
harga_jual     = st.sidebar.number_input("Harga Jual (Rp)", min_value=0.0, value=18000.0, step=1000.0)
jumlah_terjual = st.sidebar.slider("Volume Terjual (Qty)", min_value=0, max_value=1000, value=250)

# --- MATH LOGIC ---
total_omset       = harga_jual * jumlah_terjual
total_modal       = modal_per_unit * jumlah_terjual
keuntungan_bersih = total_omset - total_modal
profit_per_unit   = harga_jual - modal_per_unit
margin_profit     = (keuntungan_bersih / total_omset) * 100 if total_omset > 0 else 0

# --- METRIC CARDS ---
st.subheader(f"✨ Metrics Breakdown: {nama_produk}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Omset", f"Rp {total_omset:,.0f}")
col2.metric("Total Modal", f"Rp {total_modal:,.0f}")
col3.metric("Profit Bersih", f"Rp {keuntungan_bersih:,.0f}", delta=f"Rp {profit_per_unit:,.0f}/unit")
col4.metric("Margin Profit", f"{margin_profit:.2f}%")

st.divider()

# ===================================================
# 🔥 FITUR BARU STEP 2: KALKULATOR TARGET (GOAL SEEK) 🔥
# ===================================================
st.subheader("🎯 Goal Seeking: Kalkulator Target Profit")
st.write("Mau dapet untung berapa bulan ini? Tentukan target lu, sistem bakal ngitung strateginya!")

col_target1, col_target2 = st.columns([1, 2])

with col_target1:
    target_profit = st.number_input("Target Profit Bersih (Rp)", min_value=100000.0, value=5000000.0, step=500000.0)

with col_target2:
    if profit_per_unit > 0:
        # Rumus: Target Profit / Untung per Unit
        target_qty = math.ceil(target_profit / profit_per_unit)
        target_omset_butuh = target_qty * harga_jual
        
        st.info(f"""
        📌 **SIMULASI STRATEGI TARGET:**
        - Untung per unit lu sekarang: **Rp {profit_per_unit:,.0f}**
        - Lu wajib menjual minimal **{target_qty:,} unit/gelas** `{nama_produk}`!
        - Total Omset yang harus dikejar: **Rp {target_omset_butuh:,.0f}**
        """)
    else:
        st.error("⚠️ **GAGAL HITUNG:** Harga jual lu lebih kecil/sama dengan modal! Naikkan harga jual di sidebar dulu bray!")

st.divider()

# --- VISUAL CHART & STATUS ---
col_left, col_right = st.columns([3, 2])

with col_left:
    st.write("📈 **Visual Perbandingan Keuangan**")
    chart_data = pd.DataFrame({
        "Kategori": ["Total Modal (HPP)", "Keuntungan Bersih", "Total Omset"],
        "Nominal (Rp)": [total_modal, keuntungan_bersih if keuntungan_bersih > 0 else 0, total_omset]
    })
    st.bar_chart(chart_data.set_index("Kategori"))

with col_right:
    st.write("💌 **Status Diagnosa & Vibe Check**")
    if keuntungan_bersih > 0:
        st.success("✨ **GOOD 4 U!** Bisnis lu dapet untung manis! Pertahankan volumenya!")
        st.balloons()
    elif keuntungan_bersih == 0:
        st.warning("😐 **DEJA VU!** Lu cuma muterin uang tanpa untung. Naikkan harga jual!")
    else:
        st.error("💔 **TRAITOR!** Bisnis lu rugi nombok modal. Evaluasi HPP sekarang!")

st.divider()

# --- EXPORT DATA TO CSV ---
st.subheader("📥 Export Laporan Keuangan (.CSV)")
df_laporan = pd.DataFrame({
    "Parameter": ["Nama Produk", "Modal per Unit (Rp)", "Harga Jual (Rp)", "Qty Terjual", "Total Omset (Rp)", "Total Modal (Rp)", "Profit Bersih (Rp)", "Margin (%)"],
    "Nilai": [nama_produk, modal_per_unit, harga_jual, jumlah_terjual, total_omset, total_modal, keuntungan_bersih, f"{margin_profit:.2f}%"]
})
st.dataframe(df_laporan, use_container_width=True)
csv_data = df_laporan.to_csv(index=False).encode('utf-8')

st.download_button(
    label="💾 Download Laporan Keuangan (CSV)",
    data=csv_data,
    file_name=f"Laporan_Keuangan_{nama_produk.replace(' ', '_')}.csv",
    mime="text/csv",
)