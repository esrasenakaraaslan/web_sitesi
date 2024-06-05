import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# Özel CSS ile stil ayarları
st.markdown(
    """
    <style>
    body {
        background-image: url('https://resimlink.com/fng7xTi5Ec');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stButton>button {
        color: white;
        background-color: #9b59b6;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #ec407a;
    }
    .header-title {
        color: #9b59b6;
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-top: 20px;
    }
    .info-box {
        background-color: #ec407a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }
    .info-box p {
        margin: 0;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 12px;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlık
st.markdown('<h1 class="header-title">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

url = "https://raw.githubusercontent.com/esrasenakaraaslan/web_sitesi/main/.devcontainer/t%C3%BCm_veriler_doldurulmus.xlsx"

@st.cache_data
def load_data(url):
    return pd.read_excel(url)

# Üçlü kolonlar ve butonlar
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("İş Bul", key="iş_bul_button"):
        st.markdown('<div class="info-box"><p>Burada iş bulma işlevi gelecek.</p></div>', unsafe_allow_html=True)

with col2:
    if st.button("Meslek Grupları", key="meslek_grupları_button"):
        st.markdown('<div class="info-box"><p>Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

with col3:
    if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
        st.markdown('<div class="info-box"><p>Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p></div>', unsafe_allow_html=True)

# İş İlanları Grafikleri bölümü
if st.button("İş İlanları Grafikleri"):
    is_ilanlari = load_data(url)
    konum_sayilari = is_ilanlari['Konum'].value_counts()
    
    filtre = konum_sayilari / len(is_ilanlari) * 100 < 5
    filtrelenmis_konum_sayilari = konum_sayilari[~filtre]
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=filtrelenmis_konum_sayilari.index, y=filtrelenmis_konum_sayilari.values, palette="viridis")
    plt.title('Konumların Sayısı (Yüzde 5\'ten fazla olanlar)')
    plt.xlabel('Konumlar')
    plt.ylabel('Sayı')
    plt.xticks(rotation=90)
    st.pyplot(plt)

# Ek bir buton ve bilgi kutusu
st.markdown('<h2 class="header-title">Diğer İşlevler</h2>', unsafe_allow_html=True)

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div class="info-box"><p>Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)

# Görsel ekleme
st.markdown('<img src="https://via.placeholder.com/800x200/FFC300/9b59b6?text=FreshData+İş+İlanı+Sitesi" style="width:100%; border-radius: 10px;">', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
if st.button("Makale 1"):
    st.markdown('''
    ## Bilişim Sektöründeki İstihdam Analizi

    (Makale içeriği burada yer alacak)
    ''')

# Makale 2
if st.button("Makale 2"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 2</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Makale 3
if st.button("Makale 3"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 3</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Hakkımızda bölümü
if st.button("Hakkımızda"):
    st.markdown('''
    ## Bilişim Sektöründe Gelecek: Veri Analizi ve İş İlanları

    (Hakkımızda içeriği burada yer alacak)
    ''')
    
# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
