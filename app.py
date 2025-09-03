

import streamlit as st

import pandas as pd




# user_symbol = st.number_input("Enter your Symbol Number", placeholder="Check your result using symbol number")

# user_code = st.text_input("Enter your BIT code", placeholder="Plz Enter the Details")

df = pd.read_csv("result.csv")



# # Logical
# if  user_symbol:
#    result = df[df["Roll_Num"] == user_symbol]
#    if not result.empty:
#         st.success(f"You are passed lad!")
#         st.balloons
#    else:
#         st.error(f"Better luck next time brother")



# if user_code:
#     result_code = df[df["BIT_Code"] == str(user_code)]
#     if not result_code.empty:
#           st.success(f"You are passed lad!")
#           st.balloons
#     else:
#         st.error(f"Better luck next time brother")
         
# Clean data

# Roll Number
roll = pd.to_numeric(df["Roll_Num"], errors="coerce")


# Code
code = df["BIT_Code"].astype(str).str.strip()

# Campus
campus = df["Campus"].astype(str).str.strip()



# Streamlit Ui
st.title("Result Checker Appplication")



# enter your  roll number
st.write("Hey Guys! Please enter your Roll Number or BIT Code to check your reuslt:")


# User Input

user_roll = st.text_input("Enter your  roll number")

user_bit = st.text_input("Enter your BIT Code")


# Button to check
if st.button("Check Resut"):
    found = False


    # Check Roll number
    if user_roll:
        try:
          user_roll_num = int(user_roll)
          student = df[roll==user_roll_num]

          if not student.empty:
             st.success("Your are found!")
             st.write(f"Campus: {student['Campus'].values[0]}")
             st.write(f"BIT Code: {student['BIT_Code'].values[0]}")
             st.balloons()
             st.success("Congratulations! You have passed brother")

             found = True

        except ValueError:
           st.error("Roll nummber must be numeric.")
        
       
     # Check BIT Code
    if user_bit:
       user_bit_code = user_bit.strip()
       student = df[df["BIT_Code"] == user_bit]

       if not student.empty:
          st.success("Student Found")
          st.write(f"Campus: {student['Campus'].values[0]}")
          st.write(f"Roll Number: {student['Roll_Num'].values[0]}")

          st.balloons()
          st.success("Congratulations! You have passed brother")
          found = True

       else:
          st.write("BIT Code not Found.")


     # Nothing found
    if not  found:
       st.warning("Student not found. Please check  your input.")
           
    


