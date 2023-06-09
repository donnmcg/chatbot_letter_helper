import streamlit as st

# Set up the webpage
st.title("How to use this site")
st.markdown("***")

st.markdown("## Getting Started")
st.markdown("It is super easy to get started. Check out the video below to "
            "help you get creating letters to the editor. \n\n(5 minutes)")
video_file = open('files/getting_started_230609_2.webm', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.markdown("***")
st.markdown("## Adding a Persona")
st.markdown("You can give your letter some personality by using a persona. "
            "The model will attempt to write the letter using the "
            "personality/perspective of the suggested persona. To do this:")
st.markdown("1. Fill in the first three boxes on the Home page as usual.")
st.image("files/first_three_boxes_border.png")
st.markdown("2. Select the 'More options' check box.")
st.image("files/more_options_check_box_border.png")
st.markdown("3. Create your own pesona or select one of the other options. "
            "You can edit an option to suit.")
st.image("files/a_worried_parent_selected_border.png")
st.markdown("4. Press 'Ask. The letter should include your persona like the "
            "one below.")
st.image("files/output_example_parent_highlight_border.png")
st.markdown("***")
st.markdown("## Using Other Models/Chatbots")
st.markdown("If you want to try out a different chatbot or AI model you can "
            "use the 'Show Query' check box. Simply fill in the form as "
            "usual, select the 'Show Query' check box and press 'Ask'. You "
            "get a printout of the query that is sent to "
            "Openai to create your letter (as well as the corresponding "
            "response). You can copy and paste this into other chatbot "
            "models like Bing chat, Google Bard, etc.\n\n "
            "You don't need a password to see the query.")
st.markdown("***")
st.markdown("## No Password")
st.markdown("If you don't have a password then reach out to us. Otherwise, "
            "check out the 'Using Other Models' tip to see how you can use "
            "the request created by this page in other chatbots like Bing "
            "chat and Google Bard. You don't need a password to create a "
            "request that you can use in other applications.")
st.markdown("***")