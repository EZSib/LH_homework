'''1. Разработайте программу с использованием наследования классов, реализующую классы:
работник больницы; медсестра; хирург. Используя методы, не зная, с объектом какого класса
вы работаете, выведите на экран возраст и название должности.'''


class HospitalWorker():
    def __init__(self, age: int):
        self.age = age

    def printInfo(self):
        print(f'HospitalWorker больницы, возраст {self.age}')


class Surgeon(HospitalWorker):
    position = 2
    pos = 'Surgeon' if position >= 2 else ('Nurse' if position == 1 else 'HospitalWorker')

    def printInfo(self):
        print(f'{self.pos} больницы, возраст {self.age}')


class Nurse(HospitalWorker):
    position = 1
    pos = 'Surgeon' if position >= 2 else ('Nurse' if position == 1 else 'HospitalWorker')

    def printInfo(self):
        print(f'{self.pos} больницы, возраст {self.age}')


hospital_list = [stephen := Surgeon(37), mary := Nurse(26), rimus := HospitalWorker(67)]
for employee in hospital_list:
    employee.printInfo()

'''2. Разработайте программу, с тремя классами – Rectangle, Triangle, Circle, каждый из которых имеет методы perimeter() 
(расчет и возврат периметра фигуры) и area() (расчет и возврат площади фигуры). Создайте 7 произвольных фигур, сохраните
их в списке и циклом выполните вывод периметра и площади каждого объекта.'''


class Rectangle():
    def __init__(self, height: int | float, width: int | float):
        self.height = height
        self.width = width

    def perimeter(self):
        return f'Периметр прямоугольника со сторонами ' \
               f'{self.height} и {self.width} равен {round((self.height + self.width) * 2, 2)}'

    def area(self):
        return f'Площадь прямоугольника со сторонами {self.height} и {self.width} равна {round(self.height * self.width, 2)}'


class Triangle():
    def __init__(self, side_1: int | float, side_2: int | float, side_3: int | float):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def perimeter(self):
        return f'Периметр треугольника со сторонами ' \
               f'{self.side_1}, {self.side_2} и {self.side_3} равен {round(self.side_1 + self.side_2 + self.side_3, 2)}'

    def area(self):
        '''По формуле Герона'''
        self.half_p = (self.side_1 + self.side_2 + self.side_3) / 2
        return f'Площадь треугольника со сторонами {self.side_1}, {self.side_2} и {self.side_3} равна' \
               f' {round((self.half_p * (self.half_p - self.side_1) * (self.half_p - self.side_2) * (self.half_p - self.side_3)) ** 0.5, 2)}'


class Circle():
    def __init__(self, r: int | float):
        self.r = r
        self.pi = 3.14

    def perimeter(self):
        return f'Периметр круга с радиусом {self.r} равен {round(2 * self.pi * self.r, 2)}'

    def area(self):
        return f'Площадь круга с радиусом {self.r} равна {round(self.pi * self.r ** 2, 2)}'


list_shapes = [shape_1 := Circle(5),
               shape_2 := Circle(15),
               shape_3 := Triangle(2, 2, 3),
               shape_4 := Triangle(5, 5, 5),
               shape_5 := Rectangle(2, 2),
               shape_6 := Rectangle(14, 88),
               shape_7 := Rectangle(10, 74)]

for shape in list_shapes:
    print(shape.perimeter())
    print(shape.area())
