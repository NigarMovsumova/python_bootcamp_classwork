# Student, Teacher - 2 klass yaratmaq
# hansi attributlari ve metodlari ola biler
class Student:

    def __init__(self, name, surname, courses=[]):
        self.name = name
        self.surname = surname
        self.courses = courses

    def __str__(self):
        return 'Student: name: {}, surname: {}, courses: {}'.format(self.name, self.surname, self.courses)


student = Student('Ali', 'Zeynalov', ['Python', 'English'])

print(student)


class Teacher:

    def __init__(self, name, surname, position,
                 workplaces=[],
                 courses=[],
                 languages=['Azerbaijani']):
        self.name = name
        self.surname = surname
        self.position = position
        self.workplaces = workplaces
        self.courses = courses
        self.languages = languages

    def __str__(self):
        return 'Teacher: name: {}, surname:{}, position:{},\n workplaces={},\n' \
               'courses:{},\n languages:{}' \
            .format(self.name, self.surname, self.position, self.workplaces,
                    self.courses, self.languages)


teacher = Teacher('Nigar', 'Movsumova', 'Teacher',
                  ['Azerconnect', 'Step IT', 'Otus', 'OReilly'],
                  ['Python Bootcamp'],
                  ['Azerbaijani', 'English', 'Russian'])

print(teacher)
