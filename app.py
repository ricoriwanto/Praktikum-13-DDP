import streamlit as st

# st.title("Hallo Gais")
# st.write("Apa Kabar?")
# st.image("DDP_13_Streamlit/image.jpg", caption="Ini Gambar")

# SideBar Directory
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama": [dashboard],
        "Transaksi": [nabung]
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()