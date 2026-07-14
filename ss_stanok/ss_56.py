from ss_stanok import ss_63


def ss_56(k, dlina, visota, RAM):
    if k[7] == 'ПСЯ':
        return ss_63.ss_63(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 12, 27.5, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'
    ko, korx, kory, h, ha, hb, hc, hd = [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10
    pa, pb, pc, pd, xa, xb, xc, xd = [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10
    ya, yb, yc, yd, ka, kb, kc, kd = [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10

    if k[7] == 'Фасад':
        txt_ss = open('rs/56/f.txt', 'r').read()
        RAMX, RAMY, rRr1, tx0 = 113, 44.5, 21.5, 36.3
        RAMK = RAMY + (int(visota) - 305) * 0.125 if int(visota) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMY - tx0
        ty1 = (int(visota) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMY + rRr2, RAMK, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        if oBv[0] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h0", str(RAMX + oBv[0]))
            txt_ss = txt_ss.replace("RAM0", str(RAMK))
        if oBv[1] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h1", str(RAMX + oBv[1]))
            txt_ss = txt_ss.replace("RAM1", str(RAMK))
        if oBv[2] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h2", str(RAMX + oBv[2]))
            txt_ss = txt_ss.replace("RAM2", str(RAMK))
        if oBv[3] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h3", str(RAMX + oBv[3]))
            txt_ss = txt_ss.replace("RAM3", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("ha" + str(i), str(RAMX + oBv[3] - (i + 1)))
        if oBv[4] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h4", str(RAMX + oBv[4]))
            txt_ss = txt_ss.replace("RAM4", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hb" + str(i), str(RAMX + oBv[4] - (i + 1)))
        if oBv[5] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h5", str(RAMX + oBv[5]))
            txt_ss = txt_ss.replace("RAM5", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hc" + str(i), str(RAMX + oBv[5] - (i + 1)))
        if oBv[6] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h6", str(RAMX + oBv[6]))
            txt_ss = txt_ss.replace("RAM6", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hd" + str(i), str(RAMX + oBv[6] - (i + 1)))

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            if int(visota) < 253:
                korx[2] = 91.5 + ((rRr1 + oBv[2]) ** 2 - ((int(visota) - 89) / 2) ** 2) ** 0.5
                kory[2] = int(visota) / 2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (RAMY + oBv[3] - i - 1 - RAMK) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (RAMY + oBv[4] - i - 1 - RAMK) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (RAMY + oBv[5] - i - 1 - RAMK) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (RAMY + oBv[6] - i - 1 - RAMK) ** 2) ** 0.5
            ka[i] = (p ** 2 + (rRr1 + (oBv[3] - i - 1)) ** 2 - (rRr2 - (oBv[3] - i - 1)) ** 2) / (2 * p)
            xa[i] = xa1 + m * ka[i] / p - (f / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            ya[i] = ya1 + f * ka[i] / p + (m / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            kb[i] = (p ** 2 + (rRr1 + (oBv[4] - i - 1)) ** 2 - (rRr2 - (oBv[4] - i - 1)) ** 2) / (2 * p)
            xb[i] = xa1 + m * kb[i] / p - (f / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            yb[i] = ya1 + f * kb[i] / p + (m / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            kc[i] = (p ** 2 + (rRr1 + (oBv[5] - i - 1)) ** 2 - (rRr2 - (oBv[5] - i - 1)) ** 2) / (2 * p)
            xc[i] = xa1 + m * kc[i] / p - (f / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            yc[i] = ya1 + f * kc[i] / p + (m / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            kd[i] = (p ** 2 + (rRr1 + (oBv[6] - i - 1)) ** 2 - (rRr2 - (oBv[6] - i - 1)) ** 2) / (2 * p)
            xd[i] = xa1 + m * kd[i] / p - (f / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            yd[i] = ya1 + f * kd[i] / p + (m / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("xa" + str(i), f'{xa[i]:.3f}')
            txt_ss = txt_ss.replace("ya" + str(i), f'{ya[i]:.3f}')
            txt_ss = txt_ss.replace("xb" + str(i), f'{xb[i]:.3f}')
            txt_ss = txt_ss.replace("yb" + str(i), f'{yb[i]:.3f}')
            txt_ss = txt_ss.replace("xc" + str(i), f'{xc[i]:.3f}')
            txt_ss = txt_ss.replace("yc" + str(i), f'{yc[i]:.3f}')
            txt_ss = txt_ss.replace("xd" + str(i), f'{xd[i]:.3f}')
            txt_ss = txt_ss.replace("yd" + str(i), f'{yd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), str(RAMY + oBv[3] - (i + 1)))
            txt_ss = txt_ss.replace("pb" + str(i), str(RAMY + oBv[4] - (i + 1)))
            txt_ss = txt_ss.replace("pc" + str(i), str(RAMY + oBv[5] - (i + 1)))
            txt_ss = txt_ss.replace("pd" + str(i), str(RAMY + oBv[6] - (i + 1)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/56/st.txt', 'r').read()
        RAMX, RAMY, rRr1, tx0 = 113, 44.5, 21.5, 36.3
        RAMK = RAMY + (int(visota) - 305) * 0.125 if int(visota) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMY - tx0
        ty1 = (int(visota) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMY + rRr2, RAMK, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        if oBv[0] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h0", str(RAMX + oBv[0]))
            txt_ss = txt_ss.replace("RAM0", str(RAMK))
        if oBv[1] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h1", str(RAMX + oBv[1]))
            txt_ss = txt_ss.replace("RAM1", str(RAMK))
        if oBv[2] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h2", str(RAMX + oBv[2]))
            txt_ss = txt_ss.replace("RAM2", str(RAMK))
        if oBv[3] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h3", str(RAMX + oBv[3]))
            txt_ss = txt_ss.replace("RAM3", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("ha" + str(i), str(RAMX + oBv[3] - (i + 1)))
        if oBv[4] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h4", str(RAMX + oBv[4]))
            txt_ss = txt_ss.replace("RAM4", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hb" + str(i), str(RAMX + oBv[4] - (i + 1)))
        if oBv[5] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h5", str(RAMX + oBv[5]))
            txt_ss = txt_ss.replace("RAM5", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hc" + str(i), str(RAMX + oBv[5] - (i + 1)))
        if oBv[6] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h6", str(RAMX + oBv[6]))
            txt_ss = txt_ss.replace("RAM6", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hd" + str(i), str(RAMX + oBv[6] - (i + 1)))

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            if int(visota) < 253:
                korx[2] = 91.5 + ((rRr1 + oBv[2]) ** 2 - ((int(visota) - 89) / 2) ** 2) ** 0.5
                kory[2] = int(visota) / 2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (RAMY + oBv[3] - i - 1 - RAMK) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (RAMY + oBv[4] - i - 1 - RAMK) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (RAMY + oBv[5] - i - 1 - RAMK) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (RAMY + oBv[6] - i - 1 - RAMK) ** 2) ** 0.5
            ka[i] = (p ** 2 + (rRr1 + (oBv[3] - i - 1)) ** 2 - (rRr2 - (oBv[3] - i - 1)) ** 2) / (2 * p)
            xa[i] = xa1 + m * ka[i] / p - (f / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            ya[i] = ya1 + f * ka[i] / p + (m / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            kb[i] = (p ** 2 + (rRr1 + (oBv[4] - i - 1)) ** 2 - (rRr2 - (oBv[4] - i - 1)) ** 2) / (2 * p)
            xb[i] = xa1 + m * kb[i] / p - (f / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            yb[i] = ya1 + f * kb[i] / p + (m / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            kc[i] = (p ** 2 + (rRr1 + (oBv[5] - i - 1)) ** 2 - (rRr2 - (oBv[5] - i - 1)) ** 2) / (2 * p)
            xc[i] = xa1 + m * kc[i] / p - (f / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            yc[i] = ya1 + f * kc[i] / p + (m / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            kd[i] = (p ** 2 + (rRr1 + (oBv[6] - i - 1)) ** 2 - (rRr2 - (oBv[6] - i - 1)) ** 2) / (2 * p)
            xd[i] = xa1 + m * kd[i] / p - (f / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            yd[i] = ya1 + f * kd[i] / p + (m / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("xa" + str(i), f'{xa[i]:.3f}')
            txt_ss = txt_ss.replace("ya" + str(i), f'{ya[i]:.3f}')
            txt_ss = txt_ss.replace("xb" + str(i), f'{xb[i]:.3f}')
            txt_ss = txt_ss.replace("yb" + str(i), f'{yb[i]:.3f}')
            txt_ss = txt_ss.replace("xc" + str(i), f'{xc[i]:.3f}')
            txt_ss = txt_ss.replace("yc" + str(i), f'{yc[i]:.3f}')
            txt_ss = txt_ss.replace("xd" + str(i), f'{xd[i]:.3f}')
            txt_ss = txt_ss.replace("yd" + str(i), f'{yd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), str(RAMY + oBv[3] - (i + 1)))
            txt_ss = txt_ss.replace("pb" + str(i), str(RAMY + oBv[4] - (i + 1)))
            txt_ss = txt_ss.replace("pc" + str(i), str(RAMY + oBv[5] - (i + 1)))
            txt_ss = txt_ss.replace("pd" + str(i), str(RAMY + oBv[6] - (i + 1)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/56/xl.txt', 'r').read()
        RAMX, RAMY, rRr1, tx0 = 113, 44.5, 21.5, 36.3
        RAMK = RAMY + (int(dlina) - 305) * 0.125 if int(dlina) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMY - tx0
        ty1 = (int(dlina) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMY + rRr2, RAMK, int(dlina) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        if oBv[0] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h0", str(RAMX + oBv[0]))
            txt_ss = txt_ss.replace("RAM0", str(RAMK))
        if oBv[1] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h1", str(RAMX + oBv[1]))
            txt_ss = txt_ss.replace("RAM1", str(RAMK))
        if oBv[2] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h2", str(RAMX + oBv[2]))
            txt_ss = txt_ss.replace("RAM2", str(RAMK))
        if oBv[3] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h3", str(RAMX + oBv[3]))
            txt_ss = txt_ss.replace("RAM3", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("ha" + str(i), str(RAMX + oBv[3] - (i + 1)))
        if oBv[4] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h4", str(RAMX + oBv[4]))
            txt_ss = txt_ss.replace("RAM4", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hb" + str(i), str(RAMX + oBv[4] - (i + 1)))
        if oBv[5] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h5", str(RAMX + oBv[5]))
            txt_ss = txt_ss.replace("RAM5", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hc" + str(i), str(RAMX + oBv[5] - (i + 1)))
        if oBv[6] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h6", str(RAMX + oBv[6]))
            txt_ss = txt_ss.replace("RAM6", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hd" + str(i), str(RAMX + oBv[6] - (i + 1)))

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            if int(dlina) < 253:
                korx[2] = 91.5 + ((rRr1 + oBv[2]) ** 2 - ((int(dlina) - 89) / 2) ** 2) ** 0.5
                kory[2] = int(dlina) / 2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (RAMY + oBv[3] - i - 1 - RAMK) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (RAMY + oBv[4] - i - 1 - RAMK) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (RAMY + oBv[5] - i - 1 - RAMK) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (RAMY + oBv[6] - i - 1 - RAMK) ** 2) ** 0.5
            ka[i] = (p ** 2 + (rRr1 + (oBv[3] - i - 1)) ** 2 - (rRr2 - (oBv[3] - i - 1)) ** 2) / (2 * p)
            xa[i] = xa1 + m * ka[i] / p - (f / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            ya[i] = ya1 + f * ka[i] / p + (m / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            kb[i] = (p ** 2 + (rRr1 + (oBv[4] - i - 1)) ** 2 - (rRr2 - (oBv[4] - i - 1)) ** 2) / (2 * p)
            xb[i] = xa1 + m * kb[i] / p - (f / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            yb[i] = ya1 + f * kb[i] / p + (m / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            kc[i] = (p ** 2 + (rRr1 + (oBv[5] - i - 1)) ** 2 - (rRr2 - (oBv[5] - i - 1)) ** 2) / (2 * p)
            xc[i] = xa1 + m * kc[i] / p - (f / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            yc[i] = ya1 + f * kc[i] / p + (m / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            kd[i] = (p ** 2 + (rRr1 + (oBv[6] - i - 1)) ** 2 - (rRr2 - (oBv[6] - i - 1)) ** 2) / (2 * p)
            xd[i] = xa1 + m * kd[i] / p - (f / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            yd[i] = ya1 + f * kd[i] / p + (m / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("xa" + str(i), f'{xa[i]:.3f}')
            txt_ss = txt_ss.replace("ya" + str(i), f'{ya[i]:.3f}')
            txt_ss = txt_ss.replace("xb" + str(i), f'{xb[i]:.3f}')
            txt_ss = txt_ss.replace("yb" + str(i), f'{yb[i]:.3f}')
            txt_ss = txt_ss.replace("xc" + str(i), f'{xc[i]:.3f}')
            txt_ss = txt_ss.replace("yc" + str(i), f'{yc[i]:.3f}')
            txt_ss = txt_ss.replace("xd" + str(i), f'{xd[i]:.3f}')
            txt_ss = txt_ss.replace("yd" + str(i), f'{yd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), str(RAMY + oBv[3] - (i + 1)))
            txt_ss = txt_ss.replace("pb" + str(i), str(RAMY + oBv[4] - (i + 1)))
            txt_ss = txt_ss.replace("pc" + str(i), str(RAMY + oBv[5] - (i + 1)))
            txt_ss = txt_ss.replace("pd" + str(i), str(RAMY + oBv[6] - (i + 1)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/56/xl_st.txt', 'r').read()
        RAMX, RAMY, rRr1, tx0 = 113, 44.5, 21.5, 36.3
        RAMK = RAMY + (int(dlina) - 305) * 0.125 if int(dlina) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMY - tx0
        ty1 = (int(dlina) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMY + rRr2, RAMK, int(dlina) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        if oBv[0] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h0", str(RAMX + oBv[0]))
            txt_ss = txt_ss.replace("RAM0", str(RAMK))
        if oBv[1] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h1", str(RAMX + oBv[1]))
            txt_ss = txt_ss.replace("RAM1", str(RAMK))
        if oBv[2] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h2", str(RAMX + oBv[2]))
            txt_ss = txt_ss.replace("RAM2", str(RAMK))
        if oBv[3] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h3", str(RAMX + oBv[3]))
            txt_ss = txt_ss.replace("RAM3", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("ha" + str(i), str(RAMX + oBv[3] - (i + 1)))
        if oBv[4] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h4", str(RAMX + oBv[4]))
            txt_ss = txt_ss.replace("RAM4", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hb" + str(i), str(RAMX + oBv[4] - (i + 1)))
        if oBv[5] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h5", str(RAMX + oBv[5]))
            txt_ss = txt_ss.replace("RAM5", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hc" + str(i), str(RAMX + oBv[5] - (i + 1)))
        if oBv[6] + RAMY < RAMK:
            txt_ss = txt_ss.replace("h6", str(RAMX + oBv[6]))
            txt_ss = txt_ss.replace("RAM6", str(RAMK))
            for i in range(10):
                txt_ss = txt_ss.replace("hd" + str(i), str(RAMX + oBv[6] - (i + 1)))

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            if int(dlina) < 253:
                korx[2] = 91.5 + ((rRr1 + oBv[2]) ** 2 - ((int(dlina) - 89) / 2) ** 2) ** 0.5
                kory[2] = int(dlina) / 2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (RAMY + oBv[3] - i - 1 - RAMK) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (RAMY + oBv[4] - i - 1 - RAMK) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (RAMY + oBv[5] - i - 1 - RAMK) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (RAMY + oBv[6] - i - 1 - RAMK) ** 2) ** 0.5
            ka[i] = (p ** 2 + (rRr1 + (oBv[3] - i - 1)) ** 2 - (rRr2 - (oBv[3] - i - 1)) ** 2) / (2 * p)
            xa[i] = xa1 + m * ka[i] / p - (f / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            ya[i] = ya1 + f * ka[i] / p + (m / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            kb[i] = (p ** 2 + (rRr1 + (oBv[4] - i - 1)) ** 2 - (rRr2 - (oBv[4] - i - 1)) ** 2) / (2 * p)
            xb[i] = xa1 + m * kb[i] / p - (f / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            yb[i] = ya1 + f * kb[i] / p + (m / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            kc[i] = (p ** 2 + (rRr1 + (oBv[5] - i - 1)) ** 2 - (rRr2 - (oBv[5] - i - 1)) ** 2) / (2 * p)
            xc[i] = xa1 + m * kc[i] / p - (f / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            yc[i] = ya1 + f * kc[i] / p + (m / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            kd[i] = (p ** 2 + (rRr1 + (oBv[6] - i - 1)) ** 2 - (rRr2 - (oBv[6] - i - 1)) ** 2) / (2 * p)
            xd[i] = xa1 + m * kd[i] / p - (f / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            yd[i] = ya1 + f * kd[i] / p + (m / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("xa" + str(i), f'{xa[i]:.3f}')
            txt_ss = txt_ss.replace("ya" + str(i), f'{ya[i]:.3f}')
            txt_ss = txt_ss.replace("xb" + str(i), f'{xb[i]:.3f}')
            txt_ss = txt_ss.replace("yb" + str(i), f'{yb[i]:.3f}')
            txt_ss = txt_ss.replace("xc" + str(i), f'{xc[i]:.3f}')
            txt_ss = txt_ss.replace("yc" + str(i), f'{yc[i]:.3f}')
            txt_ss = txt_ss.replace("xd" + str(i), f'{xd[i]:.3f}')
            txt_ss = txt_ss.replace("yd" + str(i), f'{yd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), str(RAMY + oBv[3] - (i + 1)))
            txt_ss = txt_ss.replace("pb" + str(i), str(RAMY + oBv[4] - (i + 1)))
            txt_ss = txt_ss.replace("pc" + str(i), str(RAMY + oBv[5] - (i + 1)))
            txt_ss = txt_ss.replace("pd" + str(i), str(RAMY + oBv[6] - (i + 1)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and int(visota) >= 196:
        txt_ss = open('rs/56/but.txt', 'r').read()
        RAMX, RAMY, RAMZ, rRr1, tx0 = 113, 29.5, 44.5, 21.5, 36.3
        RAMK = RAMY + (int(visota) - 305) * 0.125 if int(visota) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMZ - tx0
        ty1 = (int(visota) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMZ + rRr2, RAMK, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            if int(visota) < 253:
                korx[2] = 91.5 + ((rRr1 + oBv[2]) ** 2 - ((int(visota) - 89) / 2) ** 2) ** 0.5
                kory[2] = int(visota) / 2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (RAMY + oBv[3] - i - 1 - RAMK) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (RAMY + oBv[4] - i - 1 - RAMK) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (RAMY + oBv[5] - i - 1 - RAMK) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (RAMY + oBv[6] - i - 1 - RAMK) ** 2) ** 0.5
            ka[i] = (p ** 2 + (rRr1 + (oBv[3] - i - 1)) ** 2 - (rRr2 - (oBv[3] - i - 1)) ** 2) / (2 * p)
            xa[i] = xa1 + m * ka[i] / p - (f / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            ya[i] = ya1 + f * ka[i] / p + (m / p) * ((rRr1 + (oBv[3] - i - 1)) ** 2 - ka[i] ** 2) ** 0.5
            kb[i] = (p ** 2 + (rRr1 + (oBv[4] - i - 1)) ** 2 - (rRr2 - (oBv[4] - i - 1)) ** 2) / (2 * p)
            xb[i] = xa1 + m * kb[i] / p - (f / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            yb[i] = ya1 + f * kb[i] / p + (m / p) * ((rRr1 + (oBv[4] - i - 1)) ** 2 - kb[i] ** 2) ** 0.5
            kc[i] = (p ** 2 + (rRr1 + (oBv[5] - i - 1)) ** 2 - (rRr2 - (oBv[5] - i - 1)) ** 2) / (2 * p)
            xc[i] = xa1 + m * kc[i] / p - (f / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            yc[i] = ya1 + f * kc[i] / p + (m / p) * ((rRr1 + (oBv[5] - i - 1)) ** 2 - kc[i] ** 2) ** 0.5
            kd[i] = (p ** 2 + (rRr1 + (oBv[6] - i - 1)) ** 2 - (rRr2 - (oBv[6] - i - 1)) ** 2) / (2 * p)
            xd[i] = xa1 + m * kd[i] / p - (f / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5
            yd[i] = ya1 + f * kd[i] / p + (m / p) * ((rRr1 + (oBv[6] - i - 1)) ** 2 - kd[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("xa" + str(i), f'{xa[i]:.3f}')
            txt_ss = txt_ss.replace("ya" + str(i), f'{ya[i]:.3f}')
            txt_ss = txt_ss.replace("xb" + str(i), f'{xb[i]:.3f}')
            txt_ss = txt_ss.replace("yb" + str(i), f'{yb[i]:.3f}')
            txt_ss = txt_ss.replace("xc" + str(i), f'{xc[i]:.3f}')
            txt_ss = txt_ss.replace("yc" + str(i), f'{yc[i]:.3f}')
            txt_ss = txt_ss.replace("xd" + str(i), f'{xd[i]:.3f}')
            txt_ss = txt_ss.replace("yd" + str(i), f'{yd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), str(RAMY + oBv[3] - (i + 1)))
            txt_ss = txt_ss.replace("pb" + str(i), str(RAMY + oBv[4] - (i + 1)))
            txt_ss = txt_ss.replace("pc" + str(i), str(RAMY + oBv[5] - (i + 1)))
            txt_ss = txt_ss.replace("pd" + str(i), str(RAMY + oBv[6] - (i + 1)))
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and 160 < int(visota) < 196:
        txt_ss = open('rs/56/butsl.txt', 'r').read()
        RAMX, RAMY, RAMZ, rRr1, tx0, oBv[0] = 113, 29.5, 44.5, 21.5, 36.3, 17
        RAMK = RAMY + (int(visota) - 305) * 0.125 if int(visota) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMZ - tx0
        ty1 = (int(visota) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMZ + rRr2, RAMK, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5


            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Бутыл.' and 140 <= int(visota) <= 160:
        txt_ss = open('rs/56/butsl2.txt', 'r').read()
        RAMX, RAMY, RAMZ, rRr1, tx0, oBv[0] = 113, 29.5, 44.5, 21.5, 36.3, 17
        RAMK = RAMY + (int(visota) - 305) * 0.125 if int(visota) > 305 else RAMY + 0.001
        ty0 = (rRr1 ** 2 - (tx0 - rRr1) ** 2) ** 0.5
        tx1 = RAMX - RAMZ - tx0
        ty1 = (int(visota) - 2 * RAMK - 2 * ty0) / 2
        rRr2 = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX - rRr1
        xa2, ya1, ya2 = RAMZ + rRr2, RAMK, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5

        for i in range(10):
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            ko[i] = (p ** 2 + (rRr1 + oBv[i]) ** 2 - (rRr2 - oBv[i]) ** 2) / (2 * p)
            korx[i] = xa1 + m * ko[i] / p - (f / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5
            kory[i] = ya1 + f * ko[i] / p + (m / p) * ((rRr1 + oBv[i]) ** 2 - ko[i] ** 2) ** 0.5

            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("korx" + str(i), f'{korx[i]:.3f}')
            txt_ss = txt_ss.replace("kory" + str(i), f'{kory[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAM" + str(i), str(RAMY + 0.001 + oBv[i]))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("Kant", Kant)


    elif (k[7] == 'Бутыл.' and int(visota) < 140) or\
        (k[7] == 'ПСЯ' and int(visota) < 120) or k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss