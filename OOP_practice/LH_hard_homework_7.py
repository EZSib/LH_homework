import string
import time


class SetError(Exception):
    pass


class LoginError(SetError):
    pass


class PasswordError(SetError):
    pass


class LenError(SetError):
    pass


valid_characters = string.ascii_letters + string.digits + '_'


class User():

    def setLogin(self, login: str):
        self.login = login
        if any(map(lambda char: char not in valid_characters, (i for i in login))):
            raise LoginError('Логин должен состоять из латинских букв, цифр или _')
        if len(login) >= 20:
            raise LenError('Используйте Не более 20 знаков')
        print('Логин успешно изменен.')

    def setPassword(self, password: str):
        self.password = password
        if any(map(lambda char: char not in valid_characters, (i for i in password))):
            raise PasswordError('Пароль должен состоять из латинских букв, цифр или _')
        if len(password) >= 20:
            raise LenError('Используйте Не более 20 знаков')
        print('Пароль успешно изменен.')

    def confirmPassword(self, confirm: str):
        self.confirm = confirm
        if confirm != self.password:
            raise PasswordError('Неверный пароль')
        print('Пароль подтвержден.')

    def setAge(self, age: int):
        self.age = age
        if not isinstance(age, int):
            raise PasswordError('Укажите целое количество лет')


list_users = []


def NewUser(name):
    if name in list_users:
        print('Имя пользователя занято, используйте другое')
        NewUser(input('Придумайте имя пользователя\n'))
    else:
        list_users.append(name)
        name = User()
    f = False
    while f != True:
        try:
            name.setLogin(input('Придумайте логин\n'))
        except Exception as ex:
            print(ex)
        else:
            f = True
    f = False
    while f != True:
        try:
            name.setPassword(input('Придумайте пароль\n'))
            name.confirmPassword(input('Подтвердите пароль\n'))
        except Exception as ex:
            print(ex)
        else:
            f = True
    f = False
    while f != True:
        try:
            name.setAge(int(input('Сколько Вам полных лет\n')))
        except (Exception, TypeError) as ex:
            print('Укажите целое количество лет')
        else:
            f = True
    select = (int(input(f'1- Если хотите создать нового пользователя\n'
                        f'2- Если хотите посмотреть список зарегистрированных пользователей\n'
                        f'3- Если хотите выйти\n')))
    if select == 1:
        NewUser(input('Придумайте имя пользователя\n'))
    elif select == 2:
        print(list_users)
    else:
        print('All the best!')
        time.sleep(3)
        quit()
    select = int(input('1- Создать нового пользователя\n2- Выйти\n'))
    NewUser(input('Придумайте имя пользователя\n')) if select == 1 else print('All the best!'), time.sleep(3), quit()


NewUser(input('Придумайте имя пользователя\n'))
