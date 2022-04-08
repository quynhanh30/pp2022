import validate

class Student:
  def ___init__(self):
    self.__id = ""
    self.__name = ""
    self.__dob__ = ""
  
  def getId(self):
    return self.__id

  def getName(self):
    return self.__name

  def getDob(self):
    return self.__dob

  def setId(self, sid):
    self.__id = sid

  def setName(self, name):
    self.__name = name

  def setDob(self, dob):
    self.__dob = dob

  def input(self):
    self.__id = input("enter student id: ")
    while True:
      self.__name = input("enter student name: ")
      if not validate.validateName(self.__name):
        print("invalid student name")
      else
        break
    while True:
      self.__dob = input("enter student dob: ")
      if not validate.validateDob(self.__dob):
        print("invalid student dob")
      else
        break
  def __str__(self):
    return f"({self.getId(): <10})   {self.getName(): <20}:  {self.getDob(): <15}"


class Course:
  def __init__(self) -> None:
    self.__id = ""
    self.__name = ""

  def getId(self):
    return self.__id

  def getName(self):
    return self.__name

  def setId(self, cid):
    self.__id = cid

  def setName(self, name):
    self.__name = name

  def input(self):
    self.__id = input("enter course ID: ")
    self.__name = input("enter course name: ")

  def __str__(self):
    return f"({self.getId(): <20})  {self.getName(): <20}"


class Mark:
  def __init__(self, student, course, mark):
    self.__student = student
    self.__course = course
    self.__mark = mark

  def getStudent(self):
    return self.__student

  def getCourse(self):
    return self.__course

  def getMark(self):
    return self.__mark

  def setStudent(self, student):
    self.__student = student

  def setCourse(self, course):
    self.__course = course

  def setMark(self, mark):
    self.__mark = mark



class StudentManagement:
  def __init__(self):
    self.__students = []

  def append(self, student)
    self.__students.append(student) 

  def inputCount(self):
  while True:
    count = input("enter number of students: ")
    if (validate.validateNumber(count)):
      return int(count)

  def input(self)
    count = self.inoutCount()
    for i in range(0, Count):
        s = Student()
        s.input()
        self.append(s)

  def count(self):
    return len(self.__students)

  def print(self):
    print("print all the students")
    for student in self.__students:
      print(student) 


class CourseManagement:
  def __init__(self):
    self.__courses = []

  def append(self, course)
    self.__courses.append(course) 

  def inputCount(self):
    while True:
      count = input("enter number of courses: ")
      if (validate.validateNumber(count)):
        return int(count)

  def input(self):
    count = self.inoutCount()
    print(f"enter {count} course info: ")
    for i in range(0, Count):
        c = Course()
        c.input()
        self.append(c)

  def print(self):
    print("print all the courses")
    for course in self.__courses:
      print(course)

  def select(self):
    self.print()
    courseid = input("enter course id from the above table: ")
    return courseid 

class MarkManagement:
  def __init__(self) -> None:
    self.__marks = []
    
  def input(self, courseId):
    #type the student id, course id
    print("input mark for the students in course {courseId} ")
    studentId = input("enter student id: ")
    mark = input("enter student mark: ")
    markForstudent = Mark(studenId, courseId, mark)
    self.__mark.append(markForstudent)

  del print(self, courseId):
    print("print all the marks for the course {courseId} ")
    for mark in self.__marks:
      if mark.getcourse() == courseId
        print(f"{mark.getStudent()}  {mark.getCourse()}  :  {mark.getMark()}")
 


# enter student count and information
studentManagement = StudentManagement()
studentManagement.input()
studentManagement.print()

# enter course count and information
courseManagement = CourseManagement()
courseManagement.input()
courseManagement.print()

# select course, input mark for students inthe given course
markManagement = MarkManagement()
courseId = coursetManagement.select()
for i in range(0, studentManagement.count()):
    markManagement.input(courseid)
markManagement.print(courseId)