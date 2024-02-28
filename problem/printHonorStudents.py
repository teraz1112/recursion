class Classroom:
    def __init__(self, students,courseName,teacher):
        self.students = students
        self.courseName = courseName
        self.teacher = teacher
    
    def getClassIdentity(self):
        return self.courseName + " managed by " + self.teacher
    
    def getNumberOfStudents(self):
        return len(self.student)

class Student:
    def __init__(self, studentId, firstName, lastName, gradeLevel):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel
    
    def getStudentInfo(self):
        return self.studentId + ': ' + self.firstName + ' ' + self.lastName + '(' + str(self.gradeLevel) + 'gr)'

def printHonorStudents(school):
    for classroom in school:
        for student in classroom.students:
            if student.gradeLevel >= 10:
                print(student.getStudentInfo()+' from '+classroom.teacher+"'s class")



classroom1 = Classroom([Student("AC-343424", "James", "Smith", 6), Student("AC-343428", "Maria", "Garcia", 5),Student("AC-343434", "Robert", "Johnson", 3),Student("AC-343454","Danny", "Robertson",10)], "Algebra II", "Emily Theodore")

classroom2 = Classroom([Student("AC-340014","Kent", "Carter",9), Student("AC-340024","Isaiah", "Chambers",10),Student("AC-340018","Leta", "Ferguson",7)], "English", "Daniel Pherb")

school = [classroom1, classroom2]


printHonorStudents(school)
