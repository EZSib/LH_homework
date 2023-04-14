# Задание номер 1.
from datetime import datetime as dt

year_now = dt.now().year
user_date_req = ['Введите ваше имя',
                 'Введите вашу фамилию',
                 'Введите год рождения',
                 'Введите город проживание',
                 'Ваше хобби',
                 'Ваш рост',
                 'Ваш вес']
user_date = [input(i) for i in user_date_req]
print('Обрабатываю информацию…')
print(f'Имя:{user_date[0]}', f'Фамилия:{user_date[1]}', f'Возраст:{year_now - int(user_date[2])}',
      f'Город:{user_date[3]}',
      f'Хобби:{user_date[4]}', f'Рост:{user_date[5]}', f'Вес:{user_date[6]}', sep='\n')
# Задание номер 2.

print('odd' if int(input()) % 2 else 'even')
