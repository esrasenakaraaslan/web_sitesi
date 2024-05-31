import streamlit as st
import pandas as pd

# Veri
data = pd.read_csv("ilanlar.csv")  # İş ilanlarını içeren CSV dosyasını okuyun

# Uygulama başlığı ve alt başlık
st.title("FreshData İş İlanı Sitesi")
st.markdown("""
  ### Hoş Geldiniz!
  Bu web sitesi aracılığıyla iş arama ve bilgi edinme işlevlerini kullanabilirsiniz.
""")

# Arka plan rengi ve resmi
st.markdown(
  """
  <style>
  body {
    background-color: #f0f2f6;
  }
  .stApp {
    background-image: url("ilan_arkaplani.jpg");  # Gerçek resim dosyasının adını ve yolunu kullanın
    background-size: cover;
  }
  .button {
    background-color: #1f77b4;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  .button:hover {
    background-color: #45a049;
  }
  </style>
  """,
  unsafe_allow_html=True
)

# Ana menü
menu = st.radio("Menü", ("İş Bul", "Meslek Grupları", "Türkiye'nin Durumu", "Hakkımızda"))

# İş Bul seçeneği
if menu == "İş Bul":
  st.header("İş Bulma İşlevi")
  ilan_secimi = st.selectbox("Meslek Grubu Seçiniz", data["Meslek Grubu"].unique())
  ilanlar = data[data["Meslek Grubu"] == ilan_secimi]
  st.write(ilanlar)
  if st.button("Başvur", key="iş_bul_button"):
    st.write("Burada iş bulma işlevi gelecek.")

# Meslek Grupları seçeneği
elif menu == "Meslek Grupları":
  st.header("Meslek Gruplarına Göre İş Arama")
  meslek_gruplari = data["Meslek Grubu"].unique()
  for grup in meslek_gruplari:
    st.subheader(grup)
    st.write(data[data["Meslek Grubu"] == grup])

# Türkiye'nin Durumu seçeneği
elif menu == "Türkiye'nin Durumu":
  st.header("Türkiye'nin Durumu")
  # Burada Türkiye'nin durumu ile ilgili verileri gösterin
  st.write("Türkiye'nin geldiği son noktayla ilgili bilgiler yer alacak.")

# Hakkımızda seçeneği
elif menu == "Hakkımızda":
  st.header("Hakkımızda")
  st.write("""
  FreshData, iş arayanlar ve işverenler arasında köprü oluşturan bir platformdur.
  Misyonumuz, iş arayanlara istedikleri işi bulmaları konusunda destek olmak ve işverenlere kaliteli iş gücü sağlamaktır.
  """)

# Ayarlar bölümü
st.sidebar.header("Ayarlar")
karanlik_mod = st.sidebar.checkbox("Karanlık Modu")
dil_secimi = st.sidebar.selectbox("Dil Seçimi", ["Türkçe", "İngilizce", "Almanca"])

# Karanlık Mod uygulaması
if karanlik_mod:
  st.markdown(
    """
    <style>
    body {
      background-color: #212121;
      color: #ffffff;
    }
    .stApp {
      background-color: #333333;
    }
    .button {
      background-color: #007bff;
      color: white;
    }
    .button:hover {
      background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
  )

