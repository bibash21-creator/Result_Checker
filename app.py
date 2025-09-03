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
        st.success(f"✅ Symbol No. {user_symbol} found in the Pass list!")
   else:
        st.error(f"❌ Symbol No. {user_symbol} not found in the Pass result list.")

