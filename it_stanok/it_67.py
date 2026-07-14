from it_stanok import it_51


def it_67(k, dlina, visota, RAM):
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_51(k, dlina, visota, RAM)
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 47, 10.4, 1.4]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/67_it/f.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 33
        h1 = int(visota) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[9]) ** 2) ** 0.5
        RAM1, RAM2, RAM3, RAM4 = h1, h1, h1, h1

        if int(visota) < 272:
            h2 = RAMX + oBv[9] + (rRr1 ** 2 - (int(visota) / 2 - (RAMY + oBv[2])) ** 2) ** 0.5
            RAM1, RAM2, RAM3, RAM4 = 0.001, RAMY + oBv[2], 0.001, RAMY + oBv[2]
            txt_ss = txt_ss.replace('RAMX+OBV2', str(round(h2, 3)))
            txt_ss = txt_ss.replace('lpy-(RAMY+OBV2)', str(int(visota) - RAM2 + 0.001))
            txt_ss = txt_ss.replace('(RAMY+OBV2)', str(RAM4 + 0.001))
            txt_ss = txt_ss.replace('RAM1', str(RAMY + oBv[2] + round(RAM1, 3)))
            txt_ss = txt_ss.replace('lpy-RAM3', str(int(visota) - RAM2 + 0.001 + round(RAM3, 3)))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM1', str(round(RAM1, 3)))
        txt_ss = txt_ss.replace('RAM2', str(round(RAM2, 3)))
        txt_ss = txt_ss.replace('RAM3', str(round(RAM3, 3)))
        txt_ss = txt_ss.replace('RAM4', str(round(RAM4, 3)))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/67_it/xl.txt', 'r').read()
        RAMX, RAMY, rRr1 = 44.5, 44.5, 33
        h1 = int(dlina) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[9]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/67_it/st.txt', 'r').read()
        oBv[9], oBv[1] = 20, 27.5
        RAMX, RAMY, rRr1, h = 44.5, 44.5, 19.1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        h4_2 = int(visota) / 2 - ((rRr1 + oBv[4] - 10) ** 2 - (oBv[4] - 10) ** 2) ** 0.5
        h6_2 = int(visota) / 2 - ((rRr1 + oBv[6] - 10) ** 2 - (oBv[6] - 10) ** 2) ** 0.5
        txt_ss = txt_ss.replace('h4_2', str(round(h4_2, 3)))
        txt_ss = txt_ss.replace('h6_2', str(round(h6_2, 3)))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            h[i] = int(visota) / 2 - ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            txt_ss = txt_ss.replace('h' + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/67_it/xlst.txt', 'r').read()
        oBv[9], oBv[1] = 20, 27.5
        RAMX, RAMY, rRr1, h = 44.5, 44.5, 19.1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        h4_2 = int(dlina) / 2 - ((rRr1 + oBv[4] - 10) ** 2 - (oBv[4] - 10) ** 2) ** 0.5
        h6_2 = int(dlina) / 2 - ((rRr1 + oBv[6] - 10) ** 2 - (oBv[6] - 10) ** 2) ** 0.5
        txt_ss = txt_ss.replace('h4_2', str(round(h4_2, 3)))
        txt_ss = txt_ss.replace('h6_2', str(round(h6_2, 3)))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            h[i] = int(dlina) / 2 - ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            txt_ss = txt_ss.replace('h' + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 196:
        txt_ss = open('rs/67_it/but.txt', 'r').read()
        oBv[9] = 36
        RAMX, RAMY, rRr1 = 44.5, 29.5, 33
        h1 = int(visota) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[9]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 160:
        txt_ss = open('rs/67_it/ps.txt', 'r').read()
        oBv[9] = 36
        RAMX, RAMY, rRr1 = 44.5, 22.5, 33
        h1 = int(dlina) / 2 - (rRr1 ** 2 - (oBv[2] - oBv[9]) ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146 and int(visota) < 160:
        txt_ss = open('rs/51_it/ps.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 160:
            RAMY = 22.5
        else:
            RAMY = 26.5
        RAMX = 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 146  and int(visota) < 196:
        txt_ss = open('rs/51_it/but.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 170:
            RAMY = 22.5
        else:
            RAMY = 26.5
        RAMX = 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51_it/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51_it/butsl.txt', 'r').read()
        RAMX, RAMY = 44.5, 29.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/51_it/pssl2.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss