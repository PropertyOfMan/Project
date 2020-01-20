from Find_variable import find_var


# При наличии нескольких множителей переменной с одной степенью находим их общее значение
# Пренебрегаем скобками и прочим. Находим исключительно
def check_is_in_db(needed_tuple):
    # Если в уравнении более 2 переменных, то такого уравнения точно нет в БД
    if len(set(needed_tuple[1])) > 2:
        return 'ERROR'
    else:
        a_exp = 0
        b_exp = 0
        a = 0
        b = 0
        c = 0
        maxy = -999999999
        for _ in needed_tuple[1]:
            if _ > maxy:
                a_exp = _
                maxy = _
            else:
                b_exp = _

        for n, _ in enumerate(needed_tuple[1]):
            if _ == a_exp:
                a += needed_tuple[0][n]
            else:
                b += needed_tuple[0][n]
        return [a, b], [a_exp, b_exp], needed_tuple[2]


print(check_is_in_db(find_var('12{x}**2+13{x}-7{x}-6{x}+0+0+0', 'x')))
