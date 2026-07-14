oBv99ss = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 21.2051, 27.5, 10.6, 19]


def ss_99(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv99ss.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/99/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/99/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[7] - 5
        txt_ss = open('rs/99/per.txt', 'r').read()
        RAMX, RAMY, zazor = RAM[0], RAM[0], 95.6
        Lst = (int(dlina) - zazor - 10) / 3 + zazor
        Wst = (int(visota) - zazor - 5) / 2 + zazor
        zazx = Lst - (zazor - 5)
        zazy = Wst - (zazor - 5)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zazx', str(zazx))
        txt_ss = txt_ss.replace('zazy', str(zazy))
        txt_ss = txt_ss.replace('Lst', str(Lst))
        txt_ss = txt_ss.replace('Wst', str(Wst))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/99/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss
