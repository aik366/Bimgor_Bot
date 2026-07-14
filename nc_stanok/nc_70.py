def nc_70(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]

    if k[7] == 'Фасад':
        txt_ss = open('rs/70/f.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        tx1, tx2, tx3, tx4, tx6 = 2.5, 5, 7.5, 10, 6
        ty1 = (int(visota) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        ty6 = (int(visota) - 2 * RAMY - 2 * oBv[1]) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)
        rRr6 = (tx6 ** 2 + ty6 ** 2) / (2 * tx6)
        h3 = round(RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(visota) / 2 - (RAMY + 47)) ** 2) ** 0.5, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('rRr6', str(round(rRr6, 3)))
        txt_ss = txt_ss.replace('h3', str(h3))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[7]
        txt_ss = open('rs/69/st.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(visota) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/70/xl.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        tx1, tx2, tx3, tx4, tx6 = 2.5, 5, 7.5, 10, 6
        ty1 = (int(dlina) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(dlina) - 2 * (RAMY + oBv[5])) / 2
        ty6 = (int(dlina) - 2 * RAMY - 2 * oBv[1]) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)
        rRr6 = (tx6 ** 2 + ty6 ** 2) / (2 * tx6)
        h3 = round(RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(dlina) / 2 - (RAMY + 47)) ** 2) ** 0.5, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('rRr6', str(round(rRr6, 3)))
        txt_ss = txt_ss.replace('h3', str(h3))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[7]
        txt_ss = open('rs/69/xlst.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(dlina) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(dlina) - 2 * (RAMY + oBv[5])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/69/but.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 160:
            RAMY = 22.5
        else:
            RAMY = 28
        RAMX = 44.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(visota) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/69/ps.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(dlina) - 2 * (RAMY + oBv[3])) / 2
        ty5 = (int(dlina) - 2 * (RAMY + oBv[5])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 120 and int(visota) < 146:
        txt_ss = open('rs/69/butsl.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        ty5 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        rRr5 = (10 ** 2 + ty5 ** 2) / (2 * 10)

        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('oBv5', str(oBv[5]))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 110 and int(visota) < 146:
        txt_ss = open('rs/69/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        oBv[0], oBv[5] = 22, 5
        ty5 = (int(dlina) - 2 * (RAMY + oBv[5])) / 2
        rRr5 = (10 ** 2 + ty5 ** 2) / (2 * 10)

        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('oBv0', str(oBv[0]))
        txt_ss = txt_ss.replace('oBv5', str(oBv[5]))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка' or (k[7] == 'Бутыл.' and int(visota) < 120) \
            or (k[7] == 'ПСЯ' and int(visota) < 110):
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss