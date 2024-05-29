import streamlit as st
col1, col2 = st.columns(2)
with col1:
    st.header("Sütun 1")
    st.write("Bu sütun 1'deki içerik.")
with col2:
    st.header("Sütun 2")
    st.write("Bu sütun 2'deki içerik.")
