import pandas as pd, pandasai as pai, streamlit as st, numpy as np

st.set_page_config(layout="wide",
                   page_title="PR Stress Reliever",
                   page_icon=":purple_heart:",
                   menu_items={"Get help":"mailto:dcedres@cccupr.org",
                               "Report a Bug":"mailto:dcedres@cccupr.org",
                               "About":"AI App for Stress Relief before initial consultation with health care provider"})

print("Testing the App through the terminal")
st.subtitle("Testing the App through the web browser")
# st.write("Testing the App through the web browser")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun:
#   1. Use a list to store the messages
#   2. Append to it every the user or bot sends a message. 
#   3. Each entry in the list will be a dictionary with keys: 
#      - role: author of the message
#      - content: the message content
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# Removes "Made with Streamlit"
hide_style = """<style>
                 footer {visibility: hidden;}
             </style>"""
# Allows HTML markdown code
st.markdown(hide_style, unsafe_allow_html=True)
