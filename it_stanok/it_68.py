def it_68(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6]
    Kant = '10.4' if k[5] == '18' else '14.8'
    ux, uy = [0] * 10, [0] * 10

    if k[7] == 'Фасад':
        txt_ss = open('rs/68_it/f.txt', 'r').read()
        if int(visota) < 296:
            RAMX = 45.5 + (int(visota) * 0.07)
            ty1 = 4 + (int(visota) * 0.07)
        else:
            RAMX, ty1 = 70, 27
        RAMY = 44.5
        tx1 = (RAMX - RAMY) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3]= ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        hs = RAMY + oBv[0] + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (RAMY + oBv[2] - (RAMX + oBv[0] - rRr1)) ** 2) ** 0.5
        if int(visota) >= 307:
            XRAM1, XRAM2 = (RAMX + oBv[0] - rRr1 + ux[2]), (RAMY + oBv[2])
            YRAM1, YRAM2 = (RAMY + oBv[0] + uy[2]), (RAMY + oBv[0] + 2 * ty1)
        else:
            txt_ss = txt_ss.replace('rRr1-(OBV2-OBV0), 1', 'rRr1-(OBV2-OBV0), 2')
            XRAM1, XRAM2 = (RAMY + oBv[2]), (RAMY + oBv[2]) + 0.001
            YRAM1, YRAM2 = hs, hs - 0.001

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        txt_ss = txt_ss.replace('XRAM1', f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace('XRAM2', f'{XRAM2:.3f}')
        txt_ss = txt_ss.replace('YRAM1', f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace('YRAM2', f'{YRAM2:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/68_it/st.txt', 'r').read()
        if int(visota) < 296:
            RAMX = 45.5 + (int(visota) * 0.07)
            ty1 = 4 + (int(visota) * 0.07)
        else:
            RAMX, ty1 = 70, 27
        RAMY = 44.5
        tx1 = (RAMX - RAMY) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3]= ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        hs = RAMY + oBv[0] + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (RAMY + oBv[2] - (RAMX + oBv[0] - rRr1)) ** 2) ** 0.5
        if int(visota) >= 307:
            XRAM1, XRAM2 = (RAMX + oBv[0] - rRr1 + ux[2]), (RAMY + oBv[2])
            YRAM1, YRAM2 = (RAMY + oBv[0] + uy[2]), (RAMY + oBv[0] + 2 * ty1)
        else:
            XRAM1, XRAM2 = (RAMY + oBv[2]), (RAMY + oBv[2]) + 0.001
            YRAM1, YRAM2 = hs, hs - 0.001

        txt_ss = txt_ss.replace('XRAM1', f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace('XRAM2', f'{XRAM2:.3f}')
        txt_ss = txt_ss.replace('YRAM1', f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace('YRAM2', f'{YRAM2:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/68_it/xl.txt', 'r').read()
        if int(dlina) < 296:
            RAMX = 45.5 + (int(dlina) * 0.07)
            ty1 = 4 + (int(dlina) * 0.07)
        else:
            RAMX, ty1 = 70, 27
        RAMY = 44.5
        tx1 = (RAMX - RAMY) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3]= ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        hs = RAMY + oBv[0] + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (RAMY + oBv[2] - (RAMX + oBv[0] - rRr1)) ** 2) ** 0.5
        if int(dlina) >= 307:
            XRAM1, XRAM2 = (RAMX + oBv[0] - rRr1 + ux[2]), (RAMY + oBv[2])
            YRAM1, YRAM2 = (RAMY + oBv[0] + uy[2]), (RAMY + oBv[0] + 2 * ty1)
        else:
            txt_ss = txt_ss.replace('rRr1-(OBV2-OBV0), 2', 'rRr1-(OBV2-OBV0), 1')
            XRAM1, XRAM2 = (RAMY + oBv[2]), (RAMY + oBv[2]) + 0.001
            YRAM1, YRAM2 = hs, hs - 0.001

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        txt_ss = txt_ss.replace('XRAM1', f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace('XRAM2', f'{XRAM2:.3f}')
        txt_ss = txt_ss.replace('YRAM1', f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace('YRAM2', f'{YRAM2:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/68_it/xlst.txt', 'r').read()
        if int(dlina) < 296:
            RAMX = 45.5 + (int(dlina) * 0.07)
            ty1 = 4 + (int(dlina) * 0.07)
        else:
            RAMX, ty1 = 70, 27
        RAMY = 44.5
        tx1 = (RAMX - RAMY) / 2
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3]= ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        hs = RAMY + oBv[0] + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (RAMY + oBv[2] - (RAMX + oBv[0] - rRr1)) ** 2) ** 0.5
        if int(dlina) >= 307:
            XRAM1, XRAM2 = (RAMX + oBv[0] - rRr1 + ux[2]), (RAMY + oBv[2])
            YRAM1, YRAM2 = (RAMY + oBv[0] + uy[2]), (RAMY + oBv[0] + 2 * ty1)
        else:
            XRAM1, XRAM2 = (RAMY + oBv[2]), (RAMY + oBv[2]) + 0.001
            YRAM1, YRAM2 = hs, hs - 0.001

        txt_ss = txt_ss.replace('XRAM1', f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace('XRAM2', f'{XRAM2:.3f}')
        txt_ss = txt_ss.replace('YRAM1', f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace('YRAM2', f'{YRAM2:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 150:
        txt_ss = open('rs/68_it/but.txt', 'r').read()
        RAMY = 29.5 if int(visota) >= 190 else 22.4
        RAMX, RAMK = 45.5 + (int(visota) * 0.075), 44.5
        tx1 = (RAMX - RAMK) / 2
        ty1 = 4 + (int(visota) * 0.057)
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        hp = RAMY + oBv[0] + 2 * ty1 - ((rRr1 + oBv[0]) ** 2 - (rRr1 + oBv[0] - (RAMX - RAMK)) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3] = ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        txt_ss = txt_ss.replace('hp', f'{hp:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 150:
        txt_ss = open('rs/68_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 45.5 + (int(visota) * 0.075), 22.5, 44.5
        tx1 = (RAMX - RAMK) / 2
        ty1 = 4 + (int(visota) * 0.057)
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[1] - oBv[0])) ** 2 - (oBv[1] - oBv[0]) ** 2) ** 0.5
        hp = RAMY + oBv[0] + 2 * ty1 - ((rRr1 + oBv[0]) ** 2 - (rRr1 + oBv[0] - (RAMX - RAMK)) ** 2) ** 0.5
        uy[0] = ty1 / rRr1 * (rRr1 - oBv[0])
        ux[0] = rRr1 - oBv[0] - (rRr1 - tx1) / rRr1 * (rRr1 - oBv[0])
        uy[1] = ty1 / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        ux[1] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[1] - oBv[0]))
        h2 = RAMX + oBv[0] - rRr1 + ((rRr1 + (oBv[2] - oBv[0])) ** 2 - (oBv[2] - oBv[0]) ** 2) ** 0.5
        uy[2] = ty1 / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        ux[2] = (rRr1 - tx1) / rRr1 * (rRr1 + (oBv[2] - oBv[0]))
        uy[3] = ty1 / rRr1 * (rRr1 + (oBv[3] - oBv[0]))
        uy[4] = ty1 / rRr1 * (rRr1 + (oBv[4] - oBv[0]))
        uy[5] = ty1 / rRr1 * (rRr1 + (oBv[5] - oBv[0]))
        uy[6] = ty1 / rRr1 * (rRr1 + (oBv[6] - oBv[0]))
        ux[3] = rRr1 - (oBv[0] - oBv[3]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[3]))
        ux[4] = rRr1 - (oBv[0] - oBv[4]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[4]))
        ux[5] = rRr1 - (oBv[0] - oBv[5]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[5]))
        ux[6] = rRr1 - (oBv[0] - oBv[6]) - (rRr1 - tx1) / rRr1 * (rRr1 - (oBv[0] - oBv[6]))

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace('ux' + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace('uy' + str(i), f'{uy[i]:.3f}')

        txt_ss = txt_ss.replace('hp', f'{hp:.3f}')
        txt_ss = txt_ss.replace('h1', f'{h1:.3f}')
        txt_ss = txt_ss.replace('h2', f'{h2:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] in ('ПСЯ', 'Бутыл.') and 125 <= int(visota) < 150:
        txt_ss = open('rs/68_it/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK, oBv[0] = 45.5 + (int(visota) * 0.075), 22.5, 44.5, 17
        tx1 = (RAMX - RAMK) / 2
        ty1 = 4 + (int(visota) * 0.057)
        rRr1 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        hp = RAMY + oBv[0] + 2 * ty1 - ((rRr1 + oBv[0]) ** 2 - (rRr1 + oBv[0] - (RAMX - RAMK)) ** 2) ** 0.5

        txt_ss = txt_ss.replace('OBV0', str(oBv[0]))
        txt_ss = txt_ss.replace('hp', f'{hp:.3f}')
        txt_ss = txt_ss.replace('tx1', f'{tx1:.3f}')
        txt_ss = txt_ss.replace('ty1', f'{ty1:.3f}')
        txt_ss = txt_ss.replace('rRr1', f'{rRr1:.3f}')
        txt_ss = txt_ss.replace('RAMX', f'{RAMX:.3f}')
        txt_ss = txt_ss.replace('RAMY', f'{RAMY:.3f}')
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif (k[7] == 'Планка') or (k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 125):
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss