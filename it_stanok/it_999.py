def it_999(k, dlina, visota, RAM):
    txt_ss = ''
    oBv4 = -31.5

    if k[7] in ('Фасад', 'Хлеб', 'ПСЯ', 'Бутыл.'):
        txt_ss = open('rs/999_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('OBV4', str(oBv4))

    return txt_ss
