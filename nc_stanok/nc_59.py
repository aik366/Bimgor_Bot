def nc_59(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 12, 6]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/59/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
        tx1 = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round(RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5, 3)
            g[i] = round(RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5, 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/59/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
        tx1 = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round(RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5, 3)
            g[i] = round(
                RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(dlina) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5, 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/59/st.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
        tx1 = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round(RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5, 3)
            g[i] = round(
                RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5, 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/59/xlst.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
        tx1 = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round(RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5, 3)
            g[i] = round(
                RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(dlina) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5, 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/59/ps.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
        RAMZ = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round((2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[i], 3)
            g[i] = round((2 * (rRr - (oBv[i] - 10)) - ((2 * (rRr - (oBv[i] - 10))) ** 2 -
                                                       (ty1 - (oBv[i] - 10)) ** 2 * 4) ** 0.5) / 2 + RAMZ + (oBv[i] - 10), 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/59/but.txt', 'r').read()
        RAMY = 29.5 if int(visota) >= 165 else 22.5
        RAMX, RAMK, oBv[2] = 80, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK
        h, g = [0] * 10, [0] * 10
        for i in range(10):
            h[i] = round((2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty0 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[i], 3)
            g[i] = round((2 * (rRr - (oBv[i]-10)) - ((2 * (rRr - (oBv[i]-10))) ** 2 -
                                                     (ty0 - (oBv[i]-10)) ** 2 * 4) ** 0.5) / 2 + RAMZ + (oBv[i]-10), 3)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))
            txt_ss = txt_ss.replace('g' + str(i), str(g[i]))

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/59/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK = 80, 22.5, 35.5
        RAMZ = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h0 = round((2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty1 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0], 3)

        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', str(h0))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/59/pssl2.txt', 'r').read()
        RAMX, RAMY, RAMK = 80, 22.5, 35.5
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/59/butsl1.txt', 'r').read()
        RAMY = 22.5
        RAMX, RAMK, oBv[2] = 80, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK
        h0 = round((2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty0 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0], 3)

        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', str(h0))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) < 130:
        txt_ss = open('rs/59/butsl2.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss