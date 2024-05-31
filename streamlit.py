import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Excel dosyasını yükleme
uploaded_file = st.file_uploader("Excel dosyasını yükleyin", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Veri görselleştirme
        st.markdown('<h2 class="header-title">Veri Görselleştirme</h2>', unsafe_allow_html=True)

        for column in df.columns:
            if df[column].dtype in ['int64', 'float64']:
                fig, ax = plt.subplots()
                df[column].plot(kind='hist', ax=ax)
                plt.title(f"{column} Dağılımı")
                plt.xlabel(column)
                plt.ylabel("Frekans")
                st.pyplot(fig)

    except Exception as e:
        st.error(f"Hata: {e}")

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

