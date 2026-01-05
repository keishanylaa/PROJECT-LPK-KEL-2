import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Kimia Analisis",
    page_icon="⚗️",
    layout="centered"
)

# Judul utama
st.title("🧪 Selamat datang di Kalkulator Kimia Analisis")

# Subjudul
st.write("### Silahkan pilih menu di bawah ini")

# Menu pilihan
menu = st.selectbox(
    "Pilih jenis perhitungan:",
    (
        "Faktor Pengenceran",
        "Normalitas",
        "Molaritas",
        "Mg/L",
        "% b/v",
        "% b/b",
        "% v/v"
    )
)

# Tampilan berdasarkan menu
st.markdown("---")
st.write(f"📌 **Menu yang dipilih:** {menu}")

# Placeholder (nanti bisa diisi rumus & input)
st.info("Fitur perhitungan akan ditampilkan di sini.")
