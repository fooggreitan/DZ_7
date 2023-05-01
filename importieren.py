import view

def record():

    res = ''
    res += '{};'.format(view.get_id())
    res += '{};'.format(view.get_header())
    res += '{};'.format(view.get_importance())
    res += '{};'.format(view.get_comment())
    res += '{};'.format(view.get_dataNow())
    res += 'не изменялось'

    with open("res.csv", 'a') as file:
        file.write(f'{res}')
    file.close()

    return res