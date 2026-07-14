from nc_stanok import nc_51


def nc_67(k, dlina, visota, RAM):
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return nc_51(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 62, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 47, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/67/f.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 33
        h1 = int(visota) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5
        RAM1, RAM2, RAM3, RAM4 = h1, h1, h1, h1

        if int(visota) < 272:
            h2 = RAMX + oBv[8] + (rRr1 ** 2 - (int(visota) / 2 - (RAMY + oBv[2])) ** 2) ** 0.5
            RAM2, RAM4 = RAMY + oBv[2], RAMY + oBv[2]
            txt_ss = txt_ss.replace('RAMX+oBv2', str(round(h2, 3)))
            txt_ss = txt_ss.replace('w-(RAMY+oBv2)', '@0.001')
            txt_ss = txt_ss.replace('(RAMY+oBv2)', '@0.001')
            txt_ss = txt_ss.replace('RAM1', '@0.001')
            txt_ss = txt_ss.replace('w-RAM3', '@0.001')

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM1', str(round(RAM1, 3)))
        txt_ss = txt_ss.replace('RAM2', str(round(RAM2, 3)))
        txt_ss = txt_ss.replace('RAM3', str(round(RAM3, 3)))
        txt_ss = txt_ss.replace('RAM4', str(round(RAM4, 3)))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/67/xl.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 33
        h1 = int(dlina) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/67/st.txt', 'r').read()
        oBv[8] = 20
        RAMX, RAMY, rRr1, h = 44.5, 44.5, 19.1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        h4_2 = int(visota) / 2 - ((rRr1 + oBv[4] - 10) ** 2 - (oBv[4] - 10) ** 2) ** 0.5
        h6_2 = int(visota) / 2 - ((rRr1 + oBv[6] - 10) ** 2 - (oBv[6] - 10) ** 2) ** 0.5
        txt_ss = txt_ss.replace('h4_2', str(round(h4_2, 3)))
        txt_ss = txt_ss.replace('h6_2', str(round(h6_2, 3)))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            h[i] = int(visota) / 2 - ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            txt_ss = txt_ss.replace('h' + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/67/xlst.txt', 'r').read()
        oBv[8] = 20
        RAMX, RAMY, rRr1, h = 44.5, 44.5, 19.1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        h4_2 = int(dlina) / 2 - ((rRr1 + oBv[4] - 10) ** 2 - (oBv[4] - 10) ** 2) ** 0.5
        h6_2 = int(dlina) / 2 - ((rRr1 + oBv[6] - 10) ** 2 - (oBv[6] - 10) ** 2) ** 0.5
        txt_ss = txt_ss.replace('h4_2', str(round(h4_2, 3)))
        txt_ss = txt_ss.replace('h6_2', str(round(h6_2, 3)))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            h[i] = int(dlina) / 2 - ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            txt_ss = txt_ss.replace('h' + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 196:
        txt_ss = open('rs/67/but.txt', 'r').read()
        oBv[8] = 36
        RAMX, RAMY, rRr1 = 44.5, 29.5, 33
        h1 = int(visota) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 160:
        txt_ss = open('rs/67/ps.txt', 'r').read()
        oBv[8] = 36
        RAMX, RAMY, rRr1 = 44.5, 22.5, 33
        h1 = int(dlina) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[8]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146 and int(visota) < 160:
        txt_ss = open('rs/51/ps.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 160:
            RAMY = 22.5
        else:
            RAMY = 26.5
        RAMX = 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 146  and int(visota) < 196:
        txt_ss = open('rs/51/but.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 170:
            RAMY = 22.5
        else:
            RAMY = 26.5
        RAMX = 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/butsl.txt', 'r').read()
        RAMX, RAMY = 44.5, 29.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/51/pssl2.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss