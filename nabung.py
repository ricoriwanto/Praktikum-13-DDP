import streamlit as st 

st.title("Halaman Menabung")

with st.form("menabung"):
    nama = st.text_input("nama")
    jumlah = st.number_input("jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("tanggal")
    waktu = st.time_input("waktu")
    button = st.form_submit_button(label="menabung")
    
    if button and jumlah >= 50000:
        st.session_state['total_semua'].append({
            "Tipe" : "menabung",
            "jumlah" : jumlah
        })
        st.success("anda berhasil menabung")
    else:
        st.error("Kamu Gagal Menabung, Nominal kurang Dari 50000")
        
    