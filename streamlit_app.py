import streamlit as st

st.title('My first basic project')

st.write('Hello bakhtovar!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
