def ss_11(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/11/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '120')

    elif k[7] =='Хлеб':
        txt_ss = open('rs/11/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '120')

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/11/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '120')

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/11/xlst.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '120')

    elif k[7] == 'ПСЯ' and int(visota) >= 140:
        txt_ss = open('rs/11/ps.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '100')
        txt_ss = txt_ss.replace('RAMY', '40')
        txt_ss = txt_ss.replace('RAMPS', '70')

    elif k[7] == 'ПСЯ' and 129 <= int(visota) < 140:
        txt_ss = open('rs/11/ps.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '77')
        txt_ss = txt_ss.replace('RAMY', '35')
        txt_ss = txt_ss.replace('RAMPS', '67')

    elif k[7] == 'ПСЯ' and int(visota) < 129:
        txt_ss = open('rs/11/ps.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '77')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('RAMPS', '67')
        txt_ss = txt_ss.replace('t-9', 't-2')
        txt_ss = txt_ss.replace('146', '136')

    elif k[7] == 'Бутыл.' and int(visota) >= 145:
        txt_ss = open('rs/11/f.txt', 'r').read()
        RAMX, RAMY = 79, 48
        tx1 = RAMX - RAMY
        ty1 = (int(visota) - 2 * RAMY) / 2
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('rRr', str(round(rRr, 3)))

    elif k[7] == 'Бутыл.' and int(visota) < 145:
        txt_ss = open('rs/11/f.txt', 'r').read()
        RAMX, RAMY = 69, 38
        tx1 = RAMX - RAMY
        ty1 = (int(visota) - 2 * RAMY) / 2
        rRr = (tx1 * tx1 + ty1 * ty1) / (2 * tx1)

        txt_ss = txt_ss.replace('t-9', 't-2')
        txt_ss = txt_ss.replace('146', '136')
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