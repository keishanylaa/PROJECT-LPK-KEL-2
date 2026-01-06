import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Kalkulator Kimia Analisis",
    page_icon="⚗️",
    layout="centered"
)

st.title("🧪 Kalkulator Kimia Analisis")
st.write(
    "Kalkulator ini membantu perhitungan kimia analisis "
    "agar pengguna lebih memahami konsep perhitungan kimia."
)

# =========================
# MENU UTAMA
# =========================
menu = st.selectbox(
    "Pilih jenis perhitungan:",
    [
        "Faktor Pengenceran",
        "Molaritas",
        "Normalitas",
        "mg/L",
        "% b/v",
        "% b/b",
        "% v/v"
    ]
)

st.markdown("---")

# =========================
# DATABASE Mr
# =========================
mr_database = {
    "NaCl": 58.44,
    "HCl": 36.46,
    "H2SO4": 98.08,
    "NaOH": 40.00,
    "KOH": 56.11,
    "CH3COOH": 60.05,
    "NH3": 17.03,
    "KMnO4": 158.04,
    "AgNO3": 169.87,
    "CaCO3": 100.09
}

# =========================
# FAKTOR PENGENCERAN
# =========================
if menu == "Faktor Pengenceran":
    st.subheader("⚗️ Faktor Pengenceran")

    sub_menu = st.radio(
        "Pilih perhitungan:",
        ["Faktor pengenceran", "Volume yang harus diambil"]
    )

    if sub_menu == "Faktor pengenceran":
        V_lab = st.number_input("Volume labu takar (mL)", min_value=0.0)
        V_pipet = st.number_input("Volume yang dipipet (mL)", min_value=0.0)

        if st.button("Hitung FP"):
            if V_pipet == 0:
                st.error("Volume pipet tidak boleh 0")
            else:
                st.success(f"FP = **{V_lab / V_pipet:.3f}**")

    else:
        C1 = st.number_input("Konsentrasi awal")
        C2 = st.number_input("Konsentrasi akhir")
        V2 = st.number_input("Volume akhir (mL)")

        if st.button("Hitung Volume"):
            if C1 == 0:
                st.error("Konsentrasi awal tidak boleh 0")
            else:
                V1 = (C2 * V2) / C1
                st.success(f"Volume diambil = **{V1:.3f} mL**")

# =========================
# MOLARITAS
# =========================
elif menu == "Molaritas":
    st.subheader("⚗️ Molaritas")

    metode = st.radio(
        "Metode perhitungan:",
        ["Menggunakan massa", "Menggunakan database Mr"]
    )

    volume = st.number_input("Volume larutan (L)", min_value=0.0)

    if metode == "Menggunakan massa":
        massa = st.number_input("Massa zat (g)", min_value=0.0)
        mr = st.number_input("Mr zat", min_value=0.0)
    else:
        senyawa = st.selectbox("Pilih senyawa", list(mr_database.keys()))
        massa = st.number_input("Massa zat (g)", min_value=0.0)
        mr = mr_database[senyawa]
        st.info(f"Mr {senyawa} = {mr}")

    if st.button("Hitung Molaritas"):
        if volume == 0 or mr == 0:
            st.error("Volume dan Mr tidak boleh 0")
        else:
            M = massa / (mr * volume)
            st.success(f"Molaritas = **{M:.4f} M**")

# =========================
# NORMALITAS
# =========================
elif menu == "Normalitas":
    st.subheader("⚗️ Normalitas")

    volume = st.number_input("Volume larutan (L)", min_value=0.0)
    n = st.number_input("Faktor ekivalen (n)", min_value=0.0)

    senyawa = st.selectbox("Pilih senyawa", list(mr_database.keys()))
    massa = st.number_input("Massa zat (g)", min_value=0.0)
    mr = mr_database[senyawa]

    if st.button("Hitung Normalitas"):
        if volume == 0 or mr == 0 or n == 0:
            st.error("Volume, Mr, dan n tidak boleh 0")
        else:
            N = (massa * n) / (mr * volume)
            st.success(f"Normalitas = **{N:.4f} N**")
