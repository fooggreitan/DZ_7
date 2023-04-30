import view
def sodtedDate():
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    c = []
    for line in file:
      note_parts = line.split("  ")
      note_dict = {
        "ID": note_parts[0].split(".")[0],
        "Заголовок": note_parts[1].split(";")[0],
        "Важность": note_parts[2].split(": ")[1].split(";")[0],
        "Комментарий": note_parts[3].split(": ")[1].split(";")[0],
        "Дата создания заметки": note_parts[4].split(": ")[1],
        "Дата изменения заметки": note_parts[5].split(": ")[1].split(".\n")[0]
      }
      c.append(note_dict)
  file.close()

  sorted_c = sorted(c, key=lambda x: x["Дата создания заметки"])

  with open('res.csv', 'w', encoding="windows-1251") as can:
    for note in sorted_c:
      line = f"{note['ID']}.  " \
             f"{note['Заголовок']};  " \
             f"Важность: {note['Важность']};  " \
             f"Комментарий: {note['Комментарий']};  " \
             f"Дата создания заметки: {note['Дата создания заметки']}  " \
             f"Дата изменения заметки: {note['Дата изменения заметки']}.\n"
      can.write(line)
  file.close()

def sortedID():
  c = []
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    [c.append(line.rstrip().strip(",")) for line in sorted(file)]
  file.close()

  with open('res.csv', 'w', encoding="windows-1251") as can:
    can.writelines('\n'.join(c))
  file.close()

def importierennNot():
  with open('res.csv', 'r+', encoding="windows-1251") as file:
    for line in file:
      note_parts = line.split("  ")
      note_dict = {
        "ID": note_parts[0].split(".")[0],
        "Заголовок": note_parts[1].split(";")[0],
        "Важность": note_parts[2].split(": ")[1].split(";")[0],
        "Комментарий": note_parts[3].split(": ")[1].split(";")[0],
        "Дата создания заметки": note_parts[4].split(": ")[1],
        "Дата изменения заметки": note_parts[5].split(": ")[1].split(".\n")[0].split(".")[0]
      }
      print(note_dict)
  file.close()
def delete_note():
  with open('res.csv', 'r+', encoding='windows-1251') as file:
    lines = file.readlines()
  file.close()

  numberID = int(input("Введите номер строки заметки, которую нужно удалить: "))

  with open('res.csv', 'w', encoding='windows-1251') as file:
    for i, line in enumerate(lines):
      if not str(numberID) in line.split('.'):
        file.write(line)
  file.close()

def changelist():

  list = {}

  with open('res.csv', 'r+', encoding="windows-1251") as file:

    for line in file:
      note_parts = line.split("  ")
      note_dict = {
        "ID": note_parts[0].split(".")[0],
        "Заголовок": note_parts[1].split(";")[0],
        "Важность": note_parts[2].split(": ")[1].split(";")[0],
        "Комментарий": note_parts[3].split(": ")[1].split(";")[0],
        "Дата создания заметки": note_parts[4].split(": ")[1],
        "Дата изменения заметки": note_parts[5].split(": ")[1].split(".\n")[0].split(".")[0]
      }
      list[note_parts[0].split(".")[0]] = note_dict
  file.close()

  cad = input("Введите номер строки заметки: ")
  print(list[cad])
  caq = input("Выберите параметр который хотите изменить: ")
  list[cad][caq] = input("Выберите изменение: ")

  with open('res.csv', 'w', encoding="windows-1251") as file:
    for key, value in list.items():
      if key == cad:
        line = f"{key}.  {value['Заголовок']};  " \
               f"Важность: {value['Важность']};  " \
               f"Комментарий: {value['Комментарий']};  " \
               f"Дата создания заметки: {value['Дата создания заметки']}  " \
               f"Дата изменения заметки: {view.get_dataChenge()}.\n"
      else:
        line = f"{key}.  {value['Заголовок']};  " \
               f"Важность: {value['Важность']};  " \
               f"Комментарий: {value['Комментарий']};  " \
               f"Дата создания заметки: {value['Дата создания заметки']}  " \
               f"Дата изменения заметки:: {value['Дата изменения заметки']}.\n"
        file.write(line)
  file.close()

