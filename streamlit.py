import streamlit as st

# main fonksiyonu tanımlama
def main():
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
            background-color: #1f77b4;
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
            background-color: #45a049;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .header-title {
            color: #1f77b4;
            font-family: 'Arial', sans-serif;
            margin-left: 10px;
        }
        .header-image {
            width: 50px;
            height: auto;
        }
        .info-box {
            background-color: #ffffff;
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

    # Üst kısım (header)
    st.markdown('<div class="header"><img src="https://via.placeholder.com/50x50.png?text=🍎" class="header-image"><h1 class="header-title">FreshData İş İlanı Sitesi</h1></div>', unsafe_allow_html=True)

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

    # Ek bir buton ve bilgi kutusu
    st.markdown('<h2 class="header-title">Diğer İşlevler</h2>', unsafe_allow_html=True)

    if st.button("İşveren Girişi", key="isveren_girisi_button"):
        st.markdown('<div class="info-box"><p>Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)

    # Görsel ekleme
    st.image("https://via.placeholder.com/800x200.png?text=FreshData+İş+İlanı+Sitesi", use_column_width=True)

    # Footer
    st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# main fonksiyonunu çağırma
if __name__ == "__main__":
    main()
