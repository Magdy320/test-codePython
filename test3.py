employee = [
    {"name": "Ahmed", "salary": 5000, "active": True},
    {"name": "Sara", "salary": 6000, "active": False},
    {"name": "Omar", "salary": 4500, "active": True}
]

def calc_active_salaries(employee_list):
    total = 0 
    for employee in employee_list:
        if employee["active"]:
            total += employee["salary"]
    return total

res = calc_active_salaries(employee)
print("total active salaries: ", res)

print(f"\n")

students = [
    {"name": "Youssef", "birth_date": "2004-05-12", "city": "Cairo", "gpa": 3.8},
    {"name": "Mariam", "birth_date": "2005-09-20", "city": "Alexandria", "gpa": 3.2},
    {"name": "Karim", "birth_date": "2004-11-03", "city": "Giza", "gpa": 3.6}
]

def get_honor_students(student_records):
    honor_students = []
    for student in student_records:
        if student["gpa"] >= 3.5:
            honor_students.append(student["name"])
    return honor_students

result = get_honor_students(students)
print("Honor students:", result)