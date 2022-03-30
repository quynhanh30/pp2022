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



def inputMark(courseid, students):
  print("enter marks of the course {courseid} for students: ")
  for student in students:
      mark = float(input(f"- Student {student['name']}: "))
      student["marks"][courseid] =  mark
  
def listCourses(courses):
  # how to list ?
  for course in courses:
    print(f"{course['id']: <10}  {course['name']: <20} ")  
  

def selectCourse(courses):
  listCourses(courses)
  courseid = input("enter course id from the above table: ")
  return courseid

def listStudents(students):
  print("\n all students list")
  for student in students:
    print(f"{student['id']: <10}  {student['name']: <20}  {student['dob']: <15} ")   
  
def showMark(courseid, students):
  print("\n all students marks for the course {courseid}")
  for student in students:
      print(f"{student['name']: <20}  {student['marks'][courseid]}")  


# q1: checking if a value existss or not
# q2: encapsulation

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