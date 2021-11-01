class Student:
    list_of_students = {}
    list_of_course = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_coursed = []
        self.courses_in_progress = []
        self.grades = {}
        Student.list_of_students[self.name + ' ' + self.surname] = self.grades
        Student.list_of_course.append(self.courses_in_progress)

    def evaluate_the_lecturer(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.course_of_study:
            if course in lecture.grades:
                lecture.grades[course].append(grade)
            else:
                lecture.grades[course] = [grade]

    def iterable(self):
        courses_in_progress_str = ''
        if 0 < len(self.courses_in_progress) <= 1:
            for i in self.courses_in_progress:
                courses_in_progress_str = courses_in_progress_str + " " + i
        elif len(self.courses_in_progress) > 1:
            count = 0
            for i in self.courses_in_progress:
                count = count + 1
                if count < len(self.courses_in_progress):
                    courses_in_progress_str = courses_in_progress_str + " " + i + ","
                elif count == len(self.courses_in_progress):
                    courses_in_progress_str = courses_in_progress_str + " " + i
        finished_coursed_str = ''
        if 0 < len(self.finished_coursed) <= 1:
            for i in self.finished_coursed:
                finished_coursed_str = finished_coursed_str + ' ' + i
        elif len(self.finished_coursed) > 1:
            count = 0
            for i in self.finished_coursed:
                count = count + 1
                if count < len(self.finished_coursed):
                    finished_coursed_str = finished_coursed_str + ' ' + i + ','
                if count == len(self.finished_coursed):
                    finished_coursed_str = finished_coursed_str + ' ' + i

        if len(self.finished_coursed) > 0:
            return 'Курсы в процессе изучения: ' + courses_in_progress_str + '\n' + 'Пройденные курсы: ' + finished_coursed_str
        else:
            return 'Курсы в процессе изучения: ' + courses_in_progress_str

    def comparison_of_ratings(self, student):
        if isinstance(student, Student):
            print('\n')
            if self.average_grade() > student.average_grade():
                return f'Студент {self.name} {self.surname} со средней оценкой {self.average_grade()} превосходит в учебе студента {student.name} {student.surname} со средней оценкой {student.average_grade()}'
            elif self.average_grade() == student.average_grade():
                return f'У студентов {self.name} {self.surname} и {student.name} {student.surname} одинаковая средняя оценка равная {student.average_grade()} '
            else:
                return f'Студент {student.name} {student.surname} со средней оценкой {student.average_grade()} превосходит в учебе студента {self.name} {self.surname} со средней оценкой {self.average_grade()}'

    def average_grade(self):
        if len(self.grades) > 0:
            count = 0
            count_v = 0
            for k, v in self.grades.items():
                for i in v:
                    count = count + 1
                    count_v = count_v + i
            return f'{count_v / count:.2f}'
        else:
            return 0

    def __str__(self):
        return 'Анкетные данные студента:' + '\n' + 'Имя: ' + self.name + ' \n' + 'Фамилия: ' + self.surname + '\n' + self.iterable() + '\n' + 'Средняя оценка равна: ' + self.average_grade() + '\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_of_study = []


class Reviewer(Mentor):  # Проверяют домашние задания
    def put_grades(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_of_study and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                my_list = [grade]
                student.grades[course] = my_list

    def __str__(self):
        return 'Анкетные данные проверяющего: ' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n'


class Lecturer(Mentor):  # проводят лекции и получают оценки от студентов
    list_of_lectures = {}
    list_of_courses = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.list_of_lectures[self.name + ' ' + self.surname] = self.grades
        Lecturer.list_of_courses.append(self.course_of_study)

    def average_rating(self):
        if len(self.grades) > 0:
            val = 0
            count = 0
            for k, v in self.grades.items():
                for i in v:
                    val = val + i
                    count = count + 1
            return f'{val / count:.2f}'
        else:
            return 0

    def comparison_of_ratings(self, lecture):
        if isinstance(lecture, Lecturer):
            print('\n')
            if self.average_rating() > lecture.average_rating():
                return f'Приз зрительских симпатий у студентов завоевывает {self.name} {self.surname} со средним баллом {self.average_rating()}'
            elif self.average_rating() == lecture.average_rating():
                return f'У нас 2 победителя со средним баллом {lecture.average_rating()}'
            else:
                return f'Приз зрительских симпатий у студентов завоевывает {lecture.name} {lecture.surname} со средним баллом {lecture.average_rating()}'

    def __str__(self):
        return 'Анкетные данные лектора: ' + '\n' + 'Имя: ' + self.name + ' \n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка: ' + str(
            self.average_rating()) + '\n'


def average_student_grade(result, count_of_st):
    number_of_ratings = 0
    sum_of_ratings = 0
    count = 0
    for k, v in Student.list_of_students.items():
        for key, val in v.items():
            if result == key:
                count += 1

    for k, v in Student.list_of_students.items():
        for key, val in v.items():
            if result == key:
                while count_of_st != count:
                    print('Правильное число студентов: ', count)
                    count_of_st = int(input('Введите правильное количество студентов: '))
                for grade in val:
                    sum_of_ratings += grade
                    number_of_ratings += 1
    print(
        f'Средняя оценка у студентов по курсу {result}: {sum_of_ratings / number_of_ratings:.2f}. Количество студентов на курсе: {count} человек')


def average_rating_of_lecturers(course_name, lecture_count):
    count = 0
    for k, v in Lecturer.list_of_lectures.items():
        for key, val in v.items():
            if course_name == key:
                count += 1

    while lecture_count != count:
        print(f'Правильное количество лекторов: {count}')
        lecture_count = int(input('Введите правильное число лекторов: '))

    number_of_ratings = 0
    sum_of_ratings = 0

    for k, v in Lecturer.list_of_lectures.items():
        for key, val in v.items():
            if course_name == key:
                for i in val:
                    number_of_ratings += 1
                    sum_of_ratings += i

    print(
        f'Среднее оценка у лекторов по курсу {course_name} равна:  {sum_of_ratings / number_of_ratings:.2f}. Количество лекторов {count}')


my_student = Student('Anuar', 'Omarov', 'men')
your_student = Student('Устин', 'Морозов', 'men')

my_reviewer = Reviewer('Petr', 'Ivanov')
your_reviewer = Reviewer('Гариб', 'Тагиев')


my_reviewer.course_of_study.append('Python')
my_student.courses_in_progress.append('Python')
your_student.courses_in_progress.append('Python')

my_reviewer.put_grades(my_student, 'Python', 152)
my_reviewer.put_grades(my_student, 'Python', 5)
my_reviewer.put_grades(your_student, 'Python', 5)
my_reviewer.put_grades(your_student, 'Python', 1)
my_reviewer.put_grades(your_student, 'Python', 2)
my_reviewer.put_grades(your_student, 'Python', 2)
my_reviewer.put_grades(your_student, 'Python', 2)
my_lecture = Lecturer('Lector', 'Gannibal')
your_lecture = Lecturer('Lector2', 'Gannibal2')
my_lecture.course_of_study.append('Python')
your_lecture.course_of_study.append('Python')
my_student.evaluate_the_lecturer(my_lecture, 'Python', 5)
my_student.evaluate_the_lecturer(your_lecture, 'Python', 5)
your_student.evaluate_the_lecturer(your_lecture, 'Python', 8)
your_student.evaluate_the_lecturer(my_lecture, 'Python', 1)
print(my_student)
print(your_student)
print(my_reviewer)
print(your_reviewer)
print(my_lecture)
print(your_lecture)

print(my_lecture.comparison_of_ratings(your_lecture))
print(my_student.comparison_of_ratings(your_student))

set_of_course_lectures = set()
for i in Lecturer.list_of_courses:
    for k in i:
        set_of_course_lectures.add(k)

set_of_course = set()
for i in Student.list_of_course:
    for k in i:
        set_of_course.add(k)

name_of_course = None
while name_of_course not in set_of_course or name_of_course not in set_of_course_lectures:
    name_of_course = input('Введите название курса Лектора: ')
else:
    count_lectures = int(input('Введите количество лекторов: '))
    average_rating_of_lecturers(name_of_course, count_lectures)

finish = 0
while finish == 0:
    result = input('Введите наименование курса: ')
    if result in set_of_course:
        finish = 1
        count_of_students = int(input('Введите количество студентов: '))
        average_student_grade(result, count_of_students)
