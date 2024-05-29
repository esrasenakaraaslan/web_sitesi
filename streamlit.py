import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
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
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSidebar .css-1d391kg {
        background-color: #e1e8ed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Menü")
selection = st.sidebar.radio("Sayfa Seç", ["Ana Sayfa", "İletişim"])

# Main Page
if selection == "Ana Sayfa":
    st.title("Profesyonel ve Estetik Streamlit Web Sitesi")
    st.write("Bu web sitesi, Streamlit kullanılarak oluşturulmuş profesyonel ve estetik bir web sitesidir.")
    
    st.header("Etkileşimli Bileşenler")
    
    if st.button('Tıklayın'):
        st.write('Butona tıkladınız!')
    
    option = st.selectbox(
        'Bir seçenek belirleyin:',
        ['Seçenek 1', 'Seçenek 2', 'Seçenek 3']
    )
    st.write('Seçtiğiniz:', option)
    
    number = st.slider('Bir sayı seçin:', 0, 100, 50)
    st.write('Seçtiğiniz sayı:', number)
    
    st.header("Görselleştirme")
    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Iris Dataset Scatter Plot")
    st.plotly_chart(fig)

elif selection == "İletişim":
    st.title("İletişim")
    st.write("Bize ulaşmak için aşağıdaki formu doldurun.")
    name = st.text_input("Adınız")
    email = st.text_input("E-posta Adresiniz")
    message = st.text_area("Mesajınız")
    if st.button('Gönder'):
        st.write("Mesajınız gönderildi!")
        st.write(f"Ad: {name}")
        st.write(f"E-posta: {email}")
        st.write(f"Mesaj: {message}")

# Custom card
st.markdown(
    """
    <div style="padding: 20px; border-radius: 10px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-top: 20px;">
        <h3>Özel Kart Başlığı</h3>
        <p>Bu özel kart içeriğidir. Kartın stilini değiştirmek için CSS kullanabilirsiniz.</p>
    </div>
    """,
    unsafe_allow_html=True
)
