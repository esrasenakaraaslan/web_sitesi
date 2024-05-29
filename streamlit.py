import streamlit as st
import pandas as pd

# Arka plan rengini belirleyen stil
page_bg_img = '''
<style>
body {
background: linear-gradient(to right, #ff7e5f, #feb47b);
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Excel dosyasından veri okuma
data_path = "C:/Users/esras/OneDrive/Desktop/fresh data/tüm_veriler_doldurulmus.xlsx"
df = pd.read_excel(data_path)

st.title("İş İlanı Bulma Sitesi")

# Kullanıcıdan filtreleme için bilgi al
st.sidebar.header("Arama Filtreleri")
job_type = st.sidebar.selectbox("İş Türü", df['job_type'].unique())
location = st.sidebar.selectbox("Lokasyon", df['location'].unique())

# Filtrelenmiş veriyi göster
filtered_df = df[(df['job_type'] == job_type) & (df['location'] == location)]

st.subheader(f"İş İlanları: {job_type} - {location}")
st.dataframe(filtered_df)

# İlan detayları
for i, row in filtered_df.iterrows():
    st.markdown(f"### {row['job_title']}")
    st.write(f"**Şirket:** {row['company_name']}")
    st.write(f"**Lokasyon:** {row['location']}")
    st.write(f"**Açıklama:** {row['job_description']}")
    st.write("---")


