class User():
    def __init__(self, name, surname, year_b_date, city, hobby):
        self.name = name
        self.surname = surname
        self.year_b_date = year_b_date
        self.city = city
        self.hobby = hobby

    def printInfo(self):
        print(
            f'Имя: {self.name}\nФамилия: {self.surname}\nВозраст: {self.year_b_date}\n'
            f'Город: {self.city}\nХобби: {self.hobby}\n')

    def setName(self, rename):
        self.name = rename

    def setSurname(self, surname):
        self.surname = surname

    def setYear(self, year):
        self.year = year

    def setCity(self, city):
        self.city = city

    def setHobby(self, hobby):
        self.hobby = hobby


people_1 = User('Пётр', 'ВЕЛИКИЙ', 1672, 'Санкт-Петербург', 'Люблю вырезать деревянные игрушки')
people_2 = User('Peter', 'Griffin', 1966, 'Quahog', 'BEER')
people_3 = User('Максим', 'Матвеев', 2001, 'Тамбов', 'Плакать')

people_3.setName('Даша')
people_3.setSurname('Корейка')
people_3.setYear(2020)
people_3.setCity('Москва')
people_3.setHobby('Смеяться')

people_3.printInfo()


