class Queue:
    def __init__(self, value_list=[]):
        self.value_list = value_list

    def print_queue(self):
        print(self.value_list)

    def check_if_empty(self):
        return len(self.value_list) == 0

    def put(self, value):
        self.value_list.append(value)

    def get(self):
        return self.value_list.pop(0)


def main():
    first = Queue([3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12])
    first.print_queue()
    print(first.get())
    first.put(1)
    first.print_queue()
    while first.check_if_empty():
        first.get()


if __name__ == '__main__':
    main()
