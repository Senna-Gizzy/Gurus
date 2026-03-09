import streamlit as st

st.title("Guru's Only")

CORRECT_PASSWORD = st.secrets["guru_password"]

sheet_link_data = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"
sheet_link_edit = "https://docs.google.com/spreadsheets/d/10kSJ04j7sNsXuXEinq5sVI_ToM13g8RroU0lSbmic0Y/edit?gid=0#gid=0"

if "login_clicked" not in st.session_state:
    st.session_state.login_clicked = False


col1, col2 = st.columns(2)

with col1:
    if st.button("Naar Game Library"):
        st.session_state.login_clicked = True

with col2:
    st.link_button("Spel Opmerking Toevoegen", sheet_link_edit)


if st.session_state.login_clicked:
    password = st.text_input("Wachtwoord", type="password")

    if st.button("Login"):
        if password == CORRECT_PASSWORD:
            st.success("Toegang toegestaan, klik hieronder om de Game Library te openen.")
            st.link_button("Open Game Library", sheet_link_data)
        else:
            st.error("Verkeerd wachtwoord")
