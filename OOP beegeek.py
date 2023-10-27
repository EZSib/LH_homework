'''декоратор в json'''
# import functools
# import json
# def jsonify(func):
#     @functools.wraps(func)
#     def wrapper(*a, **kw):
#         value = json.dumps(func(*a, **kw))
#         return value
#     return wrapper

'''соответсвие координатам'''
# import sys
# for line in sys.stdin:
#     print((90>= eval(line)[0] >= -90) and (180 >= eval(line)[1] >= -180))

'''итерация и количество элементов соотв. предикату'''
# import functools
# def quantify(func):
#     @functools.wraps(func)
#     def wrapper(iter, keys=None):
#         value = filter(iter, key=keys)
#         return value
#     return wrapper

import functools
# def quantify(itera, func):
#     predicate = func or bool
#     return len(list(filter(predicate, itera,)))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(quantify(numbers, lambda x: x > 1))

'''4 четверг '''

# import calendar
# import datetime
# year = int(input())
# mont = int(input())
# all_day = calendar.monthcalendar(year, mont)
# if len(list(filter(lambda x: x>0,all_day[0]))) < 4:
#     all_day = all_day[1:]
# print(datetime.datetime(year,mont,all_day[3][3]).strftime('%d.%m.%Y'))

'''это целое число'''

def is_integer(a):
    try:
        int(a)
        return True
    except:
        return (False)

print(is_integer('-0001'))
print(is_integer('0001'))
print(is_integer('5.0'))