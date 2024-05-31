import streamlit as st
import pandas as pd
import requests
from io import BytesIO

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

# GitHub'dan Excel dosyasını yükleme
excel_url = 'https://raw.githubusercontent.com/esrasenakaraaslan/web_sitesi/main/tm_veriler.xlsx'

try:
    response = requests.get(excel_url)
    response.raise_for_status()  # HTTP hatalarını kontrol et
    excel_data = BytesIO(response.content)
    df = pd.read_excel(excel_data)
    st.dataframe(df)
except requests.exceptions.RequestException as e:
    st.error(f"Dosya indirilirken bir hata oluştu: {e}")

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
st.markdown('<img src="https://via.placeholder.com/800x200/FFC300/9b59b6?text=FreshData+İş+İlanı+Sitesi" style="width:100%; border-radius: 10px;">', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
if st.button("Makale 1"):
    st.markdown('''
    ## Bilişim Sektöründeki İstihdam Analizi

    ### Giriş

    Bilişim sektörü, teknolojik gelişmelerin hız kesmeden devam ettiği günümüz dünyasında ekonomik büyümenin itici güçlerinden biri haline gelmiştir. Özellikle pandemi süreci, dijitalleşmenin ve uzaktan çalışmanın önemini artırmış ve bilişim sektörüne olan talebi daha da yükseltmiştir. Bu makalede, pandemi sonrasında Türkiye'nin özellikle İstanbul, Ankara ve çevre illerinde bilişim sektöründeki istihdamın analizini yaparak, hangi meslek gruplarının en çok rağbet gördüğünü inceleyeceğiz.

    ### Pandemi Sonrası İstihdam Dinamikleri

    Pandemi sürecinde uzaktan çalışma modeline hızlı bir geçiş yaşandı. Ancak pandemi sonrası dönemde, şirketlerin hibrit çalışma modellerini benimsemesiyle birlikte çalışanlar tekrar iş yerlerine dönmeye başladı. Bu dönüş, bilişim sektöründe istihdam dinamiklerini önemli ölçüde etkiledi. Türkiye'nin başkenti Ankara ve en büyük şehri İstanbul, bilişim sektöründe iş ilanlarının yoğunlaştığı bölgeler olarak dikkat çekmektedir. Bu şehirler, büyük teknolojik şirketlerin merkezlerine ev sahipliği yapmakta ve bu nedenle iş fırsatlarının bol olduğu yerlerdir. 

    ### İstanbul ve Ankara'daki İstihdam Fırsatları

    İstanbul ve Ankara, Türkiye'nin teknoloji ve inovasyon merkezleri olarak öne çıkmaktadır. Bu şehirlerdeki bilişim sektörü, geniş bir yelpazede iş imkanları sunmaktadır. Aşağıdaki meslek grupları, pandemi sonrası dönemde en çok rağbet gören pozisyonlar arasında yer almaktadır:

    1. Yazılım Mühendisi
    2. Gömülü Yazılım Mühendisi
    3. Yazılım Geliştirme Uzmanı
    4. Yazılım Uzmanı
    5. Bilgi Teknolojileri Uzman Yardımcısı
    6. Yazılım Destek Uzmanı
    7. İş Geliştirme Uzmanı
    8. İş Analisti
    9. ERP Uzmanı
    10. Proje Yöneticisi / Yönetmeni

    ### Meslek Gruplarının Detaylı Analizi

    #### Yazılım Mühendisi ve Yazılım Uzmanı

    Yazılım mühendisleri ve yazılım uzmanları, bilişim sektörünün belkemiğini oluşturan pozisyonlardır. Bu uzmanlar, çeşitli yazılım çözümleri geliştirir, mevcut sistemleri iyileştirir ve yeni teknolojileri entegre ederler. Pandemi sonrasında artan dijitalleşme talebi, yazılım mühendislerine olan ihtiyacı artırmıştır.

    #### Gömülü Yazılım Mühendisi

    Gömülü yazılım mühendisleri, donanım ve yazılımın entegrasyonunu sağlayan kritik pozisyonlardır. Akıllı cihazlar ve IoT (Nesnelerin İnterneti) çözümlerinin yaygınlaşması, bu alandaki uzmanlara olan talebi yükseltmiştir.

    #### Yazılım Geliştirme Uzmanı

    Yazılım geliştirme uzmanları, uygulama geliştirme sürecinde önemli rol oynarlar. Agile ve DevOps gibi modern yazılım geliştirme metodolojileriyle uyumlu çalışan bu uzmanlar, pandemi sonrası artan dijital dönüşüm projeleri için kritik öneme sahiptir.

    #### Bilgi Teknolojileri Uzman Yardımcısı ve Yazılım Destek Uzmanı

    Bilgi teknolojileri uzman yardımcıları ve yazılım destek uzmanları, şirketlerin teknik operasyonlarının sürekliliğini sağlar. Pandemi sonrasında uzaktan çalışma ve hibrit modellerin yaygınlaşması, bu pozisyonların önemini artırmıştır.

    #### İş Geliştirme Uzmanı ve İş Analisti

    İş geliştirme uzmanları ve
    # İş Geliştirme Uzmanı ve İş Analisti
    iş geliştirme uzmanları ve iş analistleri, iş süreçlerini iyileştirmek ve şirket stratejilerini geliştirmek için çalışırlar. Pandemi sonrası dönemde, şirketlerin rekabet gücünü artırmak için bu uzmanlara olan talep artmıştır.

    #### ERP Uzmanı ve Proje Yöneticisi / Yönetmeni

    ERP uzmanları, şirketlerin iş süreçlerini yöneten ve optimize eden sistemlerin kurulumu ve bakımından sorumludur. Proje yöneticileri / yönetmenleri ise büyük ölçekli dijital dönüşüm projelerini yönetirler. Bu pozisyonlar, pandemi sonrası dönemde işletmelerin verimliliğini artırmak için kritik öneme sahiptir.

    ### Sonuç

    Türkiye'de bilişim sektöründeki istihdam, pandemi sonrası dönemde önemli değişiklikler yaşamaktadır. Ankara ve İstanbul gibi büyük şehirlerde, yazılım mühendisleri, iş analistleri, proje yöneticileri ve ERP uzmanları gibi pozisyonlara olan talep artmaktadır. Bu süreçte, bilişim sektöründeki iş arayanlar için çeşitli fırsatlar bulunmaktadır.
    </div>
    ''', unsafe_allow_html=True)

# Makale 2
if st.button("Makale 2"):
    st.markdown('''
    ## Yapay Zeka ve İnsan Kaynakları: Geleceğin İş Gücü Yönetimi

    ### Giriş

    Yapay zeka (YZ), son yıllarda iş dünyasında büyük bir devrim yaratmıştır. Özellikle insan kaynakları yönetimi gibi alanlarda, YZ'nin kullanımı iş süreçlerini optimize etmekte ve verimliliği artırmaktadır. Bu makalede, yapay zeka destekli insan kaynakları yönetiminin önemi ve gelecekte iş gücü yönetimindeki rolü ele alınacaktır.

    ### Yapay Zeka Destekli İK Yönetimi

    Geleneksel insan kaynakları yönetimi süreçleri, genellikle zaman alıcı ve tekrarlı işleri içerir. Mülakatlar, iş ilanlarının yayınlanması, CV taraması ve performans değerlendirmeleri gibi işlemler, insan kaynakları departmanlarının önemli bir zamanını alır. Yapay zeka, bu süreçleri otomatikleştirerek ve veri odaklı kararlar alınmasını sağlayarak iş gücü yönetiminde devrim yaratmaktadır.

    ### Geleceğin İK Trendleri

    Yapay zeka destekli İK yönetimi, geleceğin iş dünyasında önemli bir trend haline gelmektedir. Bu trendin ana unsurlarından biri, işe alım süreçlerinde yapay zeka tabanlı analitik araçların kullanılmasıdır. Bu araçlar, adayların yeteneklerini, deneyimlerini ve uygunluğunu değerlendirmek için büyük veri analizini kullanır. Böylece, işe alım süreçleri daha objektif ve verimli hale gelir.

    ### İK Yönetiminde Yapay Zeka Etik Sorunları

    Yapay zeka kullanımının artmasıyla birlikte, İK yönetiminde bazı etik sorunlar ortaya çıkmaktadır. Örneğin, yapay zeka algoritmalarının cinsiyet, yaş, ırk gibi öznelliklere dayalı olarak ayrımcılık yapma riski bulunmaktadır. Bu nedenle, yapay zeka destekli İK sistemlerinin geliştirilmesi ve uygulanması sırasında etik standartlara uyulması büyük önem taşır.

    ### Sonuç

    Yapay zeka, insan kaynakları yönetimi alanında büyük bir potansiyele sahiptir. Gelecekte, işe alım, performans yönetimi, eğitim ve gelişim gibi İK süreçlerinde yapay zeka tabanlı çözümlerin yaygınlaşması beklenmektedir. Ancak, bu teknolojinin etik ve güvenlik sorunları da dikkate alınmalı ve uygun önlemler alınmalıdır.
    </div>
    ''', unsafe_allow_html=True)
