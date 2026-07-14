from ss_stanok import ss_51

def ss_66(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 62, 13.6, 22.21, 12.2001, 20.7501, 27.5, 47, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if (k[7] in ('Фасад', 'Хлеб') and int(visota) < 280) or \
            (k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 160) or \
            k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return ss_51(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 280:
        txt_ss = open('rs/66/f.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[0], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб' and int(visota) >= 280:
        txt_ss = open('rs/66/xl.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 160:
        oBv[8] = 36
        txt_ss = open('rs/66/ps.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[1], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 160:
        oBv[8] = 36
        txt_ss = open('rs/66/but.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[1], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)


    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss