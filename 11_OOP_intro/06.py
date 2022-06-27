class Employee:
    company = 'pythoncompany'

    def __init__(self, position,  salary, name, surname, len_of_service, student_status):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.len_of_service = len_of_service
        self.student_status = student_status
        self.email = gen_email(name + surname) + '@' + self.company + '.com'

    def salary_raise(self):
        self.salary = self.salary * 1.1

    def taxes(self):
        if self.student_status:
            print("No taxes to pay")
        else:
            print(f'Your salary after taxes is {self.salary - 0.23 * self.salary}')


def gen_email(text):
    chars_list = ['a', 'e', 'i', 'o', 'u', 'y']
    text = text.lower()
    for char in chars_list:
        text = text.replace(char, '')
    return text


def main():
    worker = Employee('worker', 2000, 'James', 'Smith', '3 years', 0)
    print(worker.email)
    worker.taxes()


if __name__ == '__main__':
    main()