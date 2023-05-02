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


st.title("Letter to the Editor")
st.write("It isn't necessary to answer every question. "
         "But you'll need to provide information on the issue or subject.")
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
length = st.text_input("How long should the article be?",
                       placeholder="150 words")
personal_experience = st.text_area("Do you have any personal experience"
                                   " related to the topic?")
evidence = st.text_area("Do you have any evidence or statistics to support"
                        " your argument?")
call_to_action = st.text_area("What action do you want the readers or the "
                              "publication to take after reading your letter?")
password = st.text_input("Password: ", type="password")
ask_button = st.button("Ask")

if not length:
    length = "150"
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
The tone of my response should be: {tone}
Try to keep it short. My preferred article length in words is: {length}
Evidence that could be used: {evidence}
The call to action I'd like to appear: {call_to_action}
"""
# When button pressed:
if ask_button:
    # Only run the query if the password is correct
    if password == st.secrets["PASSWORD"]:
        moderation_response = openai.Moderation.create(
            input=query_combined
        )
        output = moderation_response['results'][0]['flagged']
        if output is False:
            response = chat_practice(str(query_combined))
            st.write(response["choices"][0]["message"]["content"])
            st.write(response["usage"]["total_tokens"])
        else:
            st.info("Your request has been flagged as against usage policies. "
                    "Please revise your answers and try again.")
    else:
        st.info("Please enter the required password.")
