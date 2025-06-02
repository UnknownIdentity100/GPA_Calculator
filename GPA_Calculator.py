Overall = (100, 100, 98, 96, 97, 94, 97)
Overall[0]
# Example: (grade, credits, course_type)
courses = [
    (100, 1, "on level"),
    (94, 1, "honors"),
    (99, 1, "honors"),
    (98, 1, "on level"),
    (95, 1, "honors"),
    (96, 1, "ap"),
    (99, 1, "GT")
]

def grade_to_gpa(grade, course_type):
    # Define max GPA for each course type
    scale = {"on level": 5.0, "honors" or "GT": 5.5, "ap" or "dc": 6.0}
    max_gpa = scale.get(course_type, 5.0)
    # Convert grade (0-100) to GPA on the appropriate scale
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

weighted_gpa = calculate_weighted_gpa(courses)
print(f"Your weighted GPA is: {weighted_gpa:.2f}")