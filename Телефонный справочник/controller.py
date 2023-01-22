from import_data import import_data_csv
from import_data import import_data_txt


def greeting():
    print("Добро пожаловать в телефонный справочник!")


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number]


def file_format():
    form = input('Введите цифру формата: "txt" = 1 или "csv" = 2: ')
    if form == "":
        form = None
    return form


def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep


def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        ff = file_format()
        if ff == '1':
            import_data_txt(input_data(), sep)
        if ff == '2':
            import_data_csv(input_data(), sep)
