import streamlit as st

def main():
    st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")
    st.markdown(
        """
        <style>
        .fuşya {
            background-color: #864BD8;
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
