import datetime
import holidays
import random


class Student:
    min_avg = 4.5
    university_code = 'UAM'

    def __init__(self, first_name, last_name, age, student_avg):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_avg = student_avg

    @property
    def create_username(self):
        numbers = ''
        for _ in range(6):
            numbers = numbers + str(random.choice(range(9)))
        return f'{self.first_name}{self.last_name[:3]}{numbers}'.lower()

    @create_username.setter
    def create_username(self, username):
        pass

    @property
    def create_email(self):
        return f'{self.first_name}.{self.last_name}@{self.university_code}.com'.lower()

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @fullname.setter
    def fullname(self, last_first):
        self.last_name, self.first_name = last_first.split()

    @fullname.deleter
    def fullname(self):
        self.first_name, self.last_name = None, None
        print('Your data has been deleted')

    def __repr__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() + ', avg: ' + str(self.student_avg)

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @classmethod
    def change_uni(cls, uni_code):
        cls.university_code = uni_code

    @staticmethod
    def welcome(txt):
        print('Hello! ', txt)

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Poland()
        if day.weekday() in (5, 6) or day in pl_holidays:
            return 'No'
        else:
            return 'Yes'

    def grant_scholarship(self):
        if self.student_avg >= self.min_avg:
            print("Scholarship granted")
        else:
            print('Scholarship not granted')


anna = Student('Anna', 'Kowalska', 23, 4.7)
piotr = Student('Piotr', 'Nowak', 23, 3.8)
anna.grant_scholarship()
Student.set_min_avg(4)
print(anna.academic_day(datetime.date.today()))
print(anna.create_username)
