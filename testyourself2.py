grades = [40, 75, 88, 32, 60, 49, 91]
count = 0

for grade in grades:
    if grade >= 50:
        count += 1

print("Passed students: " , count)