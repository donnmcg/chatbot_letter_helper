import openai
import streamlit as st

API_KEY = st.secrets["API_KEY"]
openai.api_key = API_KEY


def send_chat_request(question):
    """
    :param question: should be a str in the form of a question.
    :return: a str response from ChatGPT.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return completion


def moderation_check(question):
    moderation_response = openai.Moderation.create(
        input=question
    )
    output = moderation_response['results'][0]['flagged']
    return output


if __name__ == "__main__":
    pass
