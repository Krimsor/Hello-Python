def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Добавить контакт в базу данных")
    print("2. Удалить контакт из базы данных")
    print("3. Найти контакт")
    print("4. Закончить работу с базой данных")
    return int(input("Введите номер необходимого действия: "))

def find_people():
    return input('Find? ')

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    post_number = input("Введите должность: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, post_number]

def info(message):
    print(message)