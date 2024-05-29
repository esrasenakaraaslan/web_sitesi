import streamlit as st

# Uygulama başlığı ve alt başlık
st.title("FreshData İş İlanı Sitesi")
st.markdown("""
    ### Hoş Geldiniz!
    Bu web sitesi aracılığıyla iş arama ve bilgi edinme işlevlerini kullanabilirsiniz.
""")

# Arka plan rengi ve resmi
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        background-image: url("https://via.placeholder.com/1200x400.png?text=FreshData+İş+İlanı+Sitesi");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ana menü
menu = st.radio("Menü", ("İş Bul", "Meslek Grupları", "Türkiye'nin Durumu"))

# İş Bul seçeneği
if menu == "İş Bul":
    st.header("İş Bulma İşlevi")
    st.write("Burada iş bulma işlevi gelecek.")

# Meslek Grupları seçeneği
elif menu == "Meslek Grupları":
    st.header("Meslek Gruplarına Göre İş Arama")
    st.write("Burada meslek gruplarına göre iş arama işlevi gelecek.")

# Türkiye'nin Durumu seçeneği
elif menu == "Türkiye'nin Durumu":
    st.header("Türkiye'nin Durumu")
    st.write("Burada Türkiye'nin geldiği son noktayla ilgili bilgiler yer alacak.")

# Alt menü
if st.sidebar.checkbox("Ayarlar"):
    st.sidebar.subheader("Ayarlar")
    st.sidebar.checkbox("Karanlık Modu")
    st.sidebar.selectbox("Dil Seçimi", ["Türkçe", "İngilizce", "Almanca"])

# Footer
st.markdown("""
---
© 2024 FreshData. Tüm hakları saklıdır.
""")
