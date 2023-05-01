from datetime import datetime as dt
import export

def get_type():
    type = int(input(
        "0 - Создать заметку\n" 
        "1 - Показать список заметок\n"
        "2 - Сортировка списка по номеру заметки\n"
        "3 - Сортировка списка по дате\n"
        "4 - Удалить заметку\n"
        "5 - Изменить заметку\n"
        "6 - Выход\n"
        "Выберите нужный вам параметр: "
    ))
    return type

def get_id():
    id = int(input("ID: "))
    return id

def get_header():
    header = input("Заголовок: ")
    return header

def get_importance():
    importance = input("Важность: ")
    return importance

def get_comment():
    comment = input("Комментарий: ")
    return comment

def get_dataNow():
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    return time

def get_dataChenge():
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    return time
