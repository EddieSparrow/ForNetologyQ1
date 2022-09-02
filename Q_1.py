from typing import List


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def cal_average(self):
        grade_count = 0
        for key in self.grades:
            grade_count += len(self.grades[key])
        grade_sum = sum([sum(v) for v in self.grades.values()])
        avg = grade_sum / grade_count
        return avg

    def __str__(self):
        res = f'Имя: = {self.name}\n'\
              + f'Фамилия: = {self.surname}\n'\
              + f'Средняя оценка за домашние задания: = {self.cal_average()}\n'\
              + f'Курсы в процессе изучения: = {self.courses_in_progress}\n'\
              + f'Завершенные курсы: = {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, grades):
        super(Lecturer, self).__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def cal_average(self):
        grade_count = 0
        for key in self.grades:
            grade_count += len(self.grades[key])
        grade_sum = sum([sum(v) for v in self.grades.values()])
        avg = grade_sum / grade_count
        return avg

    def __str__(self):
        res = f'Имя: = {self.name}\n'\
              + f'Фамилия: = {self.surname}\n'\
              + f'Средняя оценка: = {self.cal_average()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: = {self.name}\n' + f'Фамилия: = {self.surname}'
        return res


def compare(self, other):
    if self.cal_average() < other.cal_average():
        print('Cреднняя оценка больше у ', other.name, '', other.surname)
    else:
        print('Cреднняя оценка больше у ', self.name, '', self.surname)


def avg_student(studentlist: List[Student], course):
    avg_count = 0
    avg_sum = 0
    for student in studentlist:
        if isinstance(student, Student) and course in student.grades.keys():
            values = student.grades[course]
            avg_count += len(values)
            avg_sum += sum(values)
    return (avg_sum/avg_count)


def avg_lecturer(lecturerlist: List[Lecturer], course):
    avg_count = 0
    avg_sum = 0
    for lecturer in lecturerlist:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades.keys():
            values = lecturer.grades[course]
            avg_count += len(values)
            avg_sum += sum(values)
    return (avg_sum/avg_count)


lecturer1 = Lecturer('Some', 'Buddy', [])
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Boss', 'Mega', [])
lecturer2.courses_attached += ['Python', 'Git']
student1 = Student('Ivan', 'Ivanov', 'M')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python', 'Git']
student2 = Student('James', 'Bond', 'M')
student2.finished_courses += ['Английский для начинающих']
student2.courses_in_progress += ['Python', 'C++', 'Java', 'Git']
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += 'Python', 'Git', 'C++', 'Java'
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Java', 5)
reviewer1.rate_hw(student2, 'Python', 5)
student1.rate_hw(lecturer1, 'Python', 5)
student1.rate_hw(lecturer1, 'Git', 5)
student2.rate_hw(lecturer2, 'Java', 1)
student2.rate_hw(lecturer2, 'Git', 1)
student2.rate_hw(lecturer2, 'Python', 3)
print(avg_student([student1, student2], 'Python'))
print(avg_lecturer([lecturer1, lecturer2], 'Python'))

print('Проверяющий 1')
print(reviewer1)
print('Лектор 1')
print(lecturer1)
print('Лектор 2')
print(lecturer2)
print('Студент 1')
print(student1)
print(student1.grades)
print('Студент 2')
print(student2)
print(student2.grades)
print('====')
compare(student1, lecturer1)
print(avg_student([student1, student2], 'Python'))
print(avg_lecturer([lecturer1, lecturer2], 'Python'))
