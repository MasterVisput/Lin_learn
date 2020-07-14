import re
import json
from collections import Counter

# Объявляем переменную хранящую путь до файла
filename = '../logs/access-39204-d17ad0.log'
# объявляем переменные, хранящие регулярные выражения
re_ip_add = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
re_methods = r'"[A-Z]+'


# Функция выполняет чтение из файла и запись в список значений
# Подходящих условиям переданного регулярного выражения
def reader(reg):
    with open(filename) as f:
        log = f.read()
        res_list = re.findall(reg, log)
    return res_list


# Функция принимает список и подсчитывает колличество уникальных значений
# Возвращает словарь
def count(res_list, reg=None):
    count = Counter(res_list)
    if len(count) > 0:
        return count
    else:
        return {reg: 0}


def dict_answ_builder():
    answ_dict = {
        'All requests': len(reader(re_ip_add)),
        'Count requests by method': {
            'GET': count(reader('GET'), 'GET')['GET'],
            'POST': count(reader('POST'), 'POST')['POST'],
            'UPDATE': count(reader('UPDATE'), 'UPDATE')['UPDATE'],
            'DELETE': count(reader('DELETE'), 'DELETE')['DELETE'],
            'OPTIONS': count(reader('OPTIONS'), 'OPTIONS')['OPTIONS'],
        },
        'TOP 10 IP addresses': {'#1': sort_list(count(reader(re_ip_add)))[0],
                                '#2': sort_list(count(reader(re_ip_add)))[1],
                                '#3': sort_list(count(reader(re_ip_add)))[2],
                                '#4': sort_list(count(reader(re_ip_add)))[3],
                                '#5': sort_list(count(reader(re_ip_add)))[4],
                                '#6': sort_list(count(reader(re_ip_add)))[5],
                                '#7': sort_list(count(reader(re_ip_add)))[6],
                                '#8': sort_list(count(reader(re_ip_add)))[7],
                                '#9': sort_list(count(reader(re_ip_add)))[8],
                                '#10': sort_list(count(reader(re_ip_add)))[9],
                                }

    }
    return answ_dict


def sort_list(res_list):
    list_d = [(k, res_list[k]) for k in sorted(res_list, key=res_list.get, reverse=True)]
    list_res = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list_res:
        if i +1 <= len(list_d):
            list_res[i] = (list_d[i][0])
        else:
            list_res[i] = ('-')
    return list_res


print(json.dumps(dict_answ_builder()))
