import streamlit as st
import pandas as pd
from supabase import create_client

st.set_page_config(page_title="Stok Barang", page_icon="📦", layout="wide")

# --- KONEKSI SUPABASE ---
SUPABASE_URL = "https://kowvsxabsasckkxnbtyh.supabase.co"
SUPABASE_KEY = "sb_publishable_QbFP8K9qX1vvbNwGaSDVSg_DdbYGApN"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("📦 Manajemen Stok Realtime")

# --- FETCH DATA ---
response = supabase.table("stok_barang").select("*").execute()
stok_data = pd.DataFrame(response.data)

# --- TABEL DENGAN TOMBOL HAPUS ---
st.subheader("Data Stok Saat Ini")

if not stok_data.empty:
    for index, row in stok_data.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{row['nama_bahan']}** - {row['stok_tersedia']} {row['satuan']} ({row['status']})")
        with col2:
            if st.button("Hapus", key=f"del_{row['id']}"):
                supabase.table("stok_barang").delete().eq("id", row['id']).execute()
                st.rerun()
        with col3:
            st.write("---") # Placeholder buat nanti dikembangin jadi edit form
else:
    st.info("Data kosong bray!")

# --- FORM TAMBAH (TETAP SAMA) ---
with st.expander("➕ Tambah Bahan Baru"):
    with st.form("form_stok"):
        nama = st.text_input("Nama Bahan")
        jml = st.number_input("Jumlah", value=0)
        stn = st.selectbox("Satuan", ["Kg", "Liter", "Botol", "Pcs"])
        sts = st.selectbox("Status", ["Aman", "Hampir Habis", "Habis"])
        if st.form_submit_button("Simpan"):
            supabase.table("stok_barang").insert({"nama_bahan": nama, "stok_tersedia": jml, "satuan": stn, "status": sts}).execute()
            st.rerun()
# --- TAMPILKAN TABEL ---
if not stok_data.empty:
    st.dataframe(stok_data[["id", "nama_bahan", "stok_tersedia", "satuan", "status"]], use_container_width=True)
else:
    st.info("Belum ada data stok atau koneksi lagi diproses!")
