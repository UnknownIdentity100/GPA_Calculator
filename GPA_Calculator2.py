import streamlit as st

st.title("Weighted GPA Calculator")

st.write("Enter your courses below. You can adjust the number of courses as needed.")

course_types = {
    "On Level": 5.0,
    "Honors": 5.5,
    "GT": 5.5,
    "AP": 6.0,
    "DC": 6.0
}

num_courses = st.number_input("How many courses?", min_value=1, max_value=75, value=7)
courses = []

for i in range(num_courses):
    st.subheader(f"Course {i+1}")
    grade = st.number_input(f"Grade (0-100)", min_value=0.0, max_value=100.0, value=100.0, key=f"grade_{i}")
    credits = st.number_input(f"Credits", min_value=0.5, max_value=10.0, value=1.0, key=f"credits_{i}")
    course_type = st.selectbox(f"Course Type", options=list(course_types.keys()), key=f"type_{i}")
    courses.append((grade, credits, course_type))

def grade_to_gpa(grade, course_type):
    max_gpa = course_types.get(course_type, 5.0)
    return (grade / 100) * max_gpa

def calculate_weighted_gpa(courses):
    total_weighted_gpa = 0
    total_credits = 0
    for grade, credits, course_type in courses:
        gpa = grade_to_gpa(grade, course_type)
        total_weighted_gpa += gpa * credits
        total_credits += credits
    if total_credits == 0:
        return 0
    return total_weighted_gpa / total_credits

if st.button("Calculate Weighted GPA"):
    weighted_gpa = calculate_weighted_gpa(courses)
    st.success(f"Your weighted GPA is: {weighted_gpa:.2f}")
