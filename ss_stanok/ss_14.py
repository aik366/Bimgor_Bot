def ss_14(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/14/f.txt', 'r').read()
        RAMX, RAMY = 120, 70
        tx1 = (RAMX - RAMY) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] =='Хлеб':
        txt_ss = open('rs/14/xl.txt', 'r').read()
        RAMX, RAMY = 120, 70
        tx1 = (RAMX - RAMY) / 2
        ty1 = (int(dlina) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/14/st.txt', 'r').read()
        RAMX, RAMY = 120, 70
        tx1 = (RAMX - RAMY) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/14/xlst.txt', 'r').read()
        RAMX, RAMY = 120, 70
        tx1 = (RAMX - RAMY) / 2
        ty1 = (int(dlina) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and int(visota) >= 140:
        txt_ss = open('rs/14/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 100, 40, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and 129 <= int(visota) < 140:
        txt_ss = open('rs/14/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 100, 35, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and int(visota) < 129:
        txt_ss = open('rs/14/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 100, 30, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace('t-9', 't-2')
        txt_ss = txt_ss.replace('146', '136')

    elif k[7] == 'Бутыл.' and int(visota) >= 140:
        txt_ss = open('rs/14/but.txt', 'r').read()
        RAMX, RAMY, RAMK = 110, 40, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        if int(visota) <= 155:
            txt_ss = txt_ss.replace('DS=1', 'DS=3')

    elif k[7] == 'Бутыл.' and int(visota) < 140:
        txt_ss = open('rs/14/butsl.txt', 'r').read()
        RAMX, RAMY, RAMK = 110, 40, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'Планка'):
        return txt_ss
    elif k[6] == '22':
        txt_ss = txt_ss.replace("146", "137")
    elif k[6] == '23':
        txt_ss = txt_ss.replace("146", "157")
    elif k[6] == '24':
        txt_ss = txt_ss.replace("t-9", "t-3")
    elif k[6] == '26':
        txt_ss = txt_ss.replace("146", "150")
        txt_ss = txt_ss.replace("t-9", "t-2.5")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("146", "136")
        txt_ss = txt_ss.replace("t-9", "t-2")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("146", "144")
        txt_ss = txt_ss.replace("t-9", "t-1.2")
    elif k[6] == '30':
        txt_ss = txt_ss.replace("146", "159")
        txt_ss = txt_ss.replace("t-9", "t-12.9")

    return txt_ss