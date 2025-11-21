import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="page/page2.py", title="Visualisasi Data", icon="📊"),
    st.Page(page="page/page3.py", title="Settings", icon="⚙️"),
]

pg = st.navigation(
    pages,
    position
    