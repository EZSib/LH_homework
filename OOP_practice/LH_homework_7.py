'''1. Создать класс User. В нем определить метод setLogin(login). Логин должен содержать только латинские буквы,
цифры и знак подчеркивания. Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям,
необходимо выбросить WrongLoginException.'''

'''2. В класс User добавить метод setPassword(password). Password должен содержать только латинские буквы, цифры и знак подчеркивания.
Длина password должна быть меньше 20 символов. Также password и confirmPassword должны быть равны.
Если password не соответствует этим требованиям, необходимо выбросить WrongPasswordException.'''
import string

valid_characters = string.ascii_letters + string.digits + '_'

class User():

    def setLogin(self, login: str):
        self.login = login
        if len(login) >= 20 or any(map(lambda char: char not in valid_characters, (i for i in login))):
            raise Exception('WrongLoginException')
        print('Логин успешно изменен.')

    def setPassword(self, password: str):
        self.password = password
        if len(password) >= 20 or any(map(lambda char: char not in valid_characters, (i for i in password))):
            raise Exception('WrongPasswordException')
        print('Пароль успешно изменен.')

    def confirmPassword(self, confirm: str):
        self.confirm = confirm
        if confirm != self.password:
            raise Exception('WrongPasswordException')
        print('Пароль подтвержден.')


try:
    first = User()
    first.setLogin()
    first.setPassword()
    first.confirmPassword()
except Exception as ex:
    print(ex)
