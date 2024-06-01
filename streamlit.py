import streamlit as st
import pandas as pd

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# Özel CSS ile stil ayarları
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background-color: #9b59b6; /* Mor renk */
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
        background-color: #ec407a; /* Pembe renk */
    }
    .header-title {
        color: #9b59b6; /* Mor renk */
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-top: 20px;
    }
    .info-box {
        background-color: #ec407a; /* Pembe renk */
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

data = load_data(url)

# Üçlü kolonlar ve butonlar
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("İş Bul", key="iş_bul_button"):
        st.markdown('<div class="info-box"><p>Burada iş bulma işlevi gelecek.</p></div>', unsafe_allow_html=True)

        # İş Bul butonunun altındaki butonlar
        if st.button("Konum", key="konum_button"):
            st.markdown('<div class="info-box"><p>Konuma göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

        if st.button("Pozisyon", key="pozisyon_button"):
            st.markdown('<div class="info-box"><p>Pozisyona göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

        if st.button("Çalışma Şekli", key="calisma_sekli_button"):
            st.markdown('<div class="info-box"><p>Çalışma şekline göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

with col2:
    if st.button("Meslek Grupları", key="meslek_grupları_button"):
        st.markdown('<div class="info-box"><p>Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

with col3:
    if st.button("Türkiye'nin
