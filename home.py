import streamlit as st

st.title("Guru's Only")

CORRECT_PASSWORD = st.secrets["guru_password"]

sheet_link_data = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"
sheet_link_edit = "https://docs.google.com/spreadsheets/d/10kSJ04j7sNsXuXEinq5sVI_ToM13g8RroU0lSbmic0Y/edit?gid=0#gid=0"

# Session state
if "login_clicked" not in st.session_state:
    st.session_state.login_clicked = False


col1, col2 = st.columns(2)

with col1:
    if st.button("Naar Gamelibrary"):
        st.session_state.login_clicked = True

with col2:
    st.markdown(f"""
    <a href="{sheet_link_edit}" target="_blank">
        <button style="padding:10px 20px; font-size:14px;">Spel Opmerking Toevoegen</button>
    </a>
    """, unsafe_allow_html=True)


# Show password after clicking
if st.session_state.login_clicked:
    password = st.text_input("Wachtwoord", type="password")

    if st.button("Login"):
        if password == CORRECT_PASSWORD:
            st.success("Opening Gamelibrary...")

            st.markdown(
                f"""
                <script>
                window.open("{sheet_link_data}", "_blank");
                </script>
                """,
                unsafe_allow_html=True
            )

        else:
            st.error("Verkeerd wachtwoord")
