import streamlit as st
import pandas as pd

# Başlık ve Logo
st.markdown('<h1 class="header-title">FreshData</h1>', unsafe_allow_html=True)
st.markdown('<p class="slogan">Geleceğin İş Gücünü Keşfet</p>', unsafe_allow_html=True)
st.markdown('<img src="https://via.placeholder.com/800x200/FFC300/9b59b6?text=FreshData+İş+İlanı+Sitesi" style="width:100%; border-radius: 10px;">', unsafe_allow_html=True)

# İş Bul Bölümü
st.markdown('<h2 class="header-title">İş Bul</h2>', unsafe_allow_html=True)

# Veri Çekme
uploaded_file = st.file_uploader("Veri Dosyasını Yükle", type=["csv", "xlsx"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Konum ve Pozisyon Seçimi
    cities = data["Konum"].unique()
    selected_city = st.selectbox("Şehir Seçin", cities)

    positions = data["Pozisyon"].unique()
    selected_position = st.multiselect("Pozisyonlar Seçin", positions)

    # Filtreleme
    filtered_data = data[
        (data["Konum"] == selected_city) & (data["Pozisyon"].isin(selected_position))
    ]

    # Sonuçları Gösterme
    st.dataframe(filtered_data)

# Makine Öğrenmesi Bölümü
st.markdown('<h2 class="header-title">Makine Öğrenmesi</h2>', unsafe_allow_html=True)

def run_machine_learning_code():
    # Makine öğrenmesi kodlarını buraya ekleyin
    st.write("Makine öğrenmesi işlemleri burada gerçekleştirilecek")

if st.button("İş Bul", key="iş_bul_button"):
    # ... (Diğer İş Bul butonunun altındaki kodlar)
    run_machine_learning_code()  # Fonksiyonu çağırma

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# Makaleler Bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
if st.button("Makale 1"):
    st.markdown('''
    ## Bilişim Sektöründeki İstihdam Analizi
    ...
    ''', unsafe_allow_html=True)

# Makale 2
if st.button("Makale 2"):
    st.markdown('''
    ## Yapay Zeka ve İnsan Kaynakları: Geleceğin İş Gücü Yönetimi
    ...
    ''', unsafe_allow_html=True)

