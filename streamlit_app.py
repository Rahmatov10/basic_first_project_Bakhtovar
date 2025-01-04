import streamlit as st
import pandas as pd
st.title('My first basic project')

st.write('Hello bakhtovar!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
with st.expander("Data"):
  st.write("X")
