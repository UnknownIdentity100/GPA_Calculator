import streamlit as st

st.title("Work Hours Calculator")
st.write("Enter the hours you worked for each shift. Add as many shifts as you need.")

num_shifts = st.number_input("How many shifts did you work?", min_value=1, max_value=50, value=5)
hours_list = []

for i in range(int(num_shifts)):
    hours = st.number_input(f"Hours worked for shift {i+1}:", min_value=0.0, value=0.0, step=0.25, key=f"shift_{i}")
    hours_list.append(hours)

if st.button("Calculate Total Hours"):
    total_hours = sum(hours_list)
    st.success(f"Total hours worked: {total_hours}")