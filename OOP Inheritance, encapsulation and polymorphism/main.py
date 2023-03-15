class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)


    def grades(self):
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average_student(self):
        try:
            average_grade = sum(Student.grades(self)) / len(Student.grades(self))
            return round(average_grade, 1)
        except ZeroDivisionError:
            print("Нет оценок")
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
    def __str__(self):
       print(
                f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Student.average_student(self)}"
                f"\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\nКурсы завершены: {','.join(self.finished_courses)}")

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average_student()).__lt__(other.average_student())
    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average_student()).__le__(other.average_student())
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average_student()).__eq__(other.average_student())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def grades(self):
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        try:
            average_grade = sum(Lecturer.grades(self)) / len(Lecturer.grades(self))
            return round(average_grade, 1)
        except ZeroDivisionError:
            print("Нет курсов")

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average()).__lt__(other.average())

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average()).__le__(other.average())

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('...')
        return (self.average()).__eq__(other.average())

    def __str__(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.average(self)}")

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def courses_average(persons, course):
    if not isinstance(persons, list):
        return "Нет студента"
    estimation = []
    for student in persons:
        estimation.extend(student.grades.get(course, []))
    if not estimation:
        return "По такому курсу нет оценок"
    return round(sum(estimation) / len(estimation), 2)

ruoy_student = Student('Ruoy', 'Eman', 'man')
ivan_student = Student('Иван', 'Жаров', 'man')
ruoy_student.courses_in_progress += ['Python']
ruoy_student.finished_courses += ['C++']
ruoy_student.finished_courses += ['Git']
ivan_student.courses_in_progress += ['Python']
ivan_student.courses_in_progress += ['Java']

Some_mentor = Reviewer('Some', 'Buddy')
Petr_mentor = Reviewer('Петр', 'Сидоров')
Some_mentor.courses_attached += ['Python']
Some_mentor.courses_attached += ['C++']
Petr_mentor.courses_attached += ['Java']

Some_mentor.rate_st(ruoy_student, 'Python', 9)
Some_mentor.rate_st(ruoy_student, 'Python', 10)
Some_mentor.rate_st(ruoy_student, 'Python', 10)
Petr_mentor.rate_st(ivan_student, 'Python', 6)
Petr_mentor.rate_st(ivan_student, 'Python', 8)
Petr_mentor.rate_st(ivan_student, 'Python', 9)
Petr_mentor.rate_st(ivan_student, 'Java', 9)
Petr_mentor.rate_st(ivan_student, 'Java', 10)
Petr_mentor.rate_st(ivan_student, 'Java', 9)

Dima_lecturer = Lecturer('Дмитрий', 'Сидоров')
Gena_lecturer = Lecturer('Гена', 'Сидоров')
Dima_lecturer.courses_attached += ['Python']
Gena_lecturer.courses_attached += ['Java']

ruoy_student.rate_lec(Dima_lecturer, 'Python', 10)
ruoy_student.rate_lec(Dima_lecturer, 'Python', 9.6)
ruoy_student.rate_lec(Dima_lecturer, 'Python', 10)
ivan_student.rate_lec(Gena_lecturer, 'Python', 10)
ivan_student.rate_lec(Gena_lecturer, 'Python', 7)
ivan_student.rate_lec(Gena_lecturer, 'Python', 8)
ivan_student.rate_lec(Gena_lecturer, 'Java', 5)
ivan_student.rate_lec(Gena_lecturer, 'Java', 8)
ivan_student.rate_lec(Gena_lecturer, 'Java', 6)

print(ruoy_student.grades)
print(Some_mentor.courses_attached)
print(Dima_lecturer.grades)

print(f"Cредняя оценка за домашние задания Студентов: {courses_average(Student.student_list, 'Python')}")
print(f"Cредняя оценка Лекторов: {courses_average(Lecturer.lecturer_list, 'Python')}")

print(Dima_lecturer < Gena_lecturer)
# print(Dima_lecturer <= Gena_lecturer)
print(Dima_lecturer == Gena_lecturer)
print(ruoy_student < Gena_lecturer)

print(ruoy_student < ivan_student)