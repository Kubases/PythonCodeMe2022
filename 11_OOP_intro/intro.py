class Student:
    university_code = 'UAM'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def create_email(self):
        return f'{self.first_name}.{self.last_name}@{self.university_code}.com'.lower()

    def hello(self):
        print("Hello")


anna = Student('Anna', 'Kowalska', 23)
piotr = Student('Piotr', 'Nowak', 23)
print(anna.first_name, anna.last_name, anna.age, anna.create_email())
print(piotr.first_name, piotr.last_name, piotr.age, piotr.create_email())
anna.university_code = 'put'
print(anna.create_email())

anna.hello()
Student.hello(anna)




