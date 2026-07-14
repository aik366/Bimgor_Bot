def nc_95(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 12, 6]
    h, g = [0] * 10, [0] * 10

    if k[7] == 'Фасад' and int(visota) >= 280:
        txt_ss = open('rs/95/f.txt', 'r').read()
        Txt_38 = open('rs/95/38.txt', 'r').read()
        Txt_39 = open('rs/95/39.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60
        ty1 = (int(visota) - 2 * 103 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)

        CP = (k + 1) * 4 - 1

        tx1 = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        m2 = 33
        for i in range(k + 1):
            RUM1 = RAMY + rRr1 + 27 - (rRr1 ** 2 - m2 ** 2) ** 0.5
            RYM1 = RAMY + rRr1 + 27 - (rRr1 ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace('\TTTTT\\', Txt_38)
            txt_ss = txt_ss.replace('RUM1', f'{RUM1:.3f}')
            txt_ss = txt_ss.replace('RYM1', f'{RYM1:.3f}')
            RUM2 = RAMY + rRr1 + 27 - (rRr1 ** 2 - m2 ** 2) ** 0.5
            RYM2 = RAMY + rRr1 + 27 - (rRr1 ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace('\HHHHH\\', Txt_39)
            txt_ss = txt_ss.replace('RUM2', f'{RUM2:.3f}')
            txt_ss = txt_ss.replace('RYM2', f'{RYM2:.3f}')
            m2 = m2 + 60

        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('j1', str(int(visota) / 2 + RAM / 2 - 3))
        txt_ss = txt_ss.replace('j2', str(int(visota) / 2 - RAM / 2 + 3))
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'Фасад' and 230 <= int(visota) < 280:
        txt_ss = open('rs/95/f2.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60

        tx1 = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/95/xl.txt', 'r').read()
        Txt_38 = open('rs/95/38_xl.txt', 'r').read()
        Txt_39 = open('rs/95/39_xl.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60
        ty1 = (int(dlina) - 2 * 103 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)

        CP = (k + 1) * 4 - 1

        tx1 = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(dlina) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        m2 = 33
        for i in range(k + 1):
            RUM1 = RAMY + rRr1 + 27 - (rRr1 ** 2 - m2 ** 2) ** 0.5
            RYM1 = RAMY + rRr1 + 27 - (rRr1 ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace('\TTTTT\\', Txt_38)
            txt_ss = txt_ss.replace('RUM1', f'{RUM1:.3f}')
            txt_ss = txt_ss.replace('RYM1', f'{RYM1:.3f}')
            RUM2 = RAMY + rRr1 + 27 - (rRr1 ** 2 - m2 ** 2) ** 0.5
            RYM2 = RAMY + rRr1 + 27 - (rRr1 ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace('\HHHHH\\', Txt_39)
            txt_ss = txt_ss.replace('RUM2', f'{RUM2:.3f}')
            txt_ss = txt_ss.replace('RYM2', f'{RYM2:.3f}')
            m2 = m2 + 60

        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('j1', str(int(dlina) / 2 + RAM / 2 - 3))
        txt_ss = txt_ss.replace('j2', str(int(dlina) / 2 - RAM / 2 + 3))
        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/95/st.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY = 96, 44.5
        tx1 = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/95/xlst.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY = 96, 44.5

        tx1 = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMY + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMY + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(dlina) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/95/ps.txt', 'r').read()
        Txt_38 = open('rs/72/38_xl.txt', 'r').read()
        RAMX, RAMY, RAMK, RAM = 61, 22.5, 26, 60
        RAMZ = RAMX - RAMK

        ty1 = (int(dlina) - 2 * 89 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)
        CY = ty1 - k * RAM

        for x in range(2 * k + 2):
            txt_ss = txt_ss.replace('\TTTTT', Txt_38)

        CP = 2 * (k + 1) * 4 - 1

        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        for i in range(10):
            h[i] = (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[i]
            g[i] = (2 * (rRr - (oBv[i] - 10)) - ((2 * (rRr - (oBv[i] - 10))) ** 2 -
                                                       (ty1 - (oBv[i] - 10)) ** 2 * 4) ** 0.5) / 2 + RAMZ + (oBv[i] - 10)
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        txt_ss = txt_ss.replace('CY', str(CY))
        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/95/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 26
        RAMZ = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h0 = (2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty1 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0]

        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', f'{h0:.3f}')
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/95/pssl2.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 26
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/95/but.txt', 'r').read()
        RAMY = 29.5 if int(visota) >= 165 else 22.5
        RAMX, RAMK = 80, 35.5

        tx1 = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)

        for i in range(10):
            h[i] = RAMK + rRr1 - ((rRr1 - oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5
            g[i] = RAMK + rRr1 - ((rRr1 - (oBv[i] - 10)) ** 2 - (int(visota) / 2 - RAMY - (oBv[i] - 10)) ** 2) ** 0.5
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace('g' + str(i), f'{g[i]:.3f}')

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/95/butsl1.txt', 'r').read()
        RAMY = 22.5
        RAMX, RAMK, oBv[2] = 80, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK
        h0 = (2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty0 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0]

        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', f'{h0:.3f}')
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) < 130:
        txt_ss = open('rs/95/butsl2.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK

        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss
