# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий - 
# символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

def get_type():
    type = int(input(
        "1 - ипортировать файл\n"
        "0 - экспортировать файл\n"
    ))
    return type

def get_id():
    id = int(input("id: "))
    return id

def get_name():
    name = input("name: ")
    return name

def get_surname():
    surname = input("surname: ")
    return surname

def get_number():
    number = int(input("number: "))
    return number

def get_comment():
    comment = input("comment: ")
    return comment
