import view

def record():

    res = ''
    res += '{}.  '.format(view.get_id())
    res += '{};  '.format(view.get_header())
    res += 'Важность: {};  '.format(view.get_importance())
    res += 'Комментарий: {};  '.format(view.get_comment())
    res += 'Дата создания заметки: {};  '.format(view.get_dataNow())
    res += 'Дата изменения заметки: пусто.'
    res += ''

    with open("res.csv", 'a') as file:
        file.write(f'{res}\n')
    file.close()

    return res