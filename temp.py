import streamlit as st, time, random 
# import pandas as pd, numpy as np
# import pandasai as pai


# Generate greeting for the user
def greeting_generator():
    salutes = [
        "Hello! How can I help you today?",
        "Hi! Hope you are having a great day!",
        "Hey! What's up?",
        "Any questions? Ask away!",
        "Remember to breathe and drink your water"
    ]
    greeting = random.choice(salutes)
    
    for word in greeting.split():
        yield word + " "
        time.sleep(0.2)

st.set_page_config(layout="wide",
                   page_title="PR Stress Reliever",
                   page_icon=":purple_heart:",
                   menu_items={"Get help":"mailto:dcedres@cccupr.org",
                               "Report a Bug":"mailto:dcedres@cccupr.org",
                               "About":"AI App for Stress Relief before initial consultation with health care provider"})

st.subheader("Testing the App through the web browser")
# print("Testing the App through the terminal")
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

# Accept user input
if prompt := st.chat_input("Hello!"):
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(greeting_generator())
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




# Removes "Made with Streamlit"
hide_style = """<style>
                 footer {visibility: hidden;}
             </style>"""
# Allows HTML markdown code
st.markdown(hide_style, unsafe_allow_html=True)
