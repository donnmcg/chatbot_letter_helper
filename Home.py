import streamlit as st
from files.gpt_function import send_chat_request, moderation_check
from files.gemini_function import send_gemini_query

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Set up the page
st.title("Letter to the Editor")
st.subheader("Use AI to help you write a Letter to the Editor")
st.markdown(
    'Fill in the boxes below. Enter the password. And press "Ask". Do not '
    'include personal information like your name, address and email.')
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
more = st.checkbox("More options")  # Allow user to add more options.
radio_list = {"My own persona": "Describe yourself in a sentence or more.",
              "A worried parent": "I'm a parent and I'm worried about what "
                                  "the future has in store for my kids.",
              "A former conservative": "I've always held conservative "
                                       "beliefs, but I'm beginning to think "
                                       "that things might be better if I "
                                       "change my views.",
              "Not a greenie but..": "I wouldn't consider myself a 'greenie' "
                                     "by any stretch of the imagination, "
                                     "but I think the people that care about "
                                     "our environment have some good ideas "
                                     "sometimes."}

# If user selects "More", then show other options.
if more:
    st.write("Give your letter some character by creating a persona.")
    radio = st.radio("Select an option", radio_list.keys())
    if radio == list(radio_list.keys())[0]:
        personal_experience = st.text_area(
            "Describe yourself in a few short sentences.")
    else:
        personal_experience = st.text_area("You can edit this to suit.",
                                           value=radio_list[radio])

st.markdown("***")
password = st.text_input("Password: ", type="password")
st.markdown("#")

# Create columns for the Ask button and Show Query checkbox
col1, col2, col3 = st.columns([1, 1, 2], gap="small",)

with col1:
    ask_button = st.button("Ask")
with col2:
    show_query = st.checkbox("Show Query",
                             help="This displays the request sent to the "
                                  "model. It may be useful if you want to "
                                  "use a different model like Bing chat, "
                                  "Google Bard, etc.")

st.markdown("***")  # Add a line to break things up.

# Use the placeholders if user doesn't overwrite them.
if not length:
    length = "Keep it short. Around 150 words."
if not tone:
    tone = "persuasive"

# Create the query that will be sent to ChatGPT
query_combined = f"""
Please help me write a letter to the editor about: {topic}.\n
The tone of my response should be: {tone}.\n
My preferred article length is: {length}.\n
"""

# If the user selected "More", add it to the query
if more:
    query_combined = query_combined + \
                     f"""Try and make the style of writing based around this 
                     persona: {personal_experience} """

# When Ask button pressed:
if ask_button:
    # Print the query if the checkbox is selected:
    if show_query:
        st.markdown("**Your Query:**")
        st.write(query_combined)
        st.markdown("***")  # Add a line to separate stuff.
    # Only run the query if the password is correct
    if password == st.secrets["PASSWORD"]:
        # Using GPT:
        # # Show a message to show that the request is being made.
        # with st.spinner(text="Please wait..."):
        #     # Perform a moderation check.
        #     output = moderation_check(query_combined)
        #
        # # If moderation ok (False). Then put the request through.
        # if output is False:
        #     # Let the user know there is something happening with a spinner.
        #     with st.spinner(text="Please wait..."):
        #         st.markdown("**Model Response:**")
        #         response = send_chat_request(str(query_combined))
        #     st.write(response["choices"][0]["message"]["content"])
        #     # How many tokens were used:
        #     # st.write(response["usage"]["total_tokens"])
        # else:
        #     st.info("Your request has been flagged as against usage policies. "
        #             "Please revise your answers and try again.")

        # Using Gemini:
        # Let the user know there is something happening with a spinner.
        with st.spinner(text="Please wait..."):
            st.markdown("**Model Response:**")
            # Send query to gemini
            response = send_gemini_query(str(query_combined))
        # Write the response from Gemini
        st.write(response.text)
    else:
        st.info("Please enter the required password.")
