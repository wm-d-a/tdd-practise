# Задача: Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.

def func(inp):
    c = 0
    max_c = 0
    for i in range(len(inp)):
        if inp[i] == '0':
            c += 1
        else:
            if c > max_c:
                max_c = c
            c = 0
    if c > max_c:
        max_c = c
    return max_c
