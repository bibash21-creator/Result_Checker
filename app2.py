import streamlit as st
import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

# Clean data
df["Campus"] = df["Campus"].astype(str).str.strip()
df["BIT_Code"] = df["BIT_Code"].astype(str).str.strip()

# Roll_Num as numeric, coerce errors (empty cells become NaN)
df["Roll_Num"] = pd.to_numeric(df["Roll_Num"], errors="coerce")

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="Student Result Checker", page_icon="🎓")
st.title("🎓 Student Result Checker")

st.write("Enter your **Roll Number** or **BIT Code** to check your result:")

# User input
user_roll = st.text_input("Roll Number")
user_bit = st.text_input("BIT Code")

# Button to check
if st.button("Check Result"):
    found = False
    
    # Check Roll Number
    if user_roll:
        try:
            user_roll_num = int(user_roll)
            student = df[df["Roll_Num"] == user_roll_num]
            if not student.empty:
                st.success("🎉 Student found!")
                st.write(f"**Campus:** {student['Campus'].values[0]}")
                st.write(f"**BIT Code:** {student['BIT_Code'].values[0]}")
                found = True
            else:
                st.error("❌ Roll Number not found.")
        except ValueError:
            st.error("❌ Roll Number must be numeric.")
    
    # Check BIT Code
    if user_bit:
        user_bit_code = user_bit.strip()
        student = df[df["BIT_Code"] == user_bit_code]
        if not student.empty:
            st.success("🎉 Student found!")
            st.write(f"**Campus:** {student['Campus'].values[0]}")
            st.write(f"**Roll Number:** {student['Roll_Num'].values[0]}")
            found = True
        else:
            if not user_roll:
                st.error("❌ BIT Code not found.")
    
    # If nothing found
    if not found:
        st.warning("Student not found. Please check your input.")
