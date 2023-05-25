import openai
import streamlit as st

API_KEY = st.secrets["API_KEY"]
openai.api_key = API_KEY


# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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
container = st.container()
container.title("Letter to the Editor")
container.subheader("Use AI to help you write a Letter to the Editor")
container.markdown(
    'Fill in the boxes below, enter the password and press "Ask".')
container.markdown("*Note: Do not add personal information "
                   "like your name, address and email into the form below.*")
st.markdown("***")

topic = st.text_area("What is the issue or subject you want to address "
                     "in your letter to the editor?",
                     help="Describe what the article is about and what "
                          "your own thoughts are on the subject.")
st.markdown("#")
tone = st.text_input("What is the tone of your letter? "
                     "Is it persuasive, informative, argumentative, etc.?",
                     placeholder="Persuasive")
st.markdown("#")
length = st.text_input("How long should the article roughly be?",
                       placeholder="Keep it short. Around 150 words.",
                       help="This is more of a guideline than a hard target. "
                            "The model may over- or undershoot.")
st.markdown("#")
more = st.checkbox("More options")
radio_list = {"My own persona": "Describe yourself in a few short sentences.",
               "A worried parent": "I'm a parent and I'm worried about the future for my kids.",
               "A former Liberal voter": "I'm a long time Liberal Party voter, but I've had enough.",
               "Not a greenie but..": "I wouldn't consider myself a greenie but they seem to be making a lot of sense in this area."}
if more:
    st.write("Give your letter some character by creating a persona.")
    radio = st.radio("Select an option", radio_list.keys())
    print(radio)
    if radio == list(radio_list.keys())[0]:
        personal_experience = st.text_area(
            "Describe yourself in a few short sentences.")
    else:
        personal_experience = st.text_area("You can edit this to suit.", value=radio_list[radio])
        # st.write(radio_list[radio])

st.markdown("***")
password = st.text_input("Password: ", type="password")
st.markdown("#")

ask_button = st.button("Ask")
st.markdown("***")

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
                     f"""Try and make the style of writing based around this persona: {personal_experience}"""

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
