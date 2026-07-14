from it_stanok import it_96

oBv111it = [27, 32, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 28, 6, 10.4, 1.4]


def it_111(k, dlina, visota, RAM):
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_96(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = oBv111it.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/111_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/111_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 62 + (RAM[0] - 44.5)
        lyp = int(dlina) - lxp + zaz
        dx1 = lxp - zaz

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', str(lxp))
        txt_ss = txt_ss.replace('lyp', str(lyp))
        txt_ss = txt_ss.replace('dx1', str(dx1))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/111_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/111_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    if RAM[4] == 1:
        RAMX, RAMY = RAM[0], RAM[0]
        if k[7] == 'Бутыл.':
            pod_92 = open('pl/92_f_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[4]- (RAM[0]-RAM[1]) - 3.5 + 0.01} ')
        elif k[7] in ('Фасад', 'Фасад2', 'СТЕКЛО'):
            pod_92 = open('pl/92_f_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[4] - 3.5 + 0.01} ')
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[4] - 3.5 + 0.01} ')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
