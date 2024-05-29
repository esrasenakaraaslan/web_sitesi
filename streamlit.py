import streamlit as st

# Butonların durumunu izlemek için değişkenler
is_button_clicked = {
    "iş_bul_button": False,
    "meslek_grupları_button": False,
    "son_nokta_button": False,
    "isveren_girisi_button": False,
    "hakkimizda_button": False,
}

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

# Üçlü kolonlar ve butonlar
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("İş Bul", key="iş_bul_button"):
        if is_button_clicked["iş_bul_button"]:
            is_button_clicked["iş_bul_button"] = False
        else:
            is_button_clicked["iş_bul_button"] = True

with col2:
    if st.button("Meslek Grupları", key="meslek_grupları_button"):
        if is_button_clicked["meslek_grupları_button"]:
            is_button_clicked["meslek_grupları_button"] = False
        else:
            is_button_clicked["meslek_grupları_button"] = True

with col3:
    if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
        if is_button_clicked["son_nokta_button"]:
            is_button_clicked["son_nokta_button"] = False
        else:
            is_button_clicked["son_nokta_button"] = True

# Ek bir buton ve bilgi kutusu
st.markdown('<h2 class="header-title">Diğer İşlevler</h2>', unsafe_allow_html=True)

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    if is_button_clicked["isveren_girisi_button"]:
        is_button_clicked["isveren_girisi_button"] = False
    else:
        is_button_clicked["isveren_girisi_button"] = True

# Hakkımızda butonu
if st.button("Hakkımızda", key="hakkimizda_button"):
    if is_button_clicked["hakkimizda_button"]:
        is_button_clicked["hakkimizda_button"] = False
    else:
        is_button_clicked["hakkimizda_button"] = True

# Görsel ekleme
st.markdown('<img src="https://via.placeholder.com/800x200/FFC300/9b59b6?text=FreshData+İş+İlanı+Sitesi" style="width:100%; border-radius: 10px;">', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
if st.button("Makale 1"):
    if is_button_clicked["makale_1_button"]:
        is_button_clicked["makale_1_button"] = False
    else:
        is_button_clicked["makale_1_button"] = True

# Makale 2
if st.button("Makale 2"):
    if is_button_clicked["makale_2_button"]:
        is_button_clicked["makale_2_button"] = False
    else:
        is_button_clicked["makale_2_button"] = True

# Makale 3
if st.button("Makale 3"):
    if is_button_clicked["makale_3_button"]:
        is_button_clicked["makale_3_button"] = False
    else:
        is_button_clicked["makale_3_button"] = True

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
