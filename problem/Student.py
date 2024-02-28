class Student:
    def __init__(self, studentId, firstName, lastName, gradeLevel):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel
    
    def getStudentInfo(self):
        return self.studentId + ': ' + self.firstName + ' ' + self.lastName + '(' + str(self.gradeLevel) + 'gr)'
    


student1 = Student("AC-343424", "James", "Smith", 6)

print(student1.getStudentInfo())  # AC-343424: James Smith(6)

student2 = Student("AC-343428", "Maria", "Garcia", 5)

print(student2.getStudentInfo())  # AC-343428: Maria Garcia(5)

student3 = Student("AC-343434", "Robert", "Johnson", 3)

print(student3.getStudentInfo())  # AC-343434: Robert Johnson(3)

