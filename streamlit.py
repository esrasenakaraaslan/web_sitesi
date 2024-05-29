import streamlit as st

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

# Hakkımızda butonu
button_click_counts = {"hakkimizda_button": 0}

if st.button("Hakkımızda", key="hakkimizda_button"):
    button_click_counts["hakkimizda_button"] += 1
    if button_click_counts["hakkimizda_button"] % 2 == 0:
        st.markdown('''
    ## Bilişim Sektöründe Gelecek: Veri Analizi ve İş İlanları

    ### Teknolojinin hızla gelişmesiyle birlikte, bilişim sektörü her geçen gün daha da önemli hale gelmektedir. Bu sektördeki değişim ve gelişim, hem iş arayanlar hem de işverenler için büyük fırsatlar ve zorluklar sunmaktadır. Veri analizi, bu alanda önemli bir rol oynamakta ve gelecekteki eğilimleri belirlemede kritik bir araç haline gelmektedir.

    #### Bilişimde Kariyer Yolculuğu

    Bilişim sektörü, hızla değişen ve gelişen bir alandır. Bu sektörde kariyer yapmak isteyenler için, doğru işi bulmak ve kendilerini sürekli olarak güncellemek önemlidir. Ancak, bilişim sektöründeki iş ilanlarını izlemek ve değerlendirmek karmaşık bir süreç olabilir.

    #### Veri Analiziyle Geleceği Anlamak

    Veri analizi, bilişim sektöründeki iş ilanlarını ve eğilimlerini anlamak için güçlü bir araçtır. İş ilanlarındaki trendleri analiz ederek, hangi beceri setlerinin ön plana çıktığını ve hangi alanlarda daha fazla talep olduğunu belirlemek mümkündür. Bu sayede, iş arayanlar kendilerini daha iyi yönlendirebilir ve işverenler doğru adayları bulabilir.

    #### Yenilikçi Bir Platform: FreshData

    FreshData, bilişim sektöründeki iş arayanlar için yenilikçi bir platformdur. Bu platform, iş ilanlarını derinlemesine analiz ederek kullanıcılarına en güncel bilgileri sunar. Aynı zamanda, bilişim sektörünün geleceğine dair öngörülerde bulunur ve kullanıcılarına bu konuda rehberlik eder.

    #### Kullanıcı Dostu Arayüz

    FreshData'nın kullanıcı dostu arayüzü, iş arayanların ve işverenlerin ihtiyaçlarına yönelik tasarlanmıştır. Kullanıcılar, kolayca istedikleri pozisyonları arayabilir, iş ilanlarını filtreleyebilir ve ilgilerini çeken içeriklere erişebilirler. Ayrıca, platformun görsel ve içerikleri kullanıcıların ilgisini çekmek için özenle seçilmiştir.

    #### Geleceğe Yönelik Bakış

    FreshData, bilişim sektörünün geleceğine yönelik bir bakış sunar. Veri analizi ve uzman görüşlerine dayanarak, sektördeki değişimleri ve gelecekteki trendleri tahmin etmeye çalışır. Bu sayede, hem iş arayanlar hem de işverenler geleceğe daha güvenle bakabilirler.

    ### Sonuç

    Bilişim sektörü, sürekli değişen ve gelişen bir alan olmaya devam edecektir. FreshData gibi platformlar, bu değişime ayak uydurmak isteyenler için değerli bir kaynak oluşturur. Veri analizi ve yenilikçi yaklaşımlarıyla, bilişim sektörünün geleceğini şekillendirmeye yardımcı olurlar.
    ''')
else:
        st.markdown("")        

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

    1. *Yazılım Mühendisi*
    2. *Gömülü Yazılım Mühendisi*
    3. *Yazılım Geliştirme Uzmanı*
    4. *Yazılım Uzmanı*
    5. *Bilgi Teknolojileri Uzman Yardımcısı*
    6. *Yazılım Destek Uzmanı*
    7. *İş Geliştirme Uzmanı*
    8. *İş Analisti*
    9. *ERP Uzmanı*
    10. *Proje Yöneticisi / Yönetmeni*

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

    İş geliştirme uzmanları ve iş analistleri, şirketlerin büyüme ve stratejik hedeflerine ulaşmasında önemli rol oynarlar. Pandemi sonrasında değişen pazar dinamikleri ve yeni iş modelleri, bu uzmanlıklara olan talebi artırmıştır.

    #### ERP Uzmanı

    ERP (Kurumsal Kaynak Planlaması) uzmanları, şirketlerin operasyonel süreçlerini optimize eder ve verimliliği artırır. Pandemi sürecinde tedarik zincirlerinde yaşanan aksaklıklar, ERP çözümlerine olan ihtiyacı ve dolayısıyla bu alandaki uzmanlara olan talebi yükseltmiştir.

    #### Proje Yöneticisi / Yönetmeni

    Proje yöneticileri, projelerin zamanında ve bütçeye uygun bir şekilde tamamlanmasını sağlar. Pandemi sonrası dönemde dijital dönüşüm projelerinin artması, bu pozisyonlara olan talebi artırmıştır.

    ### İstanbul ve Ankara Çevresindeki İstihdam Olanakları

    İstanbul ve Ankara'nın yanı sıra bu şehirlere yakın illerde de bilişim sektöründe önemli istihdam olanakları bulunmaktadır. Bu bölgeler, büyük şehirlerdeki yoğun iş yükünü paylaşmakta ve geniş bir yetenek havuzuna erişim sağlamaktadır. Özellikle teknoloji geliştirme bölgeleri ve teknoparklar, bu alanlarda önemli iş fırsatları sunmaktadır.

    ### Sonuç

    Pandemi sonrası dönemde bilişim sektöründe istihdam dinamikleri önemli değişiklikler göstermiştir. İstanbul ve Ankara başta olmak üzere, bu şehirlerin çevresindeki illerde de bilişim sektöründe geniş iş imkanları bulunmaktadır. Yazılım mühendisleri, yazılım geliştirme uzmanları, ERP uzmanları ve proje yöneticileri gibi meslek grupları, en çok talep gören pozisyonlar arasında yer almaktadır. Bu makalede ele alınan analizler, bilişim sektöründeki istihdam olanaklarını ve pandemi sonrası dönemdeki değişimleri ortaya koymaktadır.

    ### Kaynakça

    * Türkiye İstatistik Kurumu (TÜİK) verileri
    * İşkur iş ilanları ve istihdam raporları
    * Bilişim sektörü analiz raporları
    * Şirketlerin yayınladığı iş ilanları ve istihdam verileri

    Bu makale, Türkiye'deki bilişim sektöründe istihdam dinamiklerini anlamak ve gelecekteki eğilimleri öngörmek için önemli bir kaynak sunmaktadır.
    ''')

# Makale 2
if st.button("Makale 2"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 2</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Makale 3
if st.button("Makale 3"):
    st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 3</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
