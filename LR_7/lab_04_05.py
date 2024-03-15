class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def display(self):
        print(f"Name: {self.firstname} {self.lastname}, Age: {self.age}")

class Student(Person):
    def __init__(self, firstname, lastname, age, studentID, recordBook):
        super().__init__(firstname, lastname, age)
        self.studentID = studentID  
        self.recordBook = recordBook
        
    def display(self):
        super().display()
        print(f"Student ID: {self.studentID}, Record Book: {self.recordBook}")

class Professor(Person):
    def __init__(self, firstname, lastname, age, professorID, degree):
        super().__init__(firstname, lastname, age)
        self.professorID = professorID
        self.degree = degree
        
    def display(self):
        super().display()
        print(f"Professor ID: {self.professorID}, Degree: {self.degree}")

student1 = Student("Ivan", "Ivanov", 20, "S1001", [5, 4, 4, 3])
student2 = Student("Petr", "Petrov", 22, "S1002", [5, 3, 3, 2])
student3 = Student("Sidor", "Sidorov", 19, "S1003", [5, 5, 4, 5])

student1.display()
print("--------------------")
student2.display()
print("--------------------")
student3.display()
print("--------------------")

professor1 = Professor("Anna", "Ivanova", 45, "P1001", "Ph.D. in Computer Science")
professor2 = Professor("Boris", "Petrov", 50, "P1002", "Ph.D. in Mathematics")
professor3 = Professor("Olga", "Sidorova", 35, "P1003", "Ph.D. in Physics")

professor1.display()
print("--------------------")
professor2.display()
print("--------------------")
professor3.display()
print("--------------------")