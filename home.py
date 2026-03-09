import streamlit as st
import pandas as pd

st.title("Guru's Only")

CORRECT_PASSWORD = st.secrets["guru_password"]


password = st.text_input("Wachtwoord", type="password")
if st.button("Login"):
    if password == CORRECT_PASSWORD:
        st.session_state.authenticated = True
        sheet_link_data = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"
        sheet_link_edit = "https://docs.google.com/spreadsheets/d/10kSJ04j7sNsXuXEinq5sVI_ToM13g8RroU0lSbmic0Y/edit?gid=0#gid=0"
        st.markdown(f"""
        <a href="{sheet_link_data}" target="_blank">
            <button style="padding:10px 20px; font-size:14px;">Naar Gamelibrary</button>
        </a>
        """, unsafe_allow_html=True)

        <a href="{sheet_link_data}" target="_blank">
            <button style="padding:10px 20px; font-size:14px;">Spelopmerking Toevoegen</button>
        </a>
        """, unsafe_allow_html=True)

        st.divider()
    else:
        st.error("Verkeerd wachtwoord")

# Stop at the end to prevent the app from executing further
st.stop()
