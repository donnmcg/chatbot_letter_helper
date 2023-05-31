import streamlit as st

# Set up the webpage
st.title("How to use this site")
st.markdown("***")

st.markdown("## Check out this video for a quick run-through.")
video_file = open('files/streamlit-Home-2023-05-31-11-05-91.webm', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)