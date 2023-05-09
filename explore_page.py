import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('HeartDiseaseTrain-Test.csv')

def interactive_plot(df):
    x_val = st.selectbox("Select X axis", options=df.columns)
    y_val = st.selectbox("Select Y axis", options=df.columns)
    plot = px.scatter(df, x= x_val, y = y_val)
    st.plotly_chart(plot)
    
    
    
    
def show_explore_page():
    st.title("Explore Dataset")

    st.write("""### Scatter Plot""")
    interactive_plot(df)