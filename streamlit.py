import streamlit as st

def main():
    st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")
    st.markdown(
        """
        <style>
        .fuşya {
            background-color: #FF007F;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("FreshData İş İlanı Sitesi")

    if st.button("İş Bul", key="iş_bul_button"):
        st.write("Burada iş bulma işlevi gelecek.")

    if st.button("Meslek Grupları", key="meslek_grupları_button"):
        st.write("Burada meslek gruplarına göre iş arama işlevi gelecek.")

    if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
        st.write("Burada Türkiye'nin geldiği son noktayla ilgili bilgiler yer alacak.")

if __name__ == "__main__":
    main() 
import pandas as pd

# GitHub üzerinden veri setini yükleme
data_url = 'https://github.com/esrasenakaraaslan/datasetim/blob/main/t%C3%BCm_veriler_doldurulmus.xlsx'
df = pd.read_csv(data_url)

# Veri setini kullanarak işlemleri gerçekleştirme
# Örneğin:
st.write(df.head())

