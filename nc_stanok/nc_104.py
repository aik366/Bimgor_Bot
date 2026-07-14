import math


def nc_104(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 37, 63.5, 13, 22.3001, -6, 20.4051, 27.5, 20.9001, 21.4]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/104/f.txt', 'r').read()
        RAMX, RAMY= 44.5, 44.5
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/104/st.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[7] - 5
        txt_ss = open('rs/104/per.txt', 'r').read()
        RAMX, RAMY, zazor = 44.5, 44.5, 95.6
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

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146 and int(visota) < 170:
        txt_ss = open('rs/104/pssl.txt', 'r').read()
        RAMX, RAMY, oBv[5] = 44.5, 26.5, 2
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 170:
        txt_ss = open('rs/104/ps.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss