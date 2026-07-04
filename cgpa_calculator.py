# ===============================================
# COS202 PERSONAL POCKET CGPA CALCULATOR (PPC)
# Developed in Python
# ===============================================

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_grade_point(grade):
    grade = grade.upper()

    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        return -1


print("=" * 60)
print("        PERSONAL POCKET CGPA CALCULATOR")
print("=" * 60)

student_name = input("Enter Student Name: ")
matric_no = input("Enter Matric Number: ")

while True:
    try:
        number_of_courses = int(input("Enter Number of Courses: "))
        if number_of_courses > 0:
            break
        else:
            print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid input!")

total_units = 0
total_grade_points = 0

results = []

for i in range(number_of_courses):
    print(f"\nCourse {i + 1}")

    course_code = input("Course Code: ")

    while True:
        try:
            unit = int(input("Course Unit: "))
            if unit > 0:
                break
            else:
                print("Course unit must be greater than zero.")
        except ValueError:
            print("Invalid input!")

    while True:
        grade = input("Grade (A-F): ").upper()

        grade_point = get_grade_point(grade)

        if grade_point != -1:
            break
        else:
            print("Invalid Grade! Enter A, B, C, D, E or F.")

    quality_point = grade_point * unit

    total_units += unit
    total_grade_points += quality_point

    results.append([
        course_code,
        unit,
        grade,
        grade_point,
        quality_point
    ])

cgpa = total_grade_points / total_units

clear_screen()

print("=" * 75)
print("                PERSONAL POCKET CGPA REPORT")
print("=" * 75)

print(f"Student Name : {student_name}")
print(f"Matric Number: {matric_no}")

print("-" * 75)
print("{:<15}{:<10}{:<10}{:<15}{:<15}".format(
    "Course", "Unit", "Grade", "Grade Point", "Quality Point"))
print("-" * 75)

for item in results:
    print("{:<15}{:<10}{:<10}{:<15}{:<15}".format(
        item[0],
        item[1],
        item[2],
        item[3],
        item[4]
    ))

print("-" * 75)

print(f"Total Units        : {total_units}")
print(f"Total Grade Points : {total_grade_points}")
print(f"CGPA               : {cgpa:.2f}")

print("-" * 75)

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
elif cgpa >= 1.00:
    print("Class of Degree: Pass")
else:
    print("Class of Degree: Fail")

print("=" * 75)
print("Thank you for using the Personal Pocket CGPA Calculator!")