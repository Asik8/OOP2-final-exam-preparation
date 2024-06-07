class Student:
    def __init__(self, name, roll_number, marks1, marks2):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Marks1: {self.marks1}, Marks2: {self.marks2}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept(self, name, roll_number, marks1, marks2):
        student = Student(name, roll_number, marks1, marks2)
        self.students.append(student)

    def display(self):
        for student in self.students:
            print(student)

    def search(self, roll_number):
        try:
            found = False
            for student in self.students:
                if student.roll_number == roll_number:
                    print(student)
                    found = True
                    break
            if not found:
                raise ValueError("Student not found.")
        except ValueError as e:
            print(e)
