import streamlit as st
import pandas as pd
from supabase import create_client

st.set_page_config(page_title="Stok Barang", page_icon="📦", layout="wide")

# --- KONEKSI SUPABASE ---
SUPABASE_URL = "https://kowvsxabsasckkxnbtyh.supabase.co"
SUPABASE_KEY = "sb_publishable_QbFP8K9qX1vvbNwGaSDVSg_DdbYGApN"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("📦 Manajemen Stok & Inventaris Realtime")
st.caption("Data tersimpan otomatis di Database Supabase!")
st.divider()

# --- FETCH DATA FROM DATABASE ---
try:
    response = supabase.table("stok_barang").select("*").execute()
    stok_data = pd.DataFrame(response.data)
except Exception as e:
    stok_data = pd.DataFrame()
    st.error(f"Gagal konek ke database: {e}")

# --- FORM TAMBAH STOK BARU ---
with st.expander("➕ Tambah Bahan / Stok Baru"):
    with st.form("form_stok"):
        nama_bahan = st.text_input("Nama Bahan / Item")
        stok_input = st.number_input("Jumlah Stok", min_value=0, value=10)
        satuan_input = st.selectbox("Satuan", ["Kg", "Liter", "Botol", "Pcs", "Pack"])
        status_input = st.selectbox("Status", ["Aman", "Hampir Habis", "Habis"])
        
        submit = st.form_submit_button("Simpan ke Database")
        
        if submit and nama_bahan:
            supabase.table("stok_barang").insert({
                "nama_bahan": nama_bahan,
                "stok_tersedia": stok_input,
                "satuan": satuan_input,
                "status": status_input
            }).execute()
            st.success(f"Berhasil nambah {nama_bahan}!")
            st.rerun()

# --- TAMPILKAN TABEL ---
if not stok_data.empty:
    st.dataframe(stok_data[["id", "nama_bahan", "stok_tersedia", "satuan", "status"]], use_container_width=True)
else:
    st.info("Belum ada data stok atau koneksi lagi diproses!")
