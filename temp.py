import pandas as pd, pandasai as pai, streamlit as st, numpy as np

st.set_page_config(layout="wide",
                   page_title="PR Kidney Disease-SDOH",
                   page_icon=":test_tube:",
                   menu_items={"Get help":"mailto:dylan.cedres@upr.edu",
                               "Report a Bug":"mailto:dylan.cedres@upr.edu",
                               "About":"Dashboard with Kidney Disease Lab Data and Social Determinants of Health Indices"})

print("Testing the App through the terminal")
st.write("Testing the App through the web browser")


# Removes "Made with Streamlit"
hide_style = """<style>
                 footer {visibility: hidden;}
             </style>"""

st.markdown(hide_style, unsafe_allow_html=True)
