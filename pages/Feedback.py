import streamlit as st
from send_email import send_email

st.header("Feedback")
st.text("Please use the below form for any feedback.")
st.text("Help us make this site better and easier to use.")

# Create a form for the web user to contact us on
with st.form(key="email_forms"):
    # Place to enter an email
    user_email = st.text_input("Enter your email address")
    # allows multiline text input for an email-like message
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Letter to the Editor Feedback {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")  # submit form button
    if button:
        send_email(message)
        st.info("Your message was sent successfully!")