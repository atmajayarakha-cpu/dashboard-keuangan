import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stok Barang", page_icon="📦", layout="wide")

st.title("📦 Manajemen Stok & Inventaris")
st.caption("Pantau ketersediaan bahan baku bisnis Kopi Susuh lu!")
st.divider()

stok_data = pd.DataFrame({
    "Nama Bahan / Item": ["Biji Kopi Espresso", "Susu UHT", "Sirup Aren", "Cup 16oz", "Sedotan Eco"],
    "Stok Tersedia": [15, 40, 12, 350, 500],
    "Satuan": ["Kg", "Liter", "Botol", "Pcs", "Pcs"],
    "Status": ["Aman", "Aman", "Hampir Habis", "Aman", "Aman"]
})

st.dataframe(stok_data, use_container_width=True)
