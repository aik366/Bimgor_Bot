from it_stanok import it_51

def it_66(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 62, 23.301, 21.401, 14.101, 12.201, 27.5, 47, 12]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if (k[7] in ('Фасад', 'Хлеб') and int(visota) < 280) or \
            (k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 160) or \
            k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_51(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 280:
        txt_ss = open('rs/66_it/f.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[0], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб' and int(visota) >= 280:
        txt_ss = open('rs/66_it/xl.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 160:
        oBv[8] = 36
        txt_ss = open('rs/66_it/ps.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[1], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 160:
        oBv[8] = 36
        txt_ss = open('rs/66_it/but.txt', 'r').read()
        RAMX, RAMY, rRr1 = RAM[0], RAM[1], 51
        h1 = RAMY + oBv[8] + (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)


    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss