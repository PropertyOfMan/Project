import string


# Приводим строку к виду, читаемому командой eval()
def parse(n_string):
    # Парс строки к читаемому программой виду
    n_string = n_string.strip()
    n_string = ''.join([_ for _ in n_string if _ in ['*', '^', '/', '-', '+', '(', ')', '.']
                        or _ in string.digits]).replace('^', '**')
    x = ''.join(n_string)
    # Проверяем, что строку можно "решить" командой eval(), иначе возвращаем ERROR
    try:
        eval(x)
        return x
    except SyntaxError:
        return 'ERROR'
