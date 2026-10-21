class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("E001", "Hassan", 25000)
employee2 = Employee("E002", "Mansiya", 30000)
employee1.display()
employee2.display()
