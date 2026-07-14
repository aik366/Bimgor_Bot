oBv51it = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6]

def it_51(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv51it.copy()
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/51_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/51_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 59.3
        lyp = int(dlina) - lxp + zaz
        dx1 = lxp - zaz

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', str(lxp))
        txt_ss = txt_ss.replace('lyp', str(lyp))
        txt_ss = txt_ss.replace('dx1', str(dx1))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] =='Хлеб':
        txt_ss = open('rs/51_it/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/xl_st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 6) / 3 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ2':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/perxl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 6) / 3 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ4':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/per4.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 3) / 2 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = lxp - 103
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ4_xl':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/per4xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 3) / 2 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = lxp - 103
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51_it/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        lxp = (int(dlina) - 106 - 9) / 4 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dx3 = (lxp - 103) * 3
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dx3', f'{dx3:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ'and int(visota) >= 146:
        txt_ss = open('rs/51_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/51_it/but.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51_it/butsl.txt', 'r').read()
        RAMX, RAMY = RAM[0], 29.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/51_it/pssl2.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss