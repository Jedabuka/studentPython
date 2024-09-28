import requests
import pandas
import numpy


r = requests.get('https://www.python.org')
print(r)
print(r.status_code)
print(b'Python is a programming language' in r.content)


students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pandas.DataFrame(students_marks_dict)
print(students)
print(students.index)
print(students.columns)
students.index = ["I", "II", "III"]
print(students)


a = numpy.array([1, 2, 3, 4])
b = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(a)
print(b)
c = numpy.ones((5, 5))
print(c)
d = numpy.ones((3, 10), dtype='int32')
print(d)
e = numpy.arange(1, 9, 0.3)
print(e)
f = numpy.linspace(1, 20, 20)
print(f)

