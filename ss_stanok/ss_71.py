from ss_stanok import ss_70


def ss_71(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПСЯ', 'Бутыл.'):
        return ss_70(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 27.5, 10.6, 19]

    if k[7] == 'Фасад':
        txt_ss = open('rs/71/f.txt', 'r').read()
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
        h3 = RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(visota) / 2 - (RAMY + 47)) ** 2) ** 0.5
        h4 = RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(visota) / 2 - (RAMY + 67)) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('rRr6', str(round(rRr6, 3)))
        txt_ss = txt_ss.replace('h3', str(round(h3, 3)))
        txt_ss = txt_ss.replace('h4', str(round(h4, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/71/xl.txt', 'r').read()
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
        h3 = RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(dlina) / 2 - (RAMY + 47)) ** 2) ** 0.5
        h4 = RAMX + oBv[1] + rRr6 - ((rRr6 - 14) ** 2 - (int(dlina) / 2 - (RAMY + 67)) ** 2) ** 0.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('rRr1', str(round(rRr1, 3)))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('rRr3', str(round(rRr3, 3)))
        txt_ss = txt_ss.replace('rRr4', str(round(rRr4, 3)))
        txt_ss = txt_ss.replace('rRr5', str(round(rRr5, 3)))
        txt_ss = txt_ss.replace('rRr6', str(round(rRr6, 3)))
        txt_ss = txt_ss.replace('h3', str(round(h3, 3)))
        txt_ss = txt_ss.replace('h4', str(round(h4, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss