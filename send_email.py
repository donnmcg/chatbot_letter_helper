import smtplib, ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"  # specifically for a gmail account.
    port = 465  # standard port
    username = st.secrets["EMAIL"]
    password = st.secrets["EMAIL_PASSWORD"]
    receiver = st.secrets["EMAIL"]
    # variable holds context for sending emails securely.
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
