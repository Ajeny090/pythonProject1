class Students:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def description(self):
         print(f"* The student's name is {self.name}.")
         print(f"* The student's age is {self.age}.")
         print(f"* The course is {self.course}.")

s1 = Students("Brian", 30, "Computer science")
s2 = Students("James",34,"Management")
s1.description()
print("***********")
s2.description()