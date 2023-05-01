import csv

import view
from datetime import datetime

def sodtedDate():
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    notes = []
    for line in file:
      note_parts = line.split(";")
      note_dict = {
        "ID": note_parts[0],
        "Заголовок": note_parts[1],
        "Важность": note_parts[2],
        "Комментарий": note_parts[3],
        "Дата создания заметки": datetime.strptime(note_parts[4], '%d-%m-%Y %H:%M:%S'),
        "Дата изменения заметки": note_parts[5].split("\n")[0]
      }
      notes.append(note_dict)

    sorted_d= sorted(notes, key=lambda x: x["Дата создания заметки"])

  with open('res.csv', 'w', encoding="windows-1251") as can:
    for note in sorted_d:
      line = f"{note['ID']};" \
             f"{note['Заголовок']};" \
             f"{note['Важность']};" \
             f"{note['Комментарий']};" \
             f"{note['Дата создания заметки'].strftime('%d-%m-%Y %H:%M:%S')};" \
             f"{note['Дата изменения заметки']}\n"
      can.write(line)
  can.close()
  file.close()

def sortedID():
  sortedIDArray = []
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    [sortedIDArray.append(line.rstrip().strip(",")) for line in sorted(file)]

  with open('res.csv', 'w', encoding="windows-1251") as can:
    can.writelines('\n'.join(sortedIDArray))
  file.close()

def importierennNot():
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    for line in file:
      note_parts = line.split(";")
      note_dict = {
        "ID": note_parts[0],
        "Заголовок": note_parts[1],
        "Важность": note_parts[2],
        "Комментарий": note_parts[3],
        "Дата создания заметки": note_parts[4],
        "Дата изменения заметки": note_parts[5].split("\n")[0]
      }
      print(note_dict)
  file.close()
def delete_note():
  with open('res.csv', 'r+', encoding='windows-1251') as file:
    lines = file.readlines()

  numberID = int(input("Введите номер строки заметки для удаления: "))

  with open('res.csv', 'w', encoding='windows-1251') as file:
    for i, line in enumerate(lines):
      if not str(numberID) in line.split(';'):
        file.write(line)
  file.close()

def changelist():

  list = {}

  with open('res.csv', 'r+', encoding="windows-1251") as file:

    for line in file:
      note_parts = line.split(";")
      note_dict = {
        "ID": note_parts[0],
        "Заголовок": note_parts[1],
        "Важность": note_parts[2],
        "Комментарий": note_parts[3],
        "Дата создания заметки": note_parts[4],
        "Дата изменения заметки": note_parts[5].split("\n")[0]
      }
      list[note_parts[0].split(".")[0]] = note_dict

  cad = input("Введите номер строки заметки для имзенения: ")
  print(list[cad])
  caq = input("Введите параметр для изменения: ")
  list[cad][caq] = input("Введите изменение: ")

  with open('res.csv', 'w', encoding="windows-1251") as file:
    for key, value in list.items():
      if key == cad:
        line = f"{key};" \
               f"{value['Заголовок']};" \
               f"{value['Важность']};" \
               f"{value['Комментарий']};" \
               f"{value['Дата создания заметки']};" \
               f"{view.get_dataChenge()}\n"
      else:
        line = f"{key};" \
               f"{value['Заголовок']};" \
               f"{value['Важность']};" \
               f"{value['Комментарий']};" \
               f"{value['Дата создания заметки']};" \
               f"{value['Дата изменения заметки']}\n"

      file.write(line)

  file.close()
