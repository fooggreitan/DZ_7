def importierenn():
  c = []
  with open('res.txt', 'r', encoding="UTF-8") as file:
    [c.append(line.rstrip().strip(",")) for line in sorted(file)]

  with open('res.txt', 'w', encoding="UTF-8") as can:
    can.writelines('\n'.join(c))


def importierennNot():
  with open('res.txt', 'r', encoding="UTF-8") as file:
    [print(line, end="") for line in file]
    file.close()

def importierennNoet():
  with open('res.txt', 'r+', encoding="UTF-8") as file:
      for line in file.readlines():
        res = line.split(",")
        print(f"{res[1]}, {res[2]}")
