# Функции

def average_grade(grades_dict):
    value_grades = 0
    sum_grades = 0
    for grade_list in grades_dict.values():
        for grade in grade_list:
            sum_grades += grade
            value_grades += 1
    average_grades = sum_grades / value_grades
    return average_grades

# Описание классов

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_surname = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {round(average_grade(self.grades), 2)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}\n'''

        return name_surname


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        name_surname = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(average_grade(self.grades), 2)}\n'
        return name_surname


class Reviewer(Mentor):

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_surname = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return name_surname


# Создание экземпляров

student_1 = Student('George', 'Chernousov', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Peter', 'Parker', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Gwen', 'Stacy', 'female')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Git']
student_3.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Otto', 'Octavius')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Curtis', 'Connors')
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Guido', 'van Rossum')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Linus', 'Torvalds')
lecturer_2.courses_attached += ['Git']


# Выставляем оценки

reviewer_1.rate_student(student_1, 'Python', 8)
reviewer_1.rate_student(student_1, 'Python', 10)
reviewer_1.rate_student(student_1, 'Python', 9)
reviewer_1.rate_student(student_2, 'Python', 10)
reviewer_1.rate_student(student_2, 'Python', 6)
reviewer_1.rate_student(student_2, 'Python', 7)
reviewer_1.rate_student(student_3, 'Python', 9)
reviewer_1.rate_student(student_3, 'Python', 9)
reviewer_1.rate_student(student_3, 'Python', 5)

reviewer_2.rate_student(student_1, 'Git', 8)
reviewer_2.rate_student(student_1, 'Git', 9)
reviewer_2.rate_student(student_2, 'Git', 10)
reviewer_2.rate_student(student_2, 'Git', 6)
reviewer_2.rate_student(student_3, 'Git', 10)
reviewer_2.rate_student(student_3, 'Git', 9)

print(f'Оценки студента {student_1.name} {student_1.surname}: {student_1.grades}')
print(f'Оценки студента {student_2.name} {student_2.surname}: {student_2.grades}')
print(f'Оценки студента {student_3.name} {student_3.surname}: {student_3.grades}')
print()

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 8)
student_3.rate_lecturer(lecturer_1, 'Python', 10)
student_3.rate_lecturer(lecturer_1, 'Python', 9)
student_3.rate_lecturer(lecturer_2, 'Git', 10)

print(f'Оценки лектора {lecturer_1.name} {lecturer_1.surname}: {lecturer_1.grades}')
print(f'Оценки лектора {lecturer_2.name} {lecturer_2.surname}: {lecturer_2.grades}')
print()

# Выводим информацию о студентах, лекторах и экспертах:

print('Информация по студентам:\n')
print(student_1)
print(student_2)
print(student_3)
print()

print('Информация по лекторам:\n')
print(lecturer_1)
print(lecturer_2)
print()

print('Информация по экспертам:\n')
print(reviewer_1)
print(reviewer_2)
print()