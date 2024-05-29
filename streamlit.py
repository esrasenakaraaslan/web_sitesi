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

# Görsel ekleme
st.markdown('<img src="https://via.placeholder.com/800x200/FFC300/9b59b6?text=FreshData+İş+İlanı+Sitesi" style="width:100%; border-radius: 10px;">', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 class="header-title">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 1</h3><p>Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Makale 2
st.markdown('<div class="info-box" style="background-color: #9b59b6;"><h3 style="color: #ec407a;">Başlık 2</h3><p>Bilişim Sektöründe Gelecek: Veri Analizi ve İş İlanları

Günümüzde teknoloji, iş dünyasını derinden etkileyen bir güç haline geldi. Özellikle bilişim sektörü, hızla büyüyen ve gelişen bir alandır. Bu alandaki eğilimleri anlamak ve geleceği öngörmek, hem iş arayanlar hem de işverenler için kritik öneme sahiptir.

Bilişimde Kariyer Yolculuğu

Bilişim sektöründe kariyer yapmak isteyenler için, doğru işi bulmak önemlidir. Ancak, doğru işi bulmak bazen zor olabilir. Bu noktada, veri analizi devreye girer. Veri analizi, iş ilanlarının analiz edilmesi ve sektördeki eğilimlerin belirlenmesi açısından büyük bir potansiyele sahiptir.

FreshData: İş Arayanlar İçin Yenilikçi Bir Platform

FreshData, iş arayanlara her konuda yardımcı olacak yenilikçi bir web sitesidir. Bilişim sektöründeki iş ilanlarını çıkarıp analiz ederek, iş arayanlara en güncel ve uygun iş fırsatlarını sunar. Aynı zamanda, bilişim sektörünün gelecekteki eğilimlerini belirlemek için veri analizi kullanır.

Veri Analizi ile Geleceği Öngörmek

FreshData'nın en güçlü yanlarından biri, veri analiziyle bilişim sektöründeki eğilimleri belirleyebilmesidir. Bu sayede, iş arayanlar hangi alanlarda daha fazla iş fırsatı bulabileceklerini önceden görebilirler. Ayrıca, işverenler de gelecekteki taleplerini daha iyi anlayarak doğru adımlar atabilirler.

Yaratıcı ve Renkli Bir Platform

FreshData, sadece iş ilanlarına odaklanmakla kalmaz, aynı zamanda kullanıcılarını eğlenceli ve etkileyici bir deneyim sunar. Pembe ve mor gibi canlı renkler kullanarak, platformun görünümü daha çekici hale getirilmiştir. Makaleler ve görsellerle desteklenen içerikler, kullanıcıların bilgiye daha kolay erişmesini sağlar.

Geleceğe Yönelik İşbirlikleri

FreshData, bilişim sektöründeki önde gelen şirketlerle işbirliği yaparak, kullanıcılarına daha fazla fırsat sunmayı hedefler. Ayrıca, veri analizi alanındaki uzmanlarla ortak projeler yürüterek, bilişim sektörünün geleceğine dair daha kapsamlı bir bakış açısı sağlar.

Sonuç

Bilişim sektöründe kariyer yapmak isteyenler ve işverenler için, doğru bilgiye erişmek büyük önem taşır. FreshData, veri analizi ve yenilikçi yaklaşımıyla bu ihtiyacı karşılar. Geleceğe yönelik işbirlikleri ve eğlenceli kullanıcı deneyimiyle, bilişim sektöründe yeni bir dönemi başlatır..</p></div>', unsafe_allow_html=True)

