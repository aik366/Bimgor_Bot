def it_64(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]
    oBz = [0, 0, 0, oBv[3] - 10, oBv[4] - 10, oBv[5] - 10, oBv[6] - 10, 6, 0, 0]
    Kant = '10.4' if k[5] == '18' else '14.8'
    h, g = [0]*10, [0]*10

    if k[7] == 'Фасад':
        txt_ss = open('rs/64_it/f.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 44.5, 10
        rRr = (((int(visota) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMY + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMY + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(visota) / 2 - RAMY - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/64_it/st.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 44.5, 10
        rRr = (((int(visota) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMY + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMY + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(visota) / 2 - RAMY - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/64_it/xl.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 44.5, 10
        rRr = (((int(dlina) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMY + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMY + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(dlina) / 2 - RAMY - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/64_it/xlst.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 44.5, 10
        rRr = (((int(dlina) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMY + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(dlina) / 2 - RAMY - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMY + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(dlina) / 2 - RAMY - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/64_it/but.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 22.5, 10
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMX + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(visota) / 2 - RAMY - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMX + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(visota) / 2 - RAMY - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 120:
        txt_ss = open('rs/64_it/butsl.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 22.5, 10
        rRr = (((int(visota) - 2 * RAMY) / 2) ** 2 + dug ** 2) / (2 * dug)

        h[0] = RAMX + 17 + dug - (rRr + 17 - ((rRr + 17) ** 2 - (int(visota) / 2 - RAMY - 17) ** 2) ** 0.5)
        txt_ss = txt_ss.replace("OBV0", '17')
        txt_ss = txt_ss.replace("h0", str(round(h[0], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and int(visota) >= 165:
        txt_ss = open('rs/64_it/ps.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 22.5, 10
        rRr = (((int(dlina) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        for i in range(10):
            h[i] = RAMY + oBv[i] + dug - (rRr + oBv[i] - ((rRr + oBv[i]) ** 2 - (int(dlina) / 2 - RAMX - oBv[i]) ** 2) ** 0.5)
            g[i] = RAMY + oBz[i] + dug - (rRr + oBz[i] - ((rRr + oBz[i]) ** 2 - (int(dlina) / 2 - RAMX - oBz[i]) ** 2) ** 0.5)
            txt_ss = txt_ss.replace("OBV" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("h" + str(i), str(round(h[i], 3)))
            txt_ss = txt_ss.replace("g" + str(i), str(round(g[i], 3)))

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and 140 <= int(visota) < 165:
        txt_ss = open('rs/64_it/pssl.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 22.5, 10
        rRr = (((int(dlina) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'ПСЯ' and 120 <= int(visota) < 140:
        txt_ss = open('rs/64_it/pssl2.txt', 'r').read()
        RAMX, RAMY, dug = 44.5, 22.5, 10
        rRr = (((int(dlina) - 2 * RAMX) / 2) ** 2 + dug ** 2) / (2 * dug)

        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif (k[7] == 'Бутыл.' and int(visota) < 120) or\
        (k[7] == 'ПСЯ' and int(visota) < 120) or k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss