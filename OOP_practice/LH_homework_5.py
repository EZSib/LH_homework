# Задание номер 1
class User():
    name = ''
    surname = ''
    year_b_date = 0
    city = ''
    hobby = ''


people_1 = User()
people_1.name = 'Пётр'
people_1.surname = 'ВЕЛИКИЙ'
people_1.year_b_date = 1672
people_1.city = 'Санкт-Петербург'
people_1.hobby = 'Люблю вырезать деревянные игрушки'

people_2 = User()

people_2.name = 'Peter'
people_2.surname = 'Griffin'
people_2.year_b_date = 1966
people_2.city = 'Quahog'
people_2.hobby = 'BEER'

print(people_1.year_b_date, people_2.year_b_date, sep='\n')


# Задание номер 2.
class User():
    def __init__(self, name, surname, year_b_date, city, hobby):
        self.name = name
        self.surname = surname
        self.year_b_date = year_b_date
        self.city = city
        self.hobby = hobby

    def printInfo(self):
        print(
            f'Имя: {self.name}\nФамилия: {self.surname}\nВозраст: {self.year_b_date}\nГород: {self.city}\nХобби: {self.hobby}\n')


User.printInfo(people_2)
User.printInfo(people_1)
