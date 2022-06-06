import datetime


def is_car_relic(car):
    if datetime.date.today().year - int(car['year']) > 25:
        print(f"Your car {car['brand']} is a relic")
    else:
        print(f"Your car {car['brand']} is too young to be relic")


def print_car_dict(car):
    print(car)


def is_original(car):
    if car["is_original"]:
        print(f"Your car {car['brand']} is original")
    else:
        print(f"Your car {car['brand']} is not original")


def main():
    car = {
        "brand": None,
        "model": None,
        "year": None,
        "is_original": None
    }
    user_brand = input("Write brand of your car -> ")
    user_model = input("Write model of your car -> ")
    user_year = input("Write year of your car -> ")
    user_original = bool(input("Write 0/1 if your car is original -> "))
    car["brand"] = user_brand
    car["model"] = user_model
    car["year"] = user_year
    car["is_original"] = user_original
    print_car_dict(car)
    is_car_relic(car)
    is_original(car)


main()
