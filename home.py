import streamlit as st
#________________________________________________________________________________________________
# Page Style
st.markdown("""
<style>
/* Background color */
.stApp {
    background-color: #654f41;
}

/* Title styling */
h1 {
    text-align: center;
    color: white !important;
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    background-color: #1f6feb;
    color: white;
    border-radius: 12px;
    height: 48px;
    border: none;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #388bfd;
    transform: translateY(-2px);
}

/* Link buttons */
.stLinkButton a {
    background-color: #1f6feb !important;
    color: white !important;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Link button hover */
.stLinkButton a:hover {
    background-color: #388bfd !important;
    transform: translateY(-2px);
}

/* Login container */
[data-testid="stContainer"] {
    background-color: rgba(20,20,30,0.75);
    padding: 25px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# _________________________________________________________________________________________________________
# Header
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "https://www.spellenhuis.nl/media/8a/65/ae/1634638327/spellenhuislogo.png",
        width=200
    )
    

# _________________________________________________________________________________________________________
# Main

st.title("Guru's Only")

CORRECT_PASSWORD = st.secrets["guru_password"]

sheet_link_data = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"
sheet_link_edit = "https://docs.google.com/spreadsheets/d/10kSJ04j7sNsXuXEinq5sVI_ToM13g8RroU0lSbmic0Y/edit?gid=0#gid=0"

if "login_clicked" not in st.session_state:
    st.session_state.login_clicked = False


col1, col2, col3 = st.columns(3)

with col2:
    if st.button("Naar Game Library"):
        st.session_state.login_clicked = True

with col1:
    st.link_button("Spel Opmerking Toevoegen", sheet_link_edit)


if st.session_state.login_clicked:
    password = st.text_input("Wachtwoord", type="password")

    if st.button("Login"):
        if password == CORRECT_PASSWORD:
            st.success("Toegang toegestaan, klik hieronder om de Game Library te openen.")
            st.link_button("Open Game Library", sheet_link_data)
        else:
            st.error("Verkeerd wachtwoord")
