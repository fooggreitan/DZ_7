# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id, имя, фамилию, номер телефона, комментрий - 
# символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

import view
import importieren
import export 

def start():

    if view.get_type() == 1:
        importieren.record()
    else:
        export.importierenn()

    # id = view.get_id()
    # name = view.get_name()
    # surname = view.get_surname()
    # number = view.get_number()
    # comment = view.get_comment()
    # with open("res.txt", 'w') as file:
    #     file.write(view.conclusion())
    # return view.conclusion()