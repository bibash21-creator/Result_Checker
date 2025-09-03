

import streamlit as st

import pandas as pd






df = pd.read_csv("result.csv")




         
# Clean data

# Roll Number
roll = pd.to_numeric(df["Roll_Num"], errors="coerce")


# Code
code = df["BIT_Code"].astype(str).str.strip()

# Campus
campus = df["Campus"].astype(str).str.strip()



# Streamlit Ui
st.title("BIT Result Checker")
st.set_page_config(
    page_title="BIT Checker",   # This sets the browser tab title
    page_icon="🎓",             # Optional: favicon for your page
    layout="centered"           # Optional: page layout
)

# Override browser tab title using HTML
st.markdown(
    """
    <script>
    document.title = "BIT Checker";
    </script>
    """,
    unsafe_allow_html=True
)


# enter your  roll number
st.write("Hey Guys! Please enter your Roll Number or BIT Code to check your result:")

st.write("If you are giving back exam, enter your   BIT Code brothers neither just roll number will work")


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
           
    


