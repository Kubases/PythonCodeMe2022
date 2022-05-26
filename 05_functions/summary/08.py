def is_car_relic(car):
    if 2022 - int(car['year']) > 25: # tutaj poprawic
        print(f"Your car {car['model']} is a relic")
    else:
        print()


def print_car_dict(car):
    print(car)


def main():
    car = {
        "brand": None,
        "model": None,
        "year": None
    }
    user_brand = input("Write brand of your car -> ")
    user_model = input("Write model of your car -> ")
    user_year = input("Write year of your car -> ")
    car["brand"] = user_brand
    car["model"] = user_model
    car["year"] = user_year
    print_car_dict(car)
    is_car_relic(car)


main()
