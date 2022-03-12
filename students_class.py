# Функции

def average_grade(grades_dict):
    """Функция для подсчета средней оценки студентов/лекторов по ВСЕМ курсам
    """
    value_grades = 0
    sum_grades = 0
    for grade_list in grades_dict.values():
        for grade in grade_list:
            sum_grades += grade
            value_grades += 1
    average_grades = sum_grades / value_grades
    return average_grades

def average_students_grade(student_list, course):
    """Функция для подсчета и вывода средней оценки студента по заданному курсу
    """
    for data in student_list:
        if course in data.grades.keys():
            print(f'Средняя оценка за курс {course}:\n')
            sum_g = 0
            for student in student_list:
                num_g = len(student.grades[course])
                for grades in student.grades[course]:
                    sum_g += grades
                avr = sum_g / num_g
                sum_g = 0
                print(f'{student.name} {student.surname}: {round(avr, 1)}')
            print()
            break
        else:
            print(f'По курсу {course} ничего не найдено\n')
            break

def average_lecturers_grade(lecturers_list, course):
    """Функция для подсчета и вывода средней оценки лектора по заданному курсу
    """
    for lecturer in lecturers_list:
        if course in lecturer.grades.keys():
            num_x = len((lecturer.grades[course]))
            sum_x = 0
            print(f'Средняя оценка лекторов, преподающих {course}:')
            for grade in lecturer.grades[course]:
                sum_x += grade
            avr = sum_x / num_x
            print(f'{lecturer.name} {lecturer.surname}: {round(avr, 1)}\n')
            break


# Описание классов

class Student:

    student_list =[]

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        student_info = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {round(average_grade(self.grades), 1)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}\n'''
        return student_info

    def __ne__(self, other):
        if average_grade(self.grades) != average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result

    def __gt__(self, other):
        if average_grade(self.grades) > average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result

    def __ge__(self, other):
        if average_grade(self.grades) >= average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def __str__(self):
        lecturer_info = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                        f'Средняя оценка за лекции: {round(average_grade(self.grades), 1)}\n'
        return lecturer_info

    def __ne__(self, other):
        if average_grade(self.grades) != average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result

    def __gt__(self, other):
        if average_grade(self.grades) > average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result

    def __ge__(self, other):
        if average_grade(self.grades) >= average_grade(other.grades):
            result = 'True'
        else:
            result = 'False'
        return result


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
        reviewer_info = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return reviewer_info


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
reviewer_1.rate_student(student_3, 'Python', 10)
reviewer_1.rate_student(student_3, 'Python', 6)

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
print('-----------------------------')
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
print('-----------------------------')
print()


# Сравним средние оценки студентов и лекторов

print('Сравнения средних оценок студентов:\n')

print('student_1 == student_2:', student_1 == student_2)
print('student_1 != student_3:', student_1 != student_3)
print('student_2 == student_3:', student_2 == student_3)
print()
print('student_1 > student_2:', student_1 > student_2)
print('student_3 < student_2:', student_3 < student_2)
print('student_3 > student_1:', student_3 > student_1)
print('student_2 < student_3:', student_2 < student_3)
print()
print('student_2 >= student_3:', student_2 >= student_3)
print('student_3 <= student_1:', student_3 <= student_1)
print('student_1 >= student_3:', student_1 >= student_3)
print('student_3 <= student_2:', student_3 <= student_2)
print()

print('Сравнения средних оценок лекторов:\n')

print('lecturer_1 == lecturer_2:', lecturer_1 == lecturer_2)
print('lecturer_1 != lecturer_2:', lecturer_1 != lecturer_2)
print('lecturer_1 > lecturer_2:', lecturer_1 > lecturer_2)
print('lecturer_1 < lecturer_2:', lecturer_1 < lecturer_2)
print('lecturer_1 >= lecturer_2:', lecturer_1 >= lecturer_2)
print('lecturer_2 <= lecturer_1:', lecturer_2 <= lecturer_1)
print()
print('-----------------------------')
print()

# Выведем средние оценки у студентов и лекторов по курсам:

student_list = Student.student_list
lecturer_list = Lecturer.lecturer_list

print('Средние оценки студентов:\n')

average_students_grade(student_list, 'Python')
average_students_grade(student_list, 'Java')
average_students_grade(student_list, 'Git')

print('Средние оценки лекторов:\n')

average_lecturers_grade(lecturer_list, 'C++')
average_lecturers_grade(lecturer_list, 'Python')
average_lecturers_grade(lecturer_list, 'JAVA')
average_lecturers_grade(lecturer_list, 'Git')