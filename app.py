import streamlit as st

import pandas as pd



# Streamlit Ui
st.title("Result Checker Appplication")

user_symbol = st.number_input("Enter your Symbol Number", placeholder="Check your result using symbol number")

df = pd.read_csv("result.csv")



# Function
if  user_symbol:
   result = df[df["Roll_Num"] == user_symbol]
   if not result.empty:
        st.success(f"You are passed lad!")
   else:
        st.error(f"Better luck next time brother")

