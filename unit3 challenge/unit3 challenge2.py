"""
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
"""

class student:

 def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):          # sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
                          key = lambda student: student.cgpa,
                          reverse = True)  #syntax - lambda arg:exp
  return sorted_students


#example usage:
students = [
    student("Vignesh", "A123", 7.8),
    student("Vaishnavi", "A124", 8.9),
    student("Lakshmi", "A125", 9.1),
    student("Ravi", "A126", 9.9),
]

sorted_students = sort_students(students)

#print the sorted list of student
for student in sorted_students:
  print("Name: {}, Roll Number: {}, cgpa: {}".format(student.name, student.roll_number, student.cgpa))