class Student:
    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_number)
        print("Age:",self.age)

student = Student()
student.name = "Hassan"
student.roll_number = 23
student.age = 19
student.display()
