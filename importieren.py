import view

def record():

    res = ''
    res += '{}.  '.format(view.get_id())
    res += '{};  '.format(view.get_header())
    res += '��������: {};  '.format(view.get_importance())
    res += '�����������: {};  '.format(view.get_comment())
    res += '���� �������� �������: {};  '.format(view.get_dataNow())
    res += '���� ��������� �������: �����.'
    res += ''

    with open("res.csv", 'a') as file:
        file.write(f'{res}\n')
    file.close()

    return res