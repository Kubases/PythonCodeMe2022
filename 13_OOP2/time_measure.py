from time import perf_counter


def time_passed_decorator(param_func):
    def nested():
        start = perf_counter()
        param_func()
        print(perf_counter() - start)
    return nested


@time_passed_decorator
def show():
    for i in range(500):
        pass


def main():
    show()


if __name__ == '__main__':
    main()
