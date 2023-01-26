import view

def record():

    res = ''
    res += '{}, '.format(view.get_id())
    res += '{}, '.format(view.get_name())
    res += '{}, '.format(view.get_surname())
    res += '{}, '.format(view.get_number())
    res += '{}'.format(view.get_comment())
    res += ''

    with open("res.txt", 'a') as file:
        file.write(f'{res}\n')

    return res