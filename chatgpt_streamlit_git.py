import os
import openai
import streamlit as st


API_KEY = st.secrets["API_KEY"]
openai.api_key = API_KEY


def chat_practice(question):
    if question == "exit":
        return "exit"
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return completion


st.title("Chatbot Practice")
st.write("Please try and answer as many of the questions as possible.")
st.write("Note: Do not add personal information "
         "like your name, address, email, and phone number into the form.")

article_title = st.text_input("What is the article title?")
article_author = st.text_input("Who is the author?")
pub_date = st.text_input("What date was the article published on?")
support = st.text_input("Do you support the views in the article?")
topic = st.text_area("What is the issue or subject you want to address "
                     "in your letter to the editor?")
tone = st.text_input("What is the tone of your letter? "
                     "Is it persuasive, informative, argumentative, etc.?",
                     placeholder="Persuasive")
length = st.text_input("How long should the article be? 300 words?",
                       placeholder="300")
personal_experience = st.text_area("Do you have any personal experience"
                                   " related to the topic?")
evidence = st.text_area("Do you have any evidence or statistics to support"
                        " your argument?")
call_to_action = st.text_area("What action do you want the readers or the "
                              "publication to take after reading your letter?")
ask_button = st.button("Ask")

if not length:
    length = "300"
if not tone:
    tone = "persuasive"

query_combined = f"""
Please write a letter to the editor that includes the following items:
The topic: {topic}
Do I support the article: {support}
The response is to this article: 
    Title: {article_title} 
    Author: {article_author}
    Date of publication: {pub_date}
The tone of my response: {tone}
My preferred article length: {length}
Evidence I'm providing: {evidence}
The call to action I'd like to appear: {call_to_action}
"""
if ask_button:
    # response = chat_practice(query)
    response = chat_practice(str(query_combined))
    st.write(response["choices"][0]["message"]["content"])
    st.write(response["usage"]["total_tokens"])
