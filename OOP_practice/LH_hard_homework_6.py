class Chemist():
    def setName(self, name: str):
        self.__name = name

    def getName(self):
        return self.__name

    def setHobby(self, hobby: str):
        self.__hobby = hobby

    def getHobby(self):
        return f'Любит {self.__hobby}'

    def setAge(self, age: int):
        self.__age = age
    def setAssistant(self, asis_name: str):
        self.__asis_name = asis_name

    def setInjuries(self, injuries: bool):
        self.__injuries = injuries


    def getAge(self):
        return f'Полных лет {self.__age} '
    def getAssistant(self):
        return f'Работет с {self.__asis_name}'
    def getInjuries(self):
        return 'Есть производственная травма' if self.__injuries else 'Абсолютно здоров'

