def it_95(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 0, 0]
    oBv[10], oBv[11] = round(oBv[4] - 10, 3), round(oBv[6] - 10, 3)

    if k[7] == 'Фасад' and int(visota) >= 280:
        txt_ss = open('rs/95_it/f.txt', 'r').read()
        Txt_38 = open('rs/95_it/38.txt', 'r').read()
        Txt_39 = open('rs/95_it/39.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60
        RAMK = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMY + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        ty2 = (int(visota) - 2 * 97 - 26) / 2 - RAM / 2
        key = int(ty2 / RAM)
        m2 = 33
        j1 = int(visota) / 2 + RAM / 2 - 3
        j2 = int(visota) / 2 - RAM / 2 + 3
        for x in range(key + 1):
            RUM1 = RAMY + rRr + 27 - (rRr ** 2 - m2 ** 2) ** 0.5
            RYM1 = RAMY + rRr + 27 - (rRr ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace("RUM1", str(round(RUM1, 3)))
            txt_ss = txt_ss.replace("RYM1", str(round(RYM1, 3)))
            RUM2 = RAMY + rRr + 27 - (rRr ** 2 - m2 ** 2) ** 0.5
            RYM2 = RAMY + rRr + 27 - (rRr ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace("' HHHHH", Txt_39)
            txt_ss = txt_ss.replace("RUM2", str(round(RUM2, 3)))
            txt_ss = txt_ss.replace("RYM2", str(round(RYM2, 3)))

            txt_ss = txt_ss.replace("j1", str(j1))
            txt_ss = txt_ss.replace("j2", str(j2))
            j1 += RAM
            j2 -= RAM
            m2 += RAM
        txt_ss = txt_ss.replace("@ LINE_EP, 0 : " + f'{RYM1:.3f}', "' LINE_EP, 0 : " + f'{RYM1:.3f}')

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'Фасад' and 230 <= int(visota) < 280:
        txt_ss = open('rs/95_it/f2.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60
        RAMK = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMY + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/95_it/xl.txt', 'r').read()
        Txt_38 = open('rs/95_it/38_xl.txt', 'r').read()
        Txt_39 = open('rs/95_it/39_xl.txt', 'r').read()
        RAMX, RAMY, RAM = 96, 44.5, 60
        RAMK = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMY + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        ty2 = (int(dlina) - 2 * 97 - 26) / 2 - RAM / 2
        key = int(ty2 / RAM)
        m2 = 33
        j1 = int(dlina) / 2 + RAM / 2 - 3
        j2 = int(dlina) / 2 - RAM / 2 + 3
        for x in range(key + 1):
            RUM1 = RAMY + rRr + 27 - (rRr ** 2 - m2 ** 2) ** 0.5
            RYM1 = RAMY + rRr + 27 - (rRr ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace("RUM1", str(round(RUM1, 3)))
            txt_ss = txt_ss.replace("RYM1", str(round(RYM1, 3)))
            RUM2 = RAMY + rRr + 27 - (rRr ** 2 - m2 ** 2) ** 0.5
            RYM2 = RAMY + rRr + 27 - (rRr ** 2 - (m2 + 54) ** 2) ** 0.5
            txt_ss = txt_ss.replace("' HHHHH", Txt_39)
            txt_ss = txt_ss.replace("RUM2", str(round(RUM2, 3)))
            txt_ss = txt_ss.replace("RYM2", str(round(RYM2, 3)))

            txt_ss = txt_ss.replace("j1", f'{j1}')
            txt_ss = txt_ss.replace("j2", f'{j2}')
            j1 += RAM
            j2 -= RAM
            m2 += RAM

        txt_ss = txt_ss.replace("@ LINE_EP, 0 : " + f'{j1 - RAM}+RAM', "' LINE_EP, 0 : " + f'{j1 - RAM}+RAM')
        txt_ss = txt_ss.replace("@ LINE_EP, 0 : " + f'{j2 + RAM}-RAM', "' LINE_EP, 0 : " + f'{j1 - RAM}-RAM')

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/95_it/st.txt', 'r').read()
        oBv[1] = oBv[8]
        RAMX, RAMY = 96, 44.5
        RAMK = RAMX - RAMY
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMY + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/95_it/xl_st.txt', 'r').read()
        oBv[1] = oBv[8]
        RAMX, RAMY = 96, 44.5
        RAMK = RAMX - RAMY
        ty1 = (int(dlina) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMY + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/95_it/ps.txt', 'r').read()
        Txt_38 = open('rs/72_it/38_xl.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 61, 22.5, 26, 20
        RAMZ, RAM = RAMX - RAMK, 60
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12

        ty2 = (int(dlina) - 2 * 78 - 26) / 2 - RAM / 2
        key = int(ty2 / RAM)
        CY = ty2 - key * RAM + 78 + 13 - 3
        txt_ss = txt_ss.replace('CY', str(CY))

        for x in range(2 * key + 2):
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace('CY', str(CY))
            CY = CY + RAM

        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMZ', str(RAMX))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace(str(CY - RAM) + "+" + str(RAM), str(CY - RAM + 7))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/95_it/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 26
        RAMZ = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h0 = round(
            (2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty1 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0], 3)

        txt_ss = txt_ss.replace('OBV0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', str(h0))
        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/95_it/pssl2.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 26
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/95_it/but.txt', 'r').read()
        RAMY = 29.5 if int(visota) >= 165 else 22.5
        RAMX, RAMK, oBv[2] = 80, 35.5, 20
        RAMZ = RAMX - RAMK
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK
        h = [0] * 12
        for i in range(11, -1, -1):
            h[i] = round(
                (2 * (rRr - oBv[i]) - ((2 * (rRr - oBv[i])) ** 2 - (ty1 - oBv[i]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[i],
                3)
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('h' + str(i), str(h[i]))

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/95_it/butsl1.txt', 'r').read()
        RAMY = 22.5
        RAMX, RAMK, oBv[2] = 80, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK
        h0 = round(
            (2 * (rRr - oBv[0]) - ((2 * (rRr - oBv[0])) ** 2 - (ty0 - oBv[0]) ** 2 * 4) ** 0.5) / 2 + RAMZ + oBv[0], 3)

        txt_ss = txt_ss.replace('OBV0', str(oBv[0]))
        txt_ss = txt_ss.replace('h0', str(h0))
        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) < 130:
        txt_ss = open('rs/95_it/butsl2.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss
