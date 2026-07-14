def it_12(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/12_it/f.txt', 'r').read()
        RAMX, RAMY = 120, 70
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] =='Хлеб':
        txt_ss = open('rs/12_it/xl.txt', 'r').read()
        RAMX, RAMY = 120, 70
        rRr = (((int(dlina) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/12_it/st.txt', 'r').read()
        RAMX, RAMY = 120, 70
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/12_it/xlst.txt', 'r').read()
        RAMX, RAMY = 120, 70
        rRr = (((int(dlina) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and int(visota) >= 140:
        txt_ss = open('rs/11_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 100, 40, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and 129 <= int(visota) < 140:
        txt_ss = open('rs/11_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 100, 35, 70
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'ПСЯ' and int(visota) < 129:
        txt_ss = open('rs/11_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 77, 30, 67
        tx1 = (RAMX - RAMK) / 2
        ty1 = (int(visota) - 2 * RAMY) / 4
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace("131", "136")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2, 0,")

    elif k[7] == 'Бутыл.' and int(visota) >= 145:
        txt_ss = open('rs/12_it/f.txt', 'r').read()
        RAMX, RAMY = 79, 48
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'Бутыл.' and int(visota) < 145:
        txt_ss = open('rs/12_it/f.txt', 'r').read()
        RAMX, RAMY = 69, 38
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + (RAMX - RAMY) ** 2) / (2 * (RAMX - RAMY))

        txt_ss = txt_ss.replace('t-9', 't-2')
        txt_ss = txt_ss.replace('146', '136')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))
        txt_ss = txt_ss.replace("131", "136")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2, 0,")

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'Планка'):
        return txt_ss
    elif k[6] == '22':
        txt_ss = txt_ss.replace("131", "137")
    elif k[6] == '23':
        txt_ss = txt_ss.replace("131", "157")
    elif k[6] == '24':
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 3, 0,")
    elif k[6] == '26':
        txt_ss = txt_ss.replace("131", "150")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2.5, 0,")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("131", "136")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2, 0,")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("131", "144")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 1.2, 0,")
    elif k[6] == '30':
        txt_ss = txt_ss.replace("131", "159")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 12.9, 0,")

    return txt_ss