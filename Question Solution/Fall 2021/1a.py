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

    # def accept(self, name, roll_number, marks1, marks2):
    #     student = Student(name, roll_number, marks1, marks2)
    #     self.students.append(name)
    
    def accept(self, name):
        # student = Student(name, roll_number, marks1, marks2)
        self.students.append(name)

    def display(self):
        for student in self.students:
            print(student)

    def search(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                return
        print("Student not found.")

# Create an instance of StudentManagementSystem
sms = StudentManagementSystem()

# Accepting details of students
sms.accept(Student("John Doe", 2, 85, 90))
# sms.accept("Jane Smith", 2, 78, 88)
# sms.accept("Alice Brown", 3, 92, 95)

# Displaying all students
print("All students:")
sms.display()

# Searching for a student by roll number
print("\nSearch for student with roll number 2:")
sms.search(2)
