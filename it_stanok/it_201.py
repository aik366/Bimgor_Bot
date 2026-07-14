def it_201(k, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        zaz = 5 if RAM[1] == 22.5 else RAM[1]
        f_2 = 'f2' if RAM[3] else 'f'
        txt_ss = open(f'rs/201_it/{f_2}.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('ZAZ', str(zaz))

    return txt_ss