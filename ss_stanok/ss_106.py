import math


def ss_106(k, dlina, visota, RAM):
    txt_ss = ''

    oBv = [27, 33, 15.0001, 22.3001, 21.2501, 32.2001, 21.2501, 34.0701, 27.5, 13.5401]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/106/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[0] = oBv[7]
        txt_ss = open('rs/106/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 133:
        shag = 15
        txt_ss = open('rs/106/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss