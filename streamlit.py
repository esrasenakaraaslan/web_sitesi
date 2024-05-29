import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# CSS for custom styling
st.markdown(
    """
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
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
    st.title("Merhaba, Dünya!")
    st.write("Streamlit ile GitHub üzerinden web uygulamanızı oluşturuyorsunuz.")
    
    if st.button('Tıklayın'):
        st.write('Butona tıkladınız!')
    
    option = st.selectbox(
        'Bir seçenek belirleyin:',
        ['Seçenek 1', 'Seçenek 2', 'Seçenek 3']
    )
    st.write('Seçtiğiniz:', option)
    
    number = st.slider('Bir sayı seçin:', 0, 100, 50)
    st.write('Seçtiğiniz sayı:', number)
    
    # Plotly chart
    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Iris Dataset Scatter Plot")
    st.plotly_chart(fig)

elif selection == "İletişim":
    st.title("İletişim")
    st.write("Bize ulaşmak için aşağıdaki formu doldurun.")
    st.text_input("Adınız")
    st.text_input("E-posta Adresiniz")
    st.text_area("Mesajınız")
    if st.button('Gönder'):
        st.write("Mesajınız gönderildi!")

# Custom card
st.markdown(
    """
    <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Özel Kart Başlığı</h3>
        <p>Bu özel kart içeriğidir.</p>
    </div>
    """,
    unsafe_allow_html=True
)
