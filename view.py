def get_type():
    type = int(input(
        "\n0 - ипортировать файл\n" 
        "1 - экспортировать файл\n"
        "2 - экспортировать cортированный файл\n"
        "3 - экспортировать cортированный файл по имени\n"
        "4 - выход\n"
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