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


# Set up the page
st.title("Letter to the Editor")
st.subheader("Use ChatGPT to help you write a Letter to the Editor")
st.write('Fill in the boxes below, enter the password and press "Ask".')
st.write("Note: Do not add personal information "
         "like your name, address and email into the form below.")

topic = st.text_area("What is the issue or subject you want to address "
                     "in your letter to the editor?",
                     help="Describe what the article is about and what "
                          "your own thoughts are on the subject.")
tone = st.text_input("What is the tone of your letter? "
                     "Is it persuasive, informative, argumentative, etc.?",
                     placeholder="Persuasive")
length = st.text_input("How long should the article roughly be?",
                       placeholder="Keep it short. Around 150 words.",
                       help="This is more of a guideline than a hard target. "
                            "The model may over- or undershoot.")
password = st.text_input("Password: ", type="password")
more = st.checkbox("More options")
if more:
    personal_experience = st.text_area("Do you have any personal experience"
                                       " related to the topic?")
    evidence = st.text_area("Do you have any evidence or statistics to support"
                            " your argument?",
                            help="You could paste some relevant facts and other information.")
    call_to_action = st.text_area("What action do you want the readers or the "
                                  "publication to take after reading your letter?")
ask_button = st.button("Ask")

if not length:
    length = "150"
if not tone:
    tone = "persuasive"

# Create the query that will be sent to ChatGPT
query_combined = f"""
Please help me write a letter to the editor about: {topic}.
The tone of my response should be: {tone}.
My preferred article length is: {length}.
"""

if more:
    query_combined = query_combined + \
                     f"""This is my personal experience: {personal_experience}
Evidence that could be used: {evidence}
The call to action I'd like to appear: {call_to_action}"""

# When button pressed:
if ask_button:
    # Only run the query if the password is correct
    if password == st.secrets["PASSWORD"]:
        # Show a message to show that the request is being made.
        with st.spinner(text="Please wait..."):
            # Perform a moderation check.
            moderation_response = openai.Moderation.create(
                input=query_combined
            )
        output = moderation_response['results'][0]['flagged']
        # If moderation ok (False). Then put the request through.
        if output is False:
            # Let the user know there is something happening with a spinner.
            with st.spinner(text="Please wait..."):
                response = send_chat_request(str(query_combined))
            st.write(response["choices"][0]["message"]["content"])
            # How many tokens were used:
            # st.write(response["usage"]["total_tokens"])
        else:
            st.info("Your request has been flagged as against usage policies. "
                    "Please revise your answers and try again.")
    else:
        st.info("Please enter the required password.")
