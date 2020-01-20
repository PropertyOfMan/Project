# Находим множители переменных и их степени
def find_var(string, letter):
    lst = []
    exponent = []
    need = 0
    flag = False
    flag_c = False
    for n, _ in enumerate(string):
        try:
            if _.isdigit() and _ != '0' and \
                    not string[n + 1].isdigit() and string[n + 1] != '{' and string[n - 2:n] != '**':
                flag_c = True
        except IndexError:
            flag_c = True
        # Находим переменные в строке
        if _ == letter:
            # Находим множитель переменной
            if string[n - 2].isdigit():
                for i in range(0, n)[::-1]:
                    if string[i].isdigit():
                        flag = True
                    if flag and string[i].isdigit() and string[i + 1].isdigit():
                        continue
                    if flag and not string[i].isdigit():
                        if string[i - 1] == '-':
                            need = i - 1
                        else:
                            need = i
                        break
                flag = False
                # Если переменная находится в начале строки, то need присваивается 0, чтобы не было ошибок
                lst.append(int(string[need if need != 0 else 0:n - 1]))
            else:
                # Если перменная не имеет множителя, то он равен 1
                lst.append('1')
                # Находим степени переменной
            if string[n + 2: n + 4] == '**':
                for i in range(n, len(string) - 1):
                    if string[i].isdigit():
                        flag = True
                    if flag and string[i].isdigit() and string[i + 1].isdigit():
                        continue
                    if flag and not string[i].isdigit():
                        need = i
                        break
                flag = False
                # Костыль :)
                try:
                    exponent.append(int(string[n + 4:need]))
                except ValueError:
                    exponent.append(int(string[n + 4:]))
            else:
                exponent.append(1)
    return lst, exponent, flag_c
