grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = {}

# Используем цикл для обработки каждого ученика и его оценок
for student, grade_list in zip(sorted(students), grades):
    average_grade = sum(grade_list) / len(grade_list)
    average_grades[student] = round(average_grade, 2)

print(average_grades)

#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#students_list = sorted(list(students))
#grades_list = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])
#students_ball = {}
#students_ball.update({students_list[0]: grades_list[0], students_list[1]: grades_list[1], students_list[2]: grades_list[2], students_list[3]: grades_list[3], students_list[4]: grades_list[4]})
#print(students_ball)

def generate_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

# Пример использования функции для чисел от 3 до 20
for n in range(3, 21):
    password = generate_password(n)
    # print(generate_password(n))
    print(f"{n} - {password}")