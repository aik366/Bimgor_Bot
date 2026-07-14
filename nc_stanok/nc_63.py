def nc_63(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 12, 27.5, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'
    ux, uy, h, RAM = [0]*10, [0]*10, [0]*10, [0]*10

    if k[7] == 'Фасад':
        txt_ss = open('rs/63/f.txt', 'r').read()
        RAMY = 44.5
        RAMX = 74 if int(visota) > 319 else 74 - (320 - int(visota)) * 0.2
        RAMK = 67.54 + (int(visota) - 360) * 0.08 if int(visota) > 360 else 67.5 - (360 - int(visota)) * 0.025
        ty0 = (int(visota) - 2 * RAMK) / 4
        tx0 = (RAMX - RAMY) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            if RAMK <= (RAMY + oBv[i]):
                RAM[i] = 0.001
                h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            else:
                RAM[i] = RAMK - RAMY - oBv[i]
                h[i] = 0

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("RAM" + str(i), str(round(RAM[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/63/st.txt', 'r').read()
        RAMY = 44.5
        RAMX = 74 if int(visota) > 319 else 74 - (320 - int(visota)) * 0.2
        RAMK = 67.54 + (int(visota) - 360) * 0.08 if int(visota) > 360 else 67.5 - (360 - int(visota)) * 0.025
        ty0 = (int(visota) - 2 * RAMK) / 4
        tx0 = (RAMX - RAMY) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            if RAMK <= (RAMY + oBv[i]):
                RAM[i] = 0.001
                h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            else:
                RAM[i] = RAMK - RAMY - oBv[i]
                h[i] = 0

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("RAM" + str(i), str(round(RAM[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/63/xl.txt', 'r').read()
        RAMY = 44.5
        RAMX = 74 if int(dlina) > 319 else 74 - (320 - int(dlina)) * 0.2
        RAMK = 67.54 + (int(dlina) - 360) * 0.08 if int(dlina) > 360 else 67.5 - (360 - int(dlina)) * 0.025
        ty0 = (int(dlina) - 2 * RAMK) / 4
        tx0 = (RAMX - RAMY) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            if RAMK <= (RAMY + oBv[i]):
                RAM[i] = 0.001
                h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            else:
                RAM[i] = RAMK - RAMY - oBv[i]
                h[i] = 0

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("RAM" + str(i), str(round(RAM[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/63/xl_st.txt', 'r').read()
        RAMY = 44.5
        RAMX = 74 if int(dlina) > 319 else 74 - (320 - int(dlina)) * 0.2
        RAMK = 67.54 + (int(dlina) - 360) * 0.08 if int(dlina) > 360 else 67.5 - (360 - int(dlina)) * 0.025
        ty0 = (int(dlina) - 2 * RAMK) / 4
        tx0 = (RAMX - RAMY) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            if RAMK <= (RAMY + oBv[i]):
                RAM[i] = 0.001
                h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            else:
                RAM[i] = RAMK - RAMY - oBv[i]
                h[i] = 0

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("RAM" + str(i), str(round(RAM[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        oBz = [0, 0, 0, oBv[3] - 10, oBv[4] - 10, oBv[5] - 10, oBv[6] - 10, 0, 0, 0]
        txt_ss = open('rs/63/but.txt', 'r').read()
        RAMX, RAMK = 71, 44.5
        RAMY = 22.5 if 146 <= int(visota) < 170 else 29.5
        ty0 = (int(visota) - 2 * RAMY) / 4
        tx0 = (RAMX - RAMK) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)
        g, n = [0] * 10, [0] * 10

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            g[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            n[i] = rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - oBz[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("n" + str(i), str(round(n[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("oBz" + str(i), str(oBz[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and 140 <= int(visota) < 146:
        txt_ss = open('rs/63/butsl.txt', 'r').read()
        RAMX, RAMK, RAMY = 71, 44.5, 29.5
        ty0 = (int(visota) - 2 * RAMY) / 4
        tx0 = (RAMX - RAMK) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        oBz = [0, 0, 0, oBv[3] - 10, oBv[4] - 10, oBv[5] - 10, oBv[6] - 10, 0, 0, 0]
        txt_ss = open('rs/63/ps.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 35
        ty0 = (int(visota) - 2 * RAMY) / 4
        tx0 = (RAMX - RAMK) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)
        g = [0] * 10

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            g[i] = rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - oBz[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("oBz" + str(i), str(round(oBz[i], 3)))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'ПСЯ' and 140 <= int(visota) < 146:
        txt_ss = open('rs/63/pssl.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 35
        ty0 = (int(visota) - 2 * RAMY) / 4
        tx0 = (RAMX - RAMK) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)
    
    elif k[7] == 'ПСЯ' and 120 <= int(visota) < 140:
        txt_ss = open('rs/63/pssl2.txt', 'r').read()
        RAMX, RAMY, RAMK = 61, 22.5, 35
        ty0 = (int(visota) - 2 * RAMY) / 4
        tx0 = (RAMX - RAMK) / 2
        rRr = (tx0 * tx0 + ty0 * ty0) / (2 * tx0)

        for i in range(10):
            ux[i] = ((rRr - tx0) / rRr) * oBv[i]
            uy[i] = (ty0 / rRr) * oBv[i]
            h[i] = rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("ux" + str(i), str(round(ux[i], 3)))
            txt_ss = txt_ss.replace("uy" + str(i), str(round(uy[i], 3)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace("tx0", str(round(tx0, 3)))
        txt_ss = txt_ss.replace("ty0", str(round(ty0, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(round(RAMK, 3)))
        txt_ss = txt_ss.replace("Kant", Kant)


    elif (k[7] == 'Бутыл.' and int(visota) < 140) or\
        (k[7] == 'ПСЯ' and int(visota) < 120) or k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss