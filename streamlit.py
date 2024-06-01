import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

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

@st.cache
def load_data(url):
    return pd.read_excel(url)

data = load_data(url)

# Kategorik verileri sayısal verilere dönüştürün
le_konum = LabelEncoder()
le_pozisyon = LabelEncoder()
le_calismasekli = LabelEncoder()

data['Konum'] = le_konum.fit_transform(data['Konum'])
data['Pozisyon'] = le_pozisyon.fit_transform(data['Pozisyon'])
data['çalışma şekli'] = le_calismasekli.fit_transform(data['çalışma şekli'])

# Üçlü kolonlar ve butonlar
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("İş Bul", key="iş_bul_button"):
        st.markdown('<div class="info-box"><p>Burada iş bulma işlevi gelecek.</p></div>', unsafe_allow_html=True)
        
        # İş Bul butonunun altındaki butonlar
        konum_secim = st.selectbox("Konum Seçin", le_konum.classes_)
        pozisyon_secim = st.selectbox("Pozisyon Seçin", le_pozisyon.classes_)
        calisma_sekli_secim = st.selectbox("Çalışma Şeklini Seçin", le_calismasekli.classes_)
        
        if st.button("Sonuçları Getir", key="sonuclari_getir_button"):
            st.markdown('<div class="info-box"><p>Sonuçlar getiriliyor...</p></div>', unsafe_allow_html=True)
            
            # Seçilen pozisyonun kodunu al
            meslek_kodu = le_pozisyon.transform([pozisyon_secim])[0]

            # Meslek koduna göre veriyi filtrele
            meslek_data = data[data['Pozisyon'] == meslek_kodu]

            # Şehirlerdeki bulma olasılıklarını hesaplayın
            X = meslek_data[['Konum', 'çalışma şekli']]
            y = meslek_data['Konum']

            model = RandomForestClassifier(random_state=42)
            model.fit(X, y)

            city_probabilities = pd.DataFrame(model.predict_proba(X), columns=le_konum.inverse_transform(model.classes_))

            # Şehirlerdeki bulma olasılıklarını sıralayın
            top_cities = city_probabilities.mean().sort_values(ascending=False).head(10)

            st.write(f"{pozisyon_secim} mesleği için en çok bulunan 10 şehir ve bulma olasılıkları:\n")
            st.write(top_cities)

with col2:
    if st.button("Meslek Grupları", key="meslek_grupları_button"):
        st.markdown('<div class="info-box"><p>Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

with col3:
    if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
        st.markdown('<div class="info-box"><p>Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p></div>', unsafe_allow_html=True)

# Ek bir buton ve bilgi kutusu
st.markdown('<h2 class="header-title">Diğer İşlevler</h2>', unsafe_allow_html=True)

# İşveren Girişi butonu
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
    ...
    ''', unsafe_allow_html=True)

# Makale 2
if st.button("Makale 2"):
    st.markdown('''
    ## Yapay Zeka ve İnsan Kaynakları: Geleceğin İş Gücü Yönetimi
    ...
    ''', unsafe_allow_html=True)


