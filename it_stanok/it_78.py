def it_78(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 35.4, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/78_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/78_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 52
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
        txt_ss = open('rs/78_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/78_it/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 6) / 3 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/78_it/per4.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 3) / 2 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = lxp - 103
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[8]
        txt_ss = open('rs/78_it/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 9) / 4 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dx3 = (lxp - 103) * 3
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dx3', f'{dx3:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/78_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] - 6
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
        if k[7] in ('Фасад', 'Бутыл.', 'СТЕКЛО'):
            pod_92 = open('pl/92_f_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.06 + 0.01} ')
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.06 + 0.01} ')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss