def new_contact_csv(card):
    last_name, first_name, middle_name, brith_name, phone_number, post_number = card
    with open('contact.csv', 'a') as data:
        member = f'Lastname: {last_name}; Name: {first_name}; Surname: {middle_name}; Birthday: {brith_name}; Number phone: {phone_number}; Post number: {post_number}\n'
        data.write(member)
    return 'New contact was create'

def new_contact_txt(card):
    last_name, first_name, middle_name, brith_name, phone_number, post_number = card
    with open('contact.txt', 'a') as data:
        member = f'Lastname: {last_name}; Name: {first_name}; Surname: {middle_name}; Birthday: {brith_name}; Number phone: {phone_number}; Post number: {post_number}\n'
        data.write(member)
    return 'New contact was create'

# Первый элемент списка находится в любом файле. Последующие - нет

def find_personal_csv(key):
    with open('contact.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                last_name, first_name, middle_name, brith_name, phone_number, post_number = i.split(';')
                return f'Contact found: {last_name} {first_name} {middle_name} {brith_name} {phone_number} {post_number}\n'
            else:
                return 'Contact not found'

def find_personal_txt(key):
    with open('contact.txt', 'r') as file:
        data = file.readline().split('\n')
        for i in data:
            if i.count(key):
                last_name, first_name, middle_name, brith_name, phone_number, post_number = i.split(';')
                return f'Contact found: {last_name} {first_name} {middle_name} {brith_name} {phone_number} {post_number}\n'
            else:
                return 'Contact not found'

