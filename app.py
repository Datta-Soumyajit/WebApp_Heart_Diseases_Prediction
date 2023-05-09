import streamlit as st
import prediction_page as pp
import explore_page as ep
page = st.sidebar.radio("Pages", options =["Predict", "Explore"])

if page == "Predict":
    pp.show_predict_page()
else:
    ep.show_explore_page()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)