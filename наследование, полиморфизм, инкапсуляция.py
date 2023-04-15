# Наследование
class Paper():
    def __init__(self, name):
        self.name = name

    def show(self):
        print('I -', self.name)
class Document(Paper):
    is_subs = False

    def subs(self):
        self.is_subs = True
        print(self.name, 'Subscribed')

doc = Document('Very big 1234')
doc.subs()
doc.show()

# Полиморфизм

class Cat():
    def __init__(self, name):
        self.name = name
    def show(self):
        print('Cat', self.name)

    def say(self):
        print(self.name, '-Miay')


class Dog():
    def __init__(self, name):
        self.name = name

    def show(self):
        print('Dog', self.name)

    def say(self):
        print(self.name, '-woow-woof')

# Полиорфизм с наследством

class Animal():
    def type(self):
        print('Тип объекта животных')

    def age(self):
        print('Возраст животного')

class Rabbit(Animal):
    def age(self):
        print('Возраст кролика')

class Horse(Animal):
    def age(self):
        print('Возраст лошади')

# Инкапсуляция

# _value enable in class B from class A

class A():
    def __init__(self, value):
        self._value = value

class B(A):
    def show(self):
        print(self._value)

b = B(2)
b.show()

# __

class Tiger():
    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name

tiger1 = Tiger()
tiger1.setname('Tigronok')
print(tiger1.getname())