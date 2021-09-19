import streamlit as st
import numpy as np 
import pandas as pd

st.title("Fill student's Info")
Form = st.form("Student's info")
left_column, right_column = Form.columns(2)
name = left_column.text_input("Student's name:")
Id = right_column.text_input("Student's id:")
gender = left_column.radio("Gender:", ('Male', 'Female'))
className = right_column.radio("Class:", ('A', 'B', 'C'))

Form.markdown("Student's marks: ")
first, second, third = Form.columns(3)
Myn = first.number_input("Myanmar:", min_value=0, max_value=100, step=1)
Eng = second.number_input("English:", min_value=0, max_value=100, step=1)
Maths = third.number_input("Maths:", min_value=0, max_value=100, step=1)
Phys = first.number_input("Physics:", min_value=0, max_value=100, step=1)
Chem = second.number_input("Chemistry:", min_value=0, max_value=100, step=1)
Bio = third.number_input("Biology:", min_value=0, max_value=100, step=1)

accept = Form.form_submit_button("Submit")
if (accept):
    if (name and Id != ""):
        Form.success("Accepted")
        st.write(f"{name}'s exam result: ")
        data = pd.DataFrame({
            'Subjects': ['Myanmar', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology'],
            'Marks': [Myn, Eng, Maths, Phys, Chem, Bio],
        }).set_index('Subjects')

        st.write(data)
        st.bar_chart(data)
    else:
        Form.error("Please fill the info!")
page = st.sidebar.radio("", ("Home", "Students' info", "About", "Contact"), index=1)