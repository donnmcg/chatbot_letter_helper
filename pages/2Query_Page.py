import openai
import streamlit as st
from files.gpt_function import send_chat_request, moderation_check
from files.gemini_function import send_gemini_query


# Set up the page
st.title("General Query for ChatGPT")
st.subheader("Do you need help with phrasing or something else?")
st.write('Fill in the box below, enter the password and press "Ask".')
st.write("Note: Do not add personal information "
         "like your name, address or email into the form below.")

topic = st.text_area("Type a query",
                     help="Ask Google Gemini anything.")

password = st.text_input("Password: ", type="password")
ask_button = st.button("Ask")

# Create the query that will be sent to ChatGPT
query_combined = topic

# When button pressed:
if ask_button:
    print(query_combined)
    # Only run the query if the password is correct
    if password == st.secrets["PASSWORD"]:
        # # Show a message to show that the request is being made.
        # with st.spinner(text="Please wait..."):
        #     # Perform a moderation check.
        #     output = moderation_check(query_combined)
        # # If moderation ok (False). Then put the request through.
        # if output is False:
        #     # Let the user know there is something happening with a spinner.
        #     with st.spinner(text="Please wait..."):
        #         response = send_chat_request(str(query_combined))
        #     st.write(response["choices"][0]["message"]["content"])
        #     # How many tokens were used:
        #     # st.write(response["usage"]["total_tokens"])
        # else:
        #     st.info("Your request has been flagged as against usage policies. "
        #             "Please revise your answers and try again.")

        # Google Gemini
        # Let the user know there is something happening with a spinner.
        with st.spinner(text="Please wait..."):
            # Send query to gemini
            response = send_gemini_query(str(query_combined))
            # Write the response from Gemini
        st.write(response.text)
    else:
        st.info("Please enter the required password.")
