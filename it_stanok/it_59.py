def it_59(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 0, 0]
    oBv[10], oBv[11] = oBv[4] - 10, oBv[6] - 10
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/59_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/59_it/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/59_it/st.txt', 'r').read()
        oBv[1] = oBv[8]
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/59_it/xl_st.txt', 'r').read()
        oBv[1] = oBv[8]
        RAMX, RAMY = RAM[0] + 51.5, RAM[0]
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/59_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
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
        txt_ss = txt_ss.replace('RAMZ', str(RAMX))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/59_it/but.txt', 'r').read()
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/59_it/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK = 80, 22.5, 35.5
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/59_it/pssl2.txt', 'r').read()
        RAMX, RAMY, RAMK = 80, 22.5, 35.5
        ty1 = (int(visota) - RAMY * 2) / 2
        tx1 = (ty1 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx1 + RAMK

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/59_it/butsl1.txt', 'r').read()
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
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) < 130:
        txt_ss = open('rs/59_it/butsl2.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[2] = 80, 22.5, 35.5, 20
        RAMZ = RAMX - RAMK
        ty0 = (int(visota) - 2 * RAMY) / 2
        tx0 = (ty0 ** 2 - RAMK ** 2) / (2 * RAMK)
        rRr = tx0 + RAMK

        txt_ss = txt_ss.replace('RRR', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss
