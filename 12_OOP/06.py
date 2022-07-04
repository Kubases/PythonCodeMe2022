class Country:
    def __init__(self, area, population, language, capital_city):
        self.area = area
        self.population = population
        self.language = language
        self.capital_city = capital_city

    def show(self):
        print('Area: ', self.area)
        print('Population: ', self.population)
        print('Language: ', self.language)
        print('Capital city: ', self.capital_city)


def init_data():
    germany = Country(357588, 83.24, 'German', 'Berlin')
    poland = Country(322575, 38, 'Polish', 'Warsaw')
    czech_republic = Country(78871, 10.7, "Czech", 'Prague')
    countries_list = [germany, poland, czech_republic]
    return countries_list


def show_countries(countries_list):
    for country in countries_list:
        country.show()
        print()


def main():
    countries_list = init_data()
    show_countries(countries_list)


if __name__ == '__main__':
    main()
