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
    (
        "Faktor Pengenceran",
        "Molaritas",
        "Normalitas",
        "mg/L",
        "% b/v",
        "% b/b",
        "% v/v"
    )
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
    st.write("Faktor pengenceran (FP) adalah bilangan yang menyatakan seberapa besar suatu larutan diencerkan dibandingkan larutan awalnya. Faktor pengenceran banyak digunakan dalam kimia analitik, farmasi, biologi, dan analisis instrumen (misalnya AAS) untuk menghitung konsentrasi akhir setelah pengenceran.")
    st.write("Rumus mencari FP adalah volume labu takar/volume yang dipipet")
    st.write("Rumus untuk pengenceran adalah Consentration1.Volume1=Consentration2.Volume2")
    sub_menu = st.radio(
        "Pilih perhitungan:",
        ("Faktor pengenceran", "Volume yang harus diambil")
    )


    st.markdown("---")


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
    st.write("Molaritas (M) adalah satuan konsentrasi larutan yang menyatakan jumlah mol zat terlarut dalam setiap 1 liter larutan. Molaritas sangat umum digunakan dalam kimia analitik, kimia fisik, dan farmasi, terutama untuk perhitungan reaksi dan stoikiometri.")
    st.write("Rumus Molaritas adalah M= mol/Liter; Jika diketahui massa zatnya maka: M= massa zat(g)/ Mr(g/mol).Volume(L) ")
    metode = st.radio(
        "Metode perhitungan:",
        ("Menggunakan massa", "Menggunakan database Mr")
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
    st.write("Normalitas (N) adalah satuan konsentrasi larutan yang menyatakan jumlah ekivalen zat terlarut dalam setiap 1 liter larutan.Normalitas banyak digunakan dalam titrasi asam–basa, redoks, dan analisis volumetri, karena langsung berkaitan dengan stoikiometri reaksi.")
    st.write("Rumus Normalitas adalah N=ekivalen/Volume(L); Jika massanya diketahui maka N=massa zat (g). faktor ekivalen/ Mr(g/mol).Volume(L)")
    metode = st.radio(
        "Metode perhitungan:",
        ("Menggunakan massa", "Menggunakan database Mr")
    )


    volume = st.number_input("Volume larutan (L)", min_value=0.0)
    n = st.number_input("Faktor ekivalen (n)", min_value=0.0)


    if metode == "Menggunakan massa":
        massa = st.number_input("Massa zat (g)", min_value=0.0)
        mr = st.number_input("Mr zat", min_value=0.0)


    else:
        senyawa = st.selectbox("Pilih senyawa", list(mr_database.keys()))
        massa = st.number_input("Massa zat (g)", min_value=0.0)
        mr = mr_database[senyawa]
        st.info(f"Mr {senyawa} = {mr}")


    if st.button("Hitung Normalitas"):
        if volume == 0 or mr == 0 or n == 0:
            st.error("Volume, Mr, dan n tidak boleh 0")
        else:
            N = (massa * n) / (mr * volume)
            st.success(f"Normalitas = **{N:.4f} N**")


# =========================
# mg/L
# =========================
elif menu == "mg/L":


    st.subheader("⚗️ mg/L")
    st.write("konsentrasi mg/L (ppm) adalah cara menyatakan konsentrasi zat sebagai jumlah miligram zat terlarut dalam setiap 1 liter (L) larutan. Satuan mg/L sangat umum digunakan dalam analisis kimia, lingkungan, farmasi, dan AAS, terutama untuk menyatakan kadar zat dalam konsentrasi rendah.")
    st.write("untuk mencari massa, kita bisa menggunakan rumus massa(mg)= konsentrasi (mg/L).Volume (L)")
    sub = st.radio(
        "Pilih perhitungan:",
        ("Cari konsentrasi", "Cari massa", "Cari volume")
    )


    if sub == "Cari konsentrasi":
        massa = st.number_input("Massa (mg)", min_value=0.0)
        volume = st.number_input("Volume (L)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{massa / volume:.4f} mg/L")


    elif sub == "Cari massa":
        kons = st.number_input("Konsentrasi (mg/L)", min_value=0.0)
        volume = st.number_input("Volume (L)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{kons * volume:.4f} mg")


    else:
        kons = st.number_input("Konsentrasi (mg/L)", min_value=0.0)
        massa = st.number_input("Massa (mg)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{massa / kons:.4f} L")


# =========================
# % b/v
# =========================
elif menu == "% b/v":


    st.subheader("⚗️ % b/v")
    st.write("(persen berat per volume) adalah satuan konsentrasi yang menyatakan jumlah zat (dalam gram) yang terdapat dalam setiap 100 mL larutan. Satuan % b/v sering digunakan dalam kimia analitik, farmasi, dan laboratorium untuk menyatakan konsentrasi larutan padat dalam cairan.")
    st.write("Rumus %b/v= massa zat terlarut (g) /volume total campuran(mL) .100%")
    sub = st.radio(
        "Pilih perhitungan:",
        ("Cari %", "Cari massa", "Cari volume")
    )


    if sub == "Cari %":
        m = st.number_input("Massa (g)", min_value=0.0)
        v = st.number_input("Volume (mL)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{(m / v) * 100:.4f} % b/v")


    elif sub == "Cari massa":
        p = st.number_input("% b/v", min_value=0.0)
        v = st.number_input("Volume (mL)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{(p / 100) * v:.4f} g")


    else:
        p = st.number_input("% b/v", min_value=0.0)
        m = st.number_input("Massa (g)", min_value=0.0)


        if st.button("Hitung"):
            st.success(f"{(m * 100) / p:.2f} mL")


# =========================
# % b/b (berat / berat)
# =========================
elif menu == "% b/b":


    st.subheader("⚗️ Persen berat/berat (% b/b)")
    st.write(
        "% b/b menyatakan jumlah zat terlarut (gram) "
        "dalam setiap 100 gram campuran."
    )
    st.write("% b/b sering digunakan untuk campuran padat–padat, salep, serbuk, dan sediaan farmasi atau bahan kimia yang tidak bergantung pada perubahan volume.")
    st.write("Rumus %b/b= massa zat terlarut (g)/massa total campuran (g) .100%")


    sub = st.radio(
        "Pilih perhitungan:",
        ("Cari % b/b", "Cari massa zat (g)", "Cari massa campuran (g)")
    )


    st.markdown("---")


    if sub == "Cari % b/b":
        massa_zat = st.number_input(
            "Massa zat terlarut (g)", min_value=0.0, format="%.4f"
        )
        massa_total = st.number_input(
            "Massa campuran (g)", min_value=0.0, format="%.4f"
        )


        if st.button("Hitung % b/b"):
            if massa_total == 0:
                st.error("Massa campuran tidak boleh 0")
            else:
                persen = (massa_zat / massa_total) * 100
                st.success(f"Konsentrasi = **{persen:.4f} % b/b**")


    elif sub == "Cari massa zat (g)":
        persen = st.number_input(
            "Konsentrasi (% b/b)", min_value=0.0, format="%.4f"
        )
        massa_total = st.number_input(
            "Massa campuran (g)", min_value=0.0, format="%.4f"
        )


        if st.button("Hitung massa zat"):
            massa_zat = (persen / 100) * massa_total
            st.success(f"Massa zat terlarut = **{massa_zat:.4f} g**")


    else:  # Cari massa campuran
        persen = st.number_input(
            "Konsentrasi (% b/b)", min_value=0.0, format="%.4f"
        )
        massa_zat = st.number_input(
            "Massa zat terlarut (g)", min_value=0.0, format="%.4f"
        )


        if st.button("Hitung massa campuran"):
            if persen == 0:
                st.error("Konsentrasi tidak boleh 0")
            else:
                massa_total = (massa_zat * 100) / persen
                st.success(f"Massa campuran = **{massa_total:.4f} g**")


# =========================
# % v/v (volume / volume)
# =========================
elif menu == "% v/v":


    st.subheader("⚗️ Persen volume/volume (% v/v)")
    st.write(
        "% v/v menyatakan volume zat terlarut (mL) "
        "dalam setiap 100 mL larutan."
    )
    st.write("% v/v umum digunakan untuk menyatakan konsentrasi campuran cair–cair, misalnya alkohol, pelarut organik, dan larutan farmasi.")
    st.write("Rumus %v/v= volume zat terlarut (mL) /volume total campuran (mL) .100%")


    sub = st.radio(
        "Pilih perhitungan:",
        ("Cari % v/v", "Cari volume zat (mL)", "Cari volume larutan (mL)")
    )


    st.markdown("---")


    if sub == "Cari % v/v":
        volume_zat = st.number_input(
            "Volume zat terlarut (mL)", min_value=0.0, format="%.2f"
        )
        volume_total = st.number_input(
            "Volume larutan (mL)", min_value=0.0, format="%.2f"
        )


        if st.button("Hitung % v/v"):
            if volume_total == 0:
                st.error("Volume larutan tidak boleh 0")
            else:
                persen = (volume_zat / volume_total) * 100
                st.success(f"Konsentrasi = **{persen:.4f} % v/v**")


    elif sub == "Cari volume zat (mL)":
        persen = st.number_input(
            "Konsentrasi (% v/v)", min_value=0.0, format="%.4f"
        )
        volume_total = st.number_input(
            "Volume larutan (mL)", min_value=0.0, format="%.2f"
        )


        if st.button("Hitung volume zat"):
            volume_zat = (persen / 100) * volume_total
            st.success(f"Volume zat terlarut = **{volume_zat:.2f} mL**")


    else:  # Cari volume larutan
        persen = st.number_input(
            "Konsentrasi (% v/v)", min_value=0.0, format="%.4f"
        )
        volume_zat = st.number_input(
            "Volume zat terlarut (mL)", min_value=0.0, format="%.2f"
        )


        if st.button("Hitung volume larutan"):
            if persen == 0:
                st.error("Konsentrasi tidak boleh 0")
            else:
                volume_total = (volume_zat * 100) / persen
                st.success(f"Volume larutan = **{volume_total:.2f} mL**")

