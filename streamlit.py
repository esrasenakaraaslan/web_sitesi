import streamlit as st

# Başlık
st.title("Hoş Geldiniz")

# Metin içeriği
st.write("Bu basit bir web sitesi arayüzü örneğidir.")

# Butonlar
if st.button("İş Bul"):
    st.write("Burada iş bulma işlevi gelecek.")

if st.button("Meslek Grupları"):
    st.write("Burada meslek gruplarına göre iş arama işlevi gelecek.")

if st.button("Türkiye'nin Geldiği Son Nokta"):
    st.write("Burada Türkiye'nin geldiği son noktayla ilgili bilgiler yer alacak.")
