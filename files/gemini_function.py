import google.generativeai as genai
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)


def send_gemini_query(query_text):
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(query_text)

    return response


if __name__ == "__main__":
    query = "Tell me a joke."
    print(send_gemini_query(query).text)
