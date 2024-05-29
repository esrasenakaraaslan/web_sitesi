import streamlit as st

def main():
    st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

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
            transition-duration: 0.4s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSidebar .css-1d391kg {
            background-color: #e1e8ed;
        }
        .header-title {
            color: #1f77b4;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .info-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="header-title">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("İş Bul", key="iş_bul_button"):
            st.markdown('<div class="info-box">Burada iş bulma işlevi gelecek.</div>', unsafe_allow_html=True)

    with col2:
        if st.button("Meslek Grupları", key="meslek_grupları_button"):
            st.markdown('<div class="info-box">Burada meslek gruplarına göre iş arama işlevi gelecek.</div>', unsafe_allow_html=True)

    with col3:
        if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
            st.markdown('<div class="info-box">Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</div>', unsafe_allow_html=True)

if _name_ == "_main_":
    main()
