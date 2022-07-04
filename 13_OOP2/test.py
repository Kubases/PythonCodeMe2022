def wrapper(a):
    txt = 'closure'

    def nested(num):
        print("I'm in", txt * num, a)

    return nested


returned_func = wrapper(2)

returned_func(6)
