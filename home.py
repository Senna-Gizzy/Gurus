import streamlit as st
# ______________________________________________________________________________
# Page Style

# darkbrown: #654f41
# lightbrown: #c29e8e
# blueisch: #649999


st.markdown("""
<style>
/* Background color */
.stApp {
    background-color: #649999;
}

/* Title styling */
h1 {
    text-align: center;
    color: white !important;
    font-weight: 700;
    font-size: 40px;
    margin-bottom: 20px;
}

/* Buttons */
.stButton > button {
    background-color: #c29e8e;
    color: white;
    border-radius: 12px;
    height: 48px;
    width: 100%;
    border: none;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #654f41;
    transform: translateY(-2px);
}

/* Link buttons */
.stLinkButton a {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
    background-color: #c29e8e !important;
    color: white !important;
    border-radius: 12px;
    padding: 14px 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Link button hover */
.stLinkButton a:hover {
    background-color: #654f41 !important;
    transform: translateY(-2px);
}

/* Login card container */
.login-card {
    background-color: rgba(20,20,30,0.85);
    padding: 25px;
    border-radius: 20px;
    max-width: 400px;
    margin: auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    text-align: center;
}

/* Password field styling */
div[data-testid="stTextInput"] input {
    color: black !important;  /* typed text black */
    background-color: rgba(255,255,255,0.1) !important;
    border-radius: 8px;
    border: 1px solid #ccc;
}
div[data-testid="stTextInput"] label {
    color: white !important;  /* label white */
    font-weight: 600;
}

/* Target all alert boxes */
div[role="alert"] {
    border-radius: 8px !important;
    padding: 12px !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
    color: #fff !important;
}

/* Success alert with green background */
div[role="alert"][aria-label="success"] {
    background-color: #8fc28e !important;
}

/* Error alert with red background */
div[role="alert"][aria-label="error"] {
    background-color: #d66d6d !important;
}

/* Center images inside container */
.stContainer {
    display: flex;
    justify-content: center;
    align-items: center;
}

[data-testid="stImage"] {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

# _________________________________________________________________________________________________________
# Header and Main Content Centering

left, center, right = st.columns([1, 2, 1])

with center:
    st.image("https://www.spellenhuis.nl/media/8a/65/ae/1634638327/spellenhuislogo.png", use_column_width=True)
 
    
    st.write("")  # add some vertical space
    st.write("")
    st.title("Agga Guru's")

    # Buttons
    CORRECT_PASSWORD = st.secrets["guru_password"]
    sheet_link_data = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"
    sheet_link_edit = "https://docs.google.com/spreadsheets/d/10kSJ04j7sNsXuXEinq5sVI_ToM13g8RroU0lSbmic0Y/edit?gid=0#gid=0"

    if "login_clicked" not in st.session_state:
        st.session_state.login_clicked = False

    st.write("") 

    # Spel Opmerking Button
    st.link_button("Spel Opmerking Toevoegen", sheet_link_edit, use_container_width=True)

    # Game Library Button
    if st.button("Naar Game Library", use_container_width=True):
        st.session_state.login_clicked = True

    st.write("")  

    # Password input
    if st.session_state.login_clicked:
        password = st.text_input("Wachtwoord", type="password")

        if st.button("Login"):
            if password == CORRECT_PASSWORD:
                st.success("Toegang toegestaan, klik hieronder om de Game Library te openen.")
                st.link_button("Open Game Library", sheet_link_data, use_container_width=True)
            else:
                st.error("Verkeerd wachtwoord")
