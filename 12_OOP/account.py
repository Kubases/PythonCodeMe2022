class Account:
    def __init__(self, username):
        self.username = username
        self.__account_number = '12345'

    def getter(self):
        return self.__account_number

    def setter(self, num):
        self.__account_number = num


w = Account('abc')
print(w.getter())
