from module import new_contact_csv
from module import new_contact_txt

import view as v
import module as m


def greeting():
    print("Добро пожаловать в телефонный справочник!")


def start():
    options = [input_data, del_data, find_data]
    return options[v.show_menu() - 1]()


def file_format():
    form = input(
        'Введите цифру в какой формат нужно экспортировать: "txt" = 1 или "csv" = 2: ')
    if form == "":
        form = None
    return form


def file_format_find():
    gorm = input(
        'Введите цифру в каком формате нужно произвести поиск: "txt" = 1 или "csv" = 2: ')
    if gorm == "":
        gorm = None
    return gorm


def file_format_delete():
    korm = input(
        'Введите цифру в каком формате нужно произвести удаление: "txt" = 1 или "csv" = 2: ')
    if korm == "":
        korm = None
    return korm


def input_data():
    ff = file_format()
    if ff == '1':
        res = m.new_contact_txt(v.input_data())
    if ff == '2':
        res = m.new_contact_csv(v.input_data())
    return v.info(res)


# Не удаляются строки в файлах, пайтон удаляет, но в файл заново не перезаписывает

def del_data():
    kk = file_format_delete()
    a = int(input('Введите какую строчку удалить: '))
    if kk == '1':
        with open('contact.txt', 'r') as file:
            lines = file.readlines()
        del lines[a - 1]
    if kk == '2':
        with open('contact.csv', 'r') as file:
            lines = file.readlines()
        del lines[a - 1]
    return v.info(lines)


def find_data():
    gg = file_format_find()
    if gg == '1':
        return v.info(m.find_personal_txt(v.find_people()))
    if gg == '2':
        return v.info(m.find_personal_csv(v.find_people()))
