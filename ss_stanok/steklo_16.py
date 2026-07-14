def steklo16(k, dlina, visota, RAM):
    txt_ss = ''
    RAM[0] = 64 if RAM[0] == 44.5 else RAM[0]
    if k[5] == '15':
        txt_ss = open('rs/16/st15.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', str(RAM[0]))
        if int(dlina) < 450:
            txt_ss = txt_ss.replace('@200', str(int(dlina)-155))
            txt_ss = txt_ss.replace('@235', str(int(dlina) - 140))

    elif k[5] == '12' or k[5] == '11':
        txt_ss = open('rs/16/st12.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', str(RAM[0] + 6))
        if int(dlina) < 450:
            txt_ss = txt_ss.replace('@200', str(int(dlina) - 155))
            txt_ss = txt_ss.replace('@235', str(int(dlina) - 140))

    elif k[5] == '14' or k[5] == '13':
        txt_ss = open('rs/16/st14.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', str(RAM[0] + 5.2))
        if int(dlina) < 450:
            txt_ss = txt_ss.replace('@200', str(int(dlina) - 155))
            txt_ss = txt_ss.replace('@235', str(int(dlina) - 140))

    elif k[5] in ('16', '17', '18', '19', '20'):
        txt_ss = open('rs/16/st17.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', str(RAM[0]))
        if int(dlina) < 450:
            txt_ss = txt_ss.replace('@200', str(int(dlina) - 155))
            txt_ss = txt_ss.replace('@235', str(int(dlina) - 140))


    return txt_ss
