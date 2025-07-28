import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Estimasi Harga HP Bekas")

merk = st.selectbox("Pilih Merk", ["Samsung", "Xiaomi", "iPhone", "Oppo", "Realme", "Vivo"])
tipe = st.text_input("Tipe HP (misal: A10, Redmi 9)")
tahun = st.number_input("Tahun Rilis", 2015, 2024, 2020)
lcd_retak = st.selectbox("LCD Retak?", ["Tidak", "Ya"])
baterai_soak = st.selectbox("Baterai Soak?", ["Tidak", "Ya"])
dus_ada = st.selectbox("Dus Ada?", ["Tidak", "Ya"])

if st.button("Prediksi Harga"):
    data = pd.DataFrame([{
        "merk": merk,
        "tipe": tipe,
        "tahun_rilis": tahun,
        "lcd_retak": 1 if lcd_retak == "Ya" else 0,
        "baterai_soak": 1 if baterai_soak == "Ya" else 0,
        "dus_ada": 1 if dus_ada == "Ya" else 0,
    }])
    
    harga = model.predict(data)[0]
    st.success(f"Perkiraan harga HP: Rp{int(harga):,}")
