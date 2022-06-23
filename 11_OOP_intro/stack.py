class Stack:
    def __init__(self, value_list):
        self.value_list = value_list

    def show(self):
        print(self.value_list)

    def check_if_empty(self):
        return len(self.value_list) == 0

    def push(self, value):
        self.value_list.append(value)

    def get(self):
        return self.value_list.pop()


def main():
    first = Stack([3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12])
    first.show()
    print(first.get())
    first.push(1)
    first.get()
    while not first.check_if_empty():
        first.get()
    first.show()


if __name__ == '__main__':
    main()
