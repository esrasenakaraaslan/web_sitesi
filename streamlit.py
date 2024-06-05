import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# Butonlar ve işlevleri
if st.button("İş Bul", key="iş_bul_button"):
    st.markdown('<div class="info-box"><p>Burada iş bulma işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Meslek Grupları", key="meslek_grupları_button"):
    st.markdown('<div class="info-box"><p>Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
    st.markdown('<div class="info-box"><p>Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p></div>', unsafe_allow_html=True)

if st.button("Analiz"):
    st.markdown('<div class="info-box"><p>Burada veri analizi işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Grafikler"):
    st.markdown('<div class="info-box"><p>Burada grafikler çizme işlevi gelecek.</p></div>', unsafe_allow_html=True)
    # Grafik çizme işlevi buraya eklenecek
    data = pd.read_excel("veri_seti.xlsx")

    # Grafik çizme işlevi
    def draw_bar_chart():
        # Konum sütununda en çok tekrar eden 5 değeri bul
        top_locations = data['Konum'].value_counts().head(5)

        # Çubuk grafiği oluştur
        fig, ax = plt.subplots()
        top_locations.plot(kind='bar', ax=ax, color='#9b59b6')
        ax.set_xlabel('Konum')
        ax.set_ylabel('Frekans')
        ax.set_title('En Çok Tekrar Eden 5 Konum')
        st.pyplot(fig)

    draw_bar_chart()

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div class="info-box"><p>Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

if st.button("Makale 1"):
    st.markdown('''
    ## Bilişim Sektöründeki İstihdam Analizi

    ### Giriş
    ...
    ''')

if st.button("Makale 2"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 2</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

if st.button("Makale 3"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 3</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Hakkımızda bölümü
if st.button("Hakkımızda"):
    st.markdown('''
    ## Bilişim Sektöründe Gelecek: Veri Analizi ve İş İlanları
    ...
    ''')
    # Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

