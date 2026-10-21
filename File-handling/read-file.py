with open("students.txt", "w") as f:
    f.write("Name: Hassan\nCourse: BSc IT\n")

with open("students.txt", "r") as f:
    data = f.read()
    print(data)
