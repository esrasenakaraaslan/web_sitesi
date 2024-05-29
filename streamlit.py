import streamlit as st

# Kullanıcılar ve iş ilanları için veri saklama
users = {"john": "password123", "emma": "abc123"}
jobs = [
    {"title": "Data Scientist", "company": "TechCorp", "location": "Remote", "salary": "$100,000"},
    {"title": "Software Engineer", "company": "SoftTech", "location": "New York", "salary": "$120,000"},
    {"title": "Product Manager", "company": "BigCo", "location": "San Francisco", "salary": "$150,000"},
]

# Ana sayfa
def home_page():
    st.title("FreshData İş İlanı Sitesi")
    st.markdown("""
        ### Hoş Geldiniz!
        Bu web sitesi aracılığıyla iş arayabilir ve ilan verebilirsiniz.
    """)
    if st.button("Giriş Yap"):
        login_page()

    if st.button("Kayıt Ol"):
        register_page()

# Giriş sayfası
def login_page():
    st.title("Giriş Yap")
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if username in users and users[username] == password:
            st.success(f"Başarıyla giriş yapıldı: {username}")
            job_board(username)
        else:
            st.error("Geçersiz kullanıcı adı veya şifre!")

# Kayıt sayfası
def register_page():
    st.title("Kayıt Ol")
    new_username = st.text_input("Yeni Kullanıcı Adı")
    new_password = st.text_input("Yeni Şifre", type="password")
    if st.button("Kayıt Ol"):
        if new_username in users:
            st.error("Bu kullanıcı adı zaten kullanılıyor!")
        else:
            users[new_username] = new_password
            st.success("Kayıt başarıyla tamamlandı! Lütfen giriş yapın.")
            login_page()

# İş ilanı panosu
def job_board(username):
    st.title("İş İlanları")
    st.markdown("### İş İlanları")
    for job in jobs:
        st.write(f"{job['title']}** - {job['company']} - {job['location']} - {job['salary']}")
        if st.button("Detayları Gör"):
            job_details(job, username)

# İş ilanı detayları sayfası
def job_details(job, username):
    st.title("İş İlanı Detayları")
    st.write(f"{job['title']}** - {job['company']} - {job['location']} - {job['salary']}")
    st.markdown("""
        ### Detaylar
        Bu alanda iş ilanının detayları yer alacak.
    """)
    if st.button("Başvur"):
        st.success("Başvurunuz alınmıştır!")
    if st.button("Favorilere Ekle"):
        st.success("İlan favorilere eklendi!")
        favorite_jobs(username, job)

# Favori iş ilanları sayfası
def favorite_jobs(username, job):
    st.title("Favori İş İlanları")
    st.write(f"{job['title']} - {job['company']} - {job['location']} - {job['salary']}")
    st.markdown("""
        ### Favori İlanlarınız
        Bu alanda favorilere eklediğiniz iş ilanlarınız listelenecek.
    """)
    if st.button("Başvur"):
        st.success("Başvurunuz alınmıştır!")

# Ana uygulama
def main():
    home_page()

if _name_ == "_main_":
    main()
