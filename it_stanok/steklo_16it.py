def steklo16it(k, dlina, visota, RAM):
    txt_it = ''
    RAM[0] = 64 if RAM[0] == 44.5 else RAM[0]
    if k[5] == '12' or k[5] == '11':
        txt_it = open('rs/16_it/st12.txt', 'r').read()
        txt_it = txt_it.replace('RAMX', str(RAM[0] + 6))

    elif k[5] == "15":
        txt_it = open('rs/16_it/st15.txt', 'r').read()
        txt_it = txt_it.replace('RAMX', str(RAM[0]))

    elif k[5] in ('13', '14'):
        txt_it = open('rs/16_it/st14.txt', 'r').read()
        txt_it = txt_it.replace('RAMX', str(RAM[0]))

    elif k[5] in ('16', '17', '18', '19', '20'):
        txt_it = open('rs/16_it/st17.txt', 'r').read()
        txt_it = txt_it.replace('RAMX', str(RAM[0]))

    return txt_it