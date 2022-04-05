class Students:
  listStudents = []
  def __init__(self, n, a):
      self.id = i
      self.name = n
      self.dob = d
      self.marks = m
  def describe(self):
    print("Id:", self.id)
    print("Name:", self.name)
    print("Dob:", self.dob)
    print("Marks:", self.marks)
  def __lt__(self, other):
    return self.marks < other.marks
  def __str__(self):
    return f"My name is {self.name}. My id {self.id}."

  def inputStudentCount():
   count = int(input("enter number of students: "))
   return count
   
  def inputStudentInfo(studentCount):   
   """
   Return a list of students, with info from keyboard
   """
   students = []
  
   # input info: id, name, dob
   for i in range(0, studentCount):
     s = {}
     id = input("enter student ID: ")
     name = input("enter student Name: ")
     dob = input("enter student DoB: ")
     student = {
         "id": id,
         "name": name,
         "dob": dob,
         "marks": {}  
     }
     students.append(student)

   return students
 

  def listStudents(students):
   print("\n all students list")
   for student in students:
     print(f"{student['id']: <10}  {student['name']: <20}  {student['dob']: <15} ")   
  
  def inputStudentCount(self)
  def inputStudentInfo(self)
  def getListStudents(self)
 

class Courses(Students):

  def inputCourseCount():
    count = int(input("enter number of courses: "))
    return count 
  def inputCourseInfo(courseCount):
   """
   Return a list of courses: {id, name}
   """
   courses = []
  
   # input info: id, name, dob
   for i in range(0, studentCount):
     s = {}
     id = input("enter course ID: ")
     name = input("enter course Name: ")
     course = {
         "id": id,
         "name":name     
     }
     courses.append(course)

    return courses
  def set_term(self, term):
    print(f"Setting term to {term}")
    self.term = term
  
  def selectCourse(courses):
    listCourses(courses)
    courseid = input("enter course id from the above table: ")
    return courseid

class Courses(Students, Marks):
  def set_term(self, term):
    print(f"Setting term to {term}")
    self.term = term
  def describe(self):
    super().describe()
    print("Term:", self.term)
  def work(self):
    super().mark() # from Students

class Marks:
  def mark(self):
    print("Mark of student...")
  def __init__(self):
    self.__student = 0
  def _get_student(self):
    return self.__student
  def set_student(self, student):
    self.__student = student
  def mark(self):
    if self.__student == 0:
      print("I should be paid...")
    else:
      print("I am well paid!")
  def showMark(courseid, students):
    print("\n all students marks for the course {courseid}")
    for student in students:
        print(f"{student['name']: <20}  {student['marks'][courseid]}")  
  # enter student count and information
  studentCount = inputStudentCount()
  students = inputStudentInfo(studentCount)
  listStudents(students)

  # enter course count and information
  courseCount = inputCourseCount()
  courses = inputCourseInfo(courseCount)
  listCourses(courses)

  # select course, input mark for students inthe given course
  courseid = selectCourse(courses)
  inputMark(courseid, students)

  # show mark for a given course
  courseid = selectCourse(courses)
  showMark(courseid, students)