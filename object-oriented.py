# Raw Class
class Person:
    def __init__(self, name: str, yob: int, sex: str) -> None:
        self.name = name
        self.__year_of_birth = yob
        self.sex = sex

    def getsummary(self):
        return f"Name: {self.name}      Birth: {self.__year_of_birth}     Sex: {self.sex}"

    def setname(self, new_name: str):
        self.name = new_name

    def getname(self):
        return self.name

    def getyearofbirth(self):
        return self.__year_of_birth


# Student is a Person (Inherit Class in another Class)
class Student(Person):
    def __init__(self, name: str, yob: int, sex: str, emailid: str, studentid: int) -> None:
        super().__init__(name, yob, sex)
        self.email_id = emailid
        self.student_id = studentid

    def getsummary(self):
        return f"Name: {self.name}      Birth: {self.getyearofbirth()}     Sex: {self.sex}     Email ID: {self.email_id}     Student ID: {self.student_id}"


# Use Class
student = Student("Rakib", 2000, "Male", "rakib4kbd@gmail.com", 325723484)
print(student.getsummary())
print(student.getname())

# Set Name (Method of Inherited Class Person)
student.setname(10)
print(student.getname())


# List using Class
person_list = [
    Person("Rio", 1995, "Male"),
    Student("Rakib", 2000, "Male", "rakib4kbd@gmail.com", 34623416234)
]

# Read from List using Method
for user in person_list:
    print(user.getsummary())
