from datetime import datetime as dt

def get_type():
    type = int(input(
        "0 - C������ �������\n" 
        "1 - �������� ������ �������\n"
        "2 - ���������� �� ������\n"
        "3 - ���������� �� ����\n"
        "4 - ������� �������\n"
        "5 - �������� �������\n"
        "6 - �����\n"
        "������� ������������ ��� ��������: "
    ))
    return type

def get_id():
    id = int(input("ID: "))
    return id

def get_header():
    header = input("���������: ")
    return header

def get_importance():
    importance = input("��������: ")
    return importance

def get_comment():
    comment = input("�����������: ")
    return comment

def get_dataNow():
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    return time

def get_dataChenge():
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    return time
