import streamlit as st
import math

st.set_page_config(page_title="Target Profit", page_icon="🎯", layout="wide")

st.title("🎯 Goal Seeking Calculator")
st.caption("Hitung berapa unit yang wajib terjual buat kejar profit impian lu!")
st.divider()

harga_jual = st.number_input("Harga Jual Per Unit (Rp)", value=18000.0, step=1000.0)
modal_unit = st.number_input("Modal / HPP Per Unit (Rp)", value=8000.0, step=1000.0)
target_profit = st.number_input("Target Profit Bersih (Rp)", value=5000000.0, step=500000.0)

profit_per_unit = harga_jual - modal_unit

st.divider()

if profit_per_unit > 0:
    target_qty = math.ceil(target_profit / profit_per_unit)
    target_omset = target_qty * harga_jual

    st.success(f"""
    🎯 **HASIL ANALISIS TARGET:**
    - Keuntungan per unit: **Rp {profit_per_unit:,.0f}**
    - Lu minimal harus menjual **{target_qty:,} unit/gelas**!
    - Target Total Omset Penjualan: **Rp {target_omset:,.0f}**
    """)
    st.balloons()
else:
    st.error("⚠️ Harga jual kagak boleh kurang dari atau sama dengan modal HPP bray!")
