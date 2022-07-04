class Pen:
    def __init__(self):
        print('Pen')


class Pineapple:
    def __init__(self):
        print('Pineapple')


class PenPineapple(Pen, Pineapple):
    def __init__(self):
        super().__init__()


a = PenPineapple()
