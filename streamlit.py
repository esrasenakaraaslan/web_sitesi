import streamlit as st
import pandas as pd
import os

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

# Excel dosyasının doğru yolu
excel_file_path = 'path_to_your_excel_file.xlsx'  # Excel dosyanızın yolu

# Dosya var mı kontrolü ve yükleme
if os.path.exists(excel_file_path):
    df = pd.read_excel(excel_file_path)

    # Arama ve filtreleme
    search = st.text_input('İş başlığına göre ara')
    location_filter = st.selectbox('Konuma göre filtrele', ['Hepsi'] + df['Konum'].unique().tolist())

    filtered_df = df

    if search:
        filtered_df = filtered_df[filtered_df['Başlık'].str.contains(search, case=False)]

    if location_filter != 'Hepsi':
        filtered_df = filtered_df[filtered_df['Konum'] == location_filter]

    st.dataframe(filtered_df)
else:
    st.error("Excel dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
