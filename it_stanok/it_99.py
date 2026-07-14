oBv99it = [27, 33, 21.901, 23.301, 22.301, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]


def it_99(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv99it.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/99_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/99_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 50.5 + (RAM[0] - 44.5)
        lyp = int(dlina) - lxp + zaz
        dx1 = lxp - zaz

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', str(lxp))
        txt_ss = txt_ss.replace('lyp', str(lyp))
        txt_ss = txt_ss.replace('dx1', str(dx1))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/99_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[8] - 5
        txt_ss = open('rs/99_it/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 98.6 - 10) / 3 + 98.6
        lyp = (int(visota) - 98.6 - 5) / 2 + 98.6
        dx1 = lxp - 93.6
        dx2 = (lxp - 93.6) * 2
        dy1 = lyp - 93.6

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        oBv[1] = oBv[8] - 5
        txt_ss = open('rs/99_it/per4.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 98.6 - 5) / 2 + 98.6
        lyp = (int(visota) - 98.6 - 5) / 2 + 98.6
        dx1 = lxp - 93.6
        dx2 = lxp - 93.6
        dy1 = lyp - 93.6

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[8] - 5
        txt_ss = open('rs/99_it/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 98.6 - 15) / 4 + 98.6
        lyp = (int(visota) - 98.6 - 5) / 2 + 98.6
        dx1 = lxp - 93.6
        dx2 = (lxp - 93.6) * 2
        dx3 = (lxp - 93.6) * 3
        dy1 = lyp - 93.6

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dx3', f'{dx3:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/99_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Планка':
        txt_ss = open('rs/99_it/pl.txt', 'r').read()

    return txt_ss
