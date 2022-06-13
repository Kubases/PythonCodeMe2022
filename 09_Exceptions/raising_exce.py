class WeatherError(TypeError):
    """custom error"""
    pass


def get_weather():
    weather = input("Write weather -> sun / rain")

    if weather == 'sun':
        return weather
    elif weather == 'rain':
        return weather
    else:
        raise WeatherError("Weather not known")


def main():
    print(WeatherError.__base__)
    try:
        current_weather = get_weather()
    except TypeError as err:
        print(err)
    else:
        print(current_weather)


if __name__ == '__main__':
    main()
