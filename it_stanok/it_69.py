def it_69(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]

    if k[7] == 'Фасад':
        txt_ss = open('rs/69_it/f.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        ty5 = (int(visota) - 2 * (RAMY + oBv[6])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))


    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/69_it/st.txt', 'r').read()
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
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/69_it/xl.txt', 'r').read()
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
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/69_it/xl_st.txt', 'r').read()
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
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/69_it/but.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 160:
            RAMY = 22.5
        else:
            RAMY = 28
        RAMX = 44.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(visota) - 2 * (RAMY + oBv[5])) / 2
        ty5 = (int(visota) - 2 * (RAMY + oBv[6])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/69_it/ps.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        tx1, tx2, tx3, tx4 = 2.5, 5, 7.5, 10
        ty1 = (int(dlina) - 2 * (RAMY + oBv[5])) / 2
        ty5 = (int(dlina) - 2 * (RAMY + oBv[6])) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        rRr2 = (tx2 ** 2 + ty1 ** 2) / (2 * tx2)
        rRr3 = (tx3 ** 2 + ty1 ** 2) / (2 * tx3)
        rRr4 = (tx4 ** 2 + ty1 ** 2) / (2 * tx4)
        rRr5 = (tx4 ** 2 + ty5 ** 2) / (2 * tx4)

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Бутыл.' and int(visota) >= 120 and int(visota) < 146:
        txt_ss = open('rs/69_it/butsl.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        ty5 = (int(visota) - 2 * (RAMY + oBv[6])) / 2
        rRr5 = (10 ** 2 + ty5 ** 2) / (2 * 10)

        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('OBV0', str(oBv[0]))
        txt_ss = txt_ss.replace('OBV7', str(oBv[7]))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 110 and int(visota) < 146:
        txt_ss = open('rs/69_it/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 22.5
        ty5 = (int(dlina) - 2 * (RAMY + oBv[6])) / 2
        rRr5 = (10 ** 2 + ty5 ** 2) / (2 * 10)

        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('OBV0', str(oBv[0]))
        txt_ss = txt_ss.replace('OBV7', str(oBv[7]))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка' or (k[7] == 'Бутыл.' and int(visota) < 120) \
            or (k[7] == 'ПСЯ' and int(visota) < 110):
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss