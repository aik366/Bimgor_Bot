from ss_stanok import ss_63


def ss_54(k, dlina, visota, RAM):
    if k[7] == 'ПСЯ':
        return ss_63.ss_63(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 12, 27.5, 6]
    oBz = [0, 0, 0, oBv[3] - 10, oBv[4] - 10, oBv[5] - 10, oBv[6] - 10, 0, 0, 0]
    Kant = '10.4' if k[5] == '18' else '14.8'
    h, g, n, bxo, byo, RAZ, ux = [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10
    ha, hb, hc, hd, pa, pb, pc = [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10
    uy, zy, zx, bxz, byz, pd = [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10

    if k[7] == 'Фасад' and int(visota) >= 266:
        txt_ss = open('rs/54/f.txt', 'r').read()
        RAMX, RAMY = 74, 44.5
        BRAMX = 74 - (320 - int(visota)) * 0.2 if int(visota) <= 320 else 74

        if int(visota) <= 320:
            rad1 = 60 - (320 - int(visota)) * 0.2
            RAMK = int(visota) * 0.025 + 58.5
            xb1 = 14
            xb2 = 95.9507 - (320 - int(visota)) * 0.2
        elif 320 < int(visota) <= 380:
            rad1 = 57.35 + (int(visota) - 320) * 0.35
            RAMK = 66.1 + (int(visota) - 320) * 0.04
            xb1 = 16.65 - (int(visota) - 320) * 0.35
            xb2 = 93.3554 + (int(visota) - 320) * 0.47
        else:
            rad1 = 78.35 + (int(visota) - 380) * 0.75
            RAMK = 69.14 + (int(visota) - 380) * 0.08
            xb1 = -4.35 - (int(visota) - 380) * 0.75
            xb2 = 118.9379 + (int(visota) - 380) * 0.36

        if int(visota) >= 380:
            rRr1 = (int(visota) - 380) * 0.087 + 23.521
            rRr2 = (int(visota) - 380) * 0.202 + 52.566
        elif 329 < int(visota) < 380:
            rRr1 = (int(visota) - 330) * 0.087 + 20.65
            rRr2 = (int(visota) - 330) * 0.07 + 52.5
        elif 265 < int(visota) <= 330:
            rRr1 = 24
            rRr2 = 56
        else:
            rRr1 = 18
            rRr2 = 40
            txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

        if int(visota) > 430:
            sin22 = 0.210148 - (int(visota) - 430) * 0.000144
        elif 380 <= int(visota) <= 430:
            sin22 = 0.234242 - (int(visota) - 380) * 0.000452
        elif 330 <= int(visota) < 380:
            sin22 = 0.26997 - (int(visota) - 330) * 0.000454
        elif int(visota) < 330:
            sin22 = 0.8217 - (int(visota) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(visota) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(visota) / 2 - my1) / sin22) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5
        my2 = int(visota) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (oBv[3] - i - 1) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (oBv[4] - i - 1) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (oBv[5] - i - 1) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (oBv[6] - i - 1) ** 2) ** 0.5
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), f'{(RAMY + oBv[3] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pb" + str(i), f'{(RAMY + oBv[4] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pc" + str(i), f'{(RAMY + oBv[5] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pd" + str(i), f'{(RAMY + oBv[6] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        xa1, ya1 = RAMX - rRr1, RAMY
        xa2, ya2 = mx1 - ((rRr2 + rRr3) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ko = (p ** 2 + (rRr1 + oBv[2]) ** 2 - (rRr3 + oBv[2]) ** 2) / (2 * p)
        korx = xa1 + m * ko / p + (f / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        kory = ya1 + f * ko / p - (m / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        XRAM0 = korx if mx1 < (RAMX - tx0 + ux[2]) else RAMX - tx0 + ux[2]
        YRAM0 = kory if mx1 < (RAMX - tx0 + ux[2]) else RAMY + ty0 + uy[2]
        XRAM1 = korx + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else mx1 - zx[2]
        YRAM1 = kory + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else my1 - zy[2]

        yb1, rad2 = RAMK, xb2 - RAMY
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(visota) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 + m0 * k0 / p0 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5
        bxz[4] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[4]) ** 2 - k0 ** 2) ** 0.5
        bxz[5] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[5]) ** 2 - k0 ** 2) ** 0.5
        bxz[6] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[6]) ** 2 - k0 ** 2) ** 0.5
        byz[0] = yb2 + f0 * k0 / p0 + (m0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[1] = (xb2 - bxz[0]) / (6 + rad2 - oBv[1]) * 6 + bxz[0]
        byz[1] = (int(visota) - yb2 - int(visota) / 2) / (6 + rad2 - oBv[1]) * 6 + int(visota) / 2
        m1, f1 = bxz[0] - xb1, int(visota) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(visota) - yb2 - int(visota) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(visota) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        if int(visota) < 347:
            txt_ss = txt_ss.replace("w-byz8", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz8", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("bxo2", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("byo2", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz2", '@0.001')
            txt_ss = txt_ss.replace("byz2", '@0.001')
            txt_ss = txt_ss.replace("bxo8", '@0.001')
            txt_ss = txt_ss.replace("byo8", '@0.001')

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            if RAMK <= RAMY + oBv[i]:
                RAZ[i] = 0.001
            else:
                RAZ[i] = RAMK - RAMY - oBv[i]
                g[i] = BRAMX + oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("XRAM0", f'{XRAM0:.3f}')
        txt_ss = txt_ss.replace("XRAM1", f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace("YRAM0", f'{YRAM0:.3f}')
        txt_ss = txt_ss.replace("YRAM1", f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/54/st.txt', 'r').read()
        RAMX, RAMY = 74, 44.5
        BRAMX = 74 - (320 - int(visota)) * 0.2 if int(visota) <= 320 else 74

        if int(visota) <= 320:
            rad1 = 60 - (320 - int(visota)) * 0.2
            RAMK = int(visota) * 0.025 + 58.5
            xb1 = 14
            xb2 = 95.9507 - (320 - int(visota)) * 0.2
        elif 320 < int(visota) <= 380:
            rad1 = 57.35 + (int(visota) - 320) * 0.35
            RAMK = 66.1 + (int(visota) - 320) * 0.04
            xb1 = 16.65 - (int(visota) - 320) * 0.35
            xb2 = 93.3554 + (int(visota) - 320) * 0.47
        else:
            rad1 = 78.35 + (int(visota) - 380) * 0.75
            RAMK = 69.14 + (int(visota) - 380) * 0.08
            xb1 = -4.35 - (int(visota) - 380) * 0.75
            xb2 = 118.9379 + (int(visota) - 380) * 0.36

        if int(visota) >= 380:
            rRr1 = (int(visota) - 380) * 0.087 + 23.521
            rRr2 = (int(visota) - 380) * 0.202 + 52.566
        elif 329 < int(visota) < 380:
            rRr1 = (int(visota) - 330) * 0.087 + 20.65
            rRr2 = (int(visota) - 330) * 0.07 + 52.5
        elif 265 < int(visota) <= 330:
            rRr1 = 24
            rRr2 = 56
        else:
            rRr1 = 18
            rRr2 = 40
            txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

        if int(visota) > 430:
            sin22 = 0.210148 - (int(visota) - 430) * 0.000144
        elif 380 <= int(visota) <= 430:
            sin22 = 0.234242 - (int(visota) - 380) * 0.000452
        elif 330 <= int(visota) < 380:
            sin22 = 0.26997 - (int(visota) - 330) * 0.000454
        elif int(visota) < 330:
            sin22 = 0.8217 - (int(visota) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(visota) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(visota) / 2 - my1) / sin22) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5
        my2 = int(visota) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (oBv[3] - i - 1) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (oBv[4] - i - 1) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (oBv[5] - i - 1) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (oBv[6] - i - 1) ** 2) ** 0.5
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), f'{(RAMY + oBv[3] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pb" + str(i), f'{(RAMY + oBv[4] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pc" + str(i), f'{(RAMY + oBv[5] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pd" + str(i), f'{(RAMY + oBv[6] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        xa1, ya1 = RAMX - rRr1, RAMY
        xa2, ya2 = mx1 - ((rRr2 + rRr3) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5, int(visota) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ko = (p ** 2 + (rRr1 + oBv[2]) ** 2 - (rRr3 + oBv[2]) ** 2) / (2 * p)
        korx = xa1 + m * ko / p + (f / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        kory = ya1 + f * ko / p - (m / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        XRAM0 = korx if mx1 < (RAMX - tx0 + ux[2]) else RAMX - tx0 + ux[2]
        YRAM0 = kory if mx1 < (RAMX - tx0 + ux[2]) else RAMY + ty0 + uy[2]
        XRAM1 = korx + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else mx1 - zx[2]
        YRAM1 = kory + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else my1 - zy[2]

        yb1, rad2 = RAMK, xb2 - RAMY
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(visota) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 + m0 * k0 / p0 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[1] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[1]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5
        bxz[4] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[4]) ** 2 - k0 ** 2) ** 0.5
        bxz[5] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[5]) ** 2 - k0 ** 2) ** 0.5
        bxz[6] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[6]) ** 2 - k0 ** 2) ** 0.5
        byz[0] = yb2 + f0 * k0 / p0 + (m0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        byz[1] = (int(visota) - yb2 - int(visota) / 2) / (6 + rad2 - oBv[1]) * 6 + int(visota) / 2
        m1, f1 = bxz[0] - xb1, int(visota) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(visota) - yb2 - int(visota) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(visota) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        if int(visota) < 347:
            txt_ss = txt_ss.replace("w-byz8", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz8", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("bxo2", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("byo2", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz2", '@0.001')
            txt_ss = txt_ss.replace("byz2", '@0.001')
            txt_ss = txt_ss.replace("bxo8", '@0.001')
            txt_ss = txt_ss.replace("byo8", '@0.001')

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            if RAMK <= RAMY + oBv[i]:
                RAZ[i] = 0.001
            else:
                RAZ[i] = RAMK - RAMY - oBv[i]
                g[i] = BRAMX + oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("XRAM0", f'{XRAM0:.3f}')
        txt_ss = txt_ss.replace("XRAM1", f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace("YRAM0", f'{YRAM0:.3f}')
        txt_ss = txt_ss.replace("YRAM1", f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))
        
    elif k[7] == 'Хлеб' and int(visota) >= 270 and int(dlina) >= 347:
        txt_ss = open('rs/54/xl.txt', 'r').read()
        RAMX, RAMY = 74, 44.5
        BRAMX = 74 - (320 - int(dlina)) * 0.2 if int(dlina) <= 320 else 74

        if int(dlina) <= 320:
            rad1 = 60 - (320 - int(dlina)) * 0.2
            RAMK = int(dlina) * 0.025 + 58.5
            xb1 = 14
            xb2 = 95.9507 - (320 - int(dlina)) * 0.2
        elif 320 < int(dlina) <= 380:
            rad1 = 57.35 + (int(dlina) - 320) * 0.35
            RAMK = 66.1 + (int(dlina) - 320) * 0.04
            xb1 = 16.65 - (int(dlina) - 320) * 0.35
            xb2 = 93.3554 + (int(dlina) - 320) * 0.47
        else:
            rad1 = 78.35 + (int(dlina) - 380) * 0.75
            RAMK = 69.14 + (int(dlina) - 380) * 0.08
            xb1 = -4.35 - (int(dlina) - 380) * 0.75
            xb2 = 118.9379 + (int(dlina) - 380) * 0.36

        if int(dlina) >= 380:
            rRr1 = (int(dlina) - 380) * 0.087 + 23.521
            rRr2 = (int(dlina) - 380) * 0.202 + 52.566
        elif 329 < int(dlina) < 380:
            rRr1 = (int(dlina) - 330) * 0.087 + 20.65
            rRr2 = (int(dlina) - 330) * 0.07 + 52.5
        elif 265 < int(dlina) <= 330:
            rRr1 = 24
            rRr2 = 56
        else:
            rRr1 = 18
            rRr2 = 40
            txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

        if int(dlina) > 430:
            sin22 = 0.210148 - (int(dlina) - 430) * 0.000144
        elif 380 <= int(dlina) <= 430:
            sin22 = 0.234242 - (int(dlina) - 380) * 0.000452
        elif 330 <= int(dlina) < 380:
            sin22 = 0.26997 - (int(dlina) - 330) * 0.000454
        elif int(dlina) < 330:
            sin22 = 0.8217 - (int(dlina) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(dlina) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(dlina) / 2 - my1) / sin22) ** 2 - (int(dlina) / 2 - my1) ** 2) ** 0.5
        my2 = int(dlina) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (oBv[3] - i - 1) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (oBv[4] - i - 1) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (oBv[5] - i - 1) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (oBv[6] - i - 1) ** 2) ** 0.5
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), f'{(RAMY + oBv[3] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pb" + str(i), f'{(RAMY + oBv[4] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pc" + str(i), f'{(RAMY + oBv[5] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pd" + str(i), f'{(RAMY + oBv[6] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        xa1, ya1 = RAMX - rRr1, RAMY
        xa2, ya2 = mx1 - ((rRr2 + rRr3) ** 2 - (int(dlina) / 2 - my1) ** 2) ** 0.5, int(dlina) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ko = (p ** 2 + (rRr1 + oBv[2]) ** 2 - (rRr3 + oBv[2]) ** 2) / (2 * p)
        korx = xa1 + m * ko / p + (f / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        kory = ya1 + f * ko / p - (m / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        XRAM0 = korx if mx1 < (RAMX - tx0 + ux[2]) else RAMX - tx0 + ux[2]
        YRAM0 = kory if mx1 < (RAMX - tx0 + ux[2]) else RAMY + ty0 + uy[2]
        XRAM1 = korx + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else mx1 - zx[2]
        YRAM1 = kory + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else my1 - zy[2]

        yb1, rad2 = RAMK, xb2 - RAMY
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(dlina) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 + m0 * k0 / p0 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5
        bxz[4] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[4]) ** 2 - k0 ** 2) ** 0.5
        bxz[5] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[5]) ** 2 - k0 ** 2) ** 0.5
        bxz[6] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[6]) ** 2 - k0 ** 2) ** 0.5
        byz[0] = yb2 + f0 * k0 / p0 + (m0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[1] = (xb2 - bxz[0]) / (6 + rad2 - oBv[1]) * 6 + bxz[0]
        byz[1] = (int(dlina) - yb2 - int(dlina) / 2) / (6 + rad2 - oBv[1]) * 6 + int(dlina) / 2
        m1, f1 = bxz[0] - xb1, int(dlina) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(dlina) - yb2 - int(dlina) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(dlina) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        if int(dlina) < 347:
            txt_ss = txt_ss.replace("w-byz8", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz8", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("bxo2", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("byo2", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz2", '@0.001')
            txt_ss = txt_ss.replace("byz2", '@0.001')
            txt_ss = txt_ss.replace("bxo8", '@0.001')
            txt_ss = txt_ss.replace("byo8", '@0.001')

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            if RAMK <= RAMY + oBv[i]:
                RAZ[i] = 0.001
            else:
                RAZ[i] = RAMK - RAMY - oBv[i]
                g[i] = BRAMX + oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("XRAM0", f'{XRAM0:.3f}')
        txt_ss = txt_ss.replace("XRAM1", f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace("YRAM0", f'{YRAM0:.3f}')
        txt_ss = txt_ss.replace("YRAM1", f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))

    elif k[7] == 'Хлеб_ст' and int(visota) >= 270 and int(dlina) >= 347:
        oBv[1] = oBv[8]
        txt_ss = open('rs/54/xlst.txt', 'r').read()
        RAMX, RAMY = 74, 44.5
        BRAMX = 74 - (320 - int(dlina)) * 0.2 if int(dlina) <= 320 else 74

        if int(dlina) <= 320:
            rad1 = 60 - (320 - int(dlina)) * 0.2
            RAMK = int(dlina) * 0.025 + 58.5
            xb1 = 14
            xb2 = 95.9507 - (320 - int(dlina)) * 0.2
        elif 320 < int(dlina) <= 380:
            rad1 = 57.35 + (int(dlina) - 320) * 0.35
            RAMK = 66.1 + (int(dlina) - 320) * 0.04
            xb1 = 16.65 - (int(dlina) - 320) * 0.35
            xb2 = 93.3554 + (int(dlina) - 320) * 0.47
        else:
            rad1 = 78.35 + (int(dlina) - 380) * 0.75
            RAMK = 69.14 + (int(dlina) - 380) * 0.08
            xb1 = -4.35 - (int(dlina) - 380) * 0.75
            xb2 = 118.9379 + (int(dlina) - 380) * 0.36

        if int(dlina) >= 380:
            rRr1 = (int(dlina) - 380) * 0.087 + 23.521
            rRr2 = (int(dlina) - 380) * 0.202 + 52.566
        elif 329 < int(dlina) < 380:
            rRr1 = (int(dlina) - 330) * 0.087 + 20.65
            rRr2 = (int(dlina) - 330) * 0.07 + 52.5
        elif 265 < int(dlina) <= 330:
            rRr1 = 24
            rRr2 = 56
        else:
            rRr1 = 18
            rRr2 = 40
            txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

        if int(dlina) > 430:
            sin22 = 0.210148 - (int(dlina) - 430) * 0.000144
        elif 380 <= int(dlina) <= 430:
            sin22 = 0.234242 - (int(dlina) - 380) * 0.000452
        elif 330 <= int(dlina) < 380:
            sin22 = 0.26997 - (int(dlina) - 330) * 0.000454
        elif int(dlina) < 330:
            sin22 = 0.8217 - (int(dlina) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(dlina) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(dlina) / 2 - my1) / sin22) ** 2 - (int(dlina) / 2 - my1) ** 2) ** 0.5
        my2 = int(dlina) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (oBv[3] - i - 1) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (oBv[4] - i - 1) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (oBv[5] - i - 1) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (oBv[6] - i - 1) ** 2) ** 0.5
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), f'{(RAMY + oBv[3] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pb" + str(i), f'{(RAMY + oBv[4] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pc" + str(i), f'{(RAMY + oBv[5] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pd" + str(i), f'{(RAMY + oBv[6] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        xa1, ya1 = RAMX - rRr1, RAMY
        xa2, ya2 = mx1 - ((rRr2 + rRr3) ** 2 - (int(dlina) / 2 - my1) ** 2) ** 0.5, int(dlina) / 2
        m, f = xa2 - xa1, ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ko = (p ** 2 + (rRr1 + oBv[2]) ** 2 - (rRr3 + oBv[2]) ** 2) / (2 * p)
        korx = xa1 + m * ko / p + (f / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        kory = ya1 + f * ko / p - (m / p) * ((rRr1 + oBv[2]) ** 2 - ko ** 2) ** 0.5
        XRAM0 = korx if mx1 < (RAMX - tx0 + ux[2]) else RAMX - tx0 + ux[2]
        YRAM0 = kory if mx1 < (RAMX - tx0 + ux[2]) else RAMY + ty0 + uy[2]
        XRAM1 = korx + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else mx1 - zx[2]
        YRAM1 = kory + 0.001 if mx1 < (RAMX - tx0 + ux[2]) else my1 - zy[2]

        yb1, rad2 = RAMK, xb2 - RAMY
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(dlina) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 + m0 * k0 / p0 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[1] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[1]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5
        bxz[4] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[4]) ** 2 - k0 ** 2) ** 0.5
        bxz[5] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[5]) ** 2 - k0 ** 2) ** 0.5
        bxz[6] = xb2 + m0 * k0 / p0 - (f0 / p0) * ((rad2 - oBv[6]) ** 2 - k0 ** 2) ** 0.5
        byz[0] = yb2 + f0 * k0 / p0 + (m0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        byz[1] = (int(dlina) - yb2 - int(dlina) / 2) / (6 + rad2 - oBv[1]) * 6 + int(dlina) / 2
        m1, f1 = bxz[0] - xb1, int(dlina) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(dlina) - yb2 - int(dlina) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(dlina) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        if int(dlina) < 347:
            txt_ss = txt_ss.replace("w-byz8", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz8", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("bxo2", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("byo2", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz2", '@0.001')
            txt_ss = txt_ss.replace("byz2", '@0.001')
            txt_ss = txt_ss.replace("bxo8", '@0.001')
            txt_ss = txt_ss.replace("byo8", '@0.001')

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            if RAMK <= RAMY + oBv[i]:
                RAZ[i] = 0.001
            else:
                RAZ[i] = RAMK - RAMY - oBv[i]
                g[i] = BRAMX + oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("XRAM0", f'{XRAM0:.3f}')
        txt_ss = txt_ss.replace("XRAM1", f'{XRAM1:.3f}')
        txt_ss = txt_ss.replace("YRAM0", f'{YRAM0:.3f}')
        txt_ss = txt_ss.replace("YRAM1", f'{YRAM1:.3f}')
        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))

    elif k[7] == 'Бутыл.' and int(visota) >= 179:
        txt_ss = open('rs/54/but.txt', 'r').read()
        oBv[1] = oBv[0]
        RAMX, RAMY = 74, 22.5
        if int(visota) <= 270:
            BRAMX = 72 - (270 - int(visota)) * 0.15
        elif 270 < int(visota) <= 320:
            BRAMX = 74 - (320 - int(visota)) * 0.2
        else:
            BRAMX = 74

        if int(visota) <= 320:
            rad1 = 60 - (320 - int(visota)) * 0.2
        elif 320 < int(visota) <= 380:
            rad1 = 57.35 + (int(visota) - 320) * 0.35
        else:
            rad1 = 78.35 + (int(visota) - 380) * 0.75

        if int(visota) < 242:
            RAMK = int(visota) * 0.025 + 27
            xb2 = 96 - (241 - int(visota)) * 0.1
        elif 242 <= int(visota) < 270:
            RAMK = int(visota) * 0.025 + 34
            xb2 = 100.3155 - (270 - int(visota)) * 0.3122
        elif 270 < int(visota) <= 320:
            RAMK = int(visota) * 0.025 + 58.5
            xb2 = 99 - (320 - int(visota)) * 0.2
        elif 320 < int(visota) <= 380:
            RAMK = 66.1 + (int(visota) - 320) * 0.04
            xb2 = 93.3554 + (int(visota) - 320) * 0.47
        else:
            RAMK = 69.14 + (int(visota) - 380) * 0.08
            xb2 = 118.9379 + (int(visota) - 380) * 0.36

        xb1 = BRAMX - rad1
        rRr1, rRr2 = 18, 35
        sin22 = 0.8217 - (int(visota) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(visota) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(visota) / 2 - my1) / sin22) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5
        my2 = int(visota) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            ha[i] = RAMX - rRr1 + ((rRr1 + (oBv[3] - i - 1)) ** 2 - (oBv[3] - i - 1) ** 2) ** 0.5
            hb[i] = RAMX - rRr1 + ((rRr1 + (oBv[4] - i - 1)) ** 2 - (oBv[4] - i - 1) ** 2) ** 0.5
            hc[i] = RAMX - rRr1 + ((rRr1 + (oBv[5] - i - 1)) ** 2 - (oBv[5] - i - 1) ** 2) ** 0.5
            hd[i] = RAMX - rRr1 + ((rRr1 + (oBv[6] - i - 1)) ** 2 - (oBv[6] - i - 1) ** 2) ** 0.5
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("ha" + str(i), f'{ha[i]:.3f}')
            txt_ss = txt_ss.replace("hb" + str(i), f'{hb[i]:.3f}')
            txt_ss = txt_ss.replace("hc" + str(i), f'{hc[i]:.3f}')
            txt_ss = txt_ss.replace("hd" + str(i), f'{hd[i]:.3f}')
            txt_ss = txt_ss.replace("pa" + str(i), f'{(RAMY + oBv[3] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pb" + str(i), f'{(RAMY + oBv[4] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pc" + str(i), f'{(RAMY + oBv[5] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("pd" + str(i), f'{(RAMY + oBv[6] - (i + 1)):.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        yb1, rad2 = RAMK, xb2 - 44.5
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(visota) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5
        bxz[4] = xb2 - (f0 / p0) * ((rad2 - oBv[4]) ** 2 - k0 ** 2) ** 0.5
        bxz[5] = xb2 - (f0 / p0) * ((rad2 - oBv[5]) ** 2 - k0 ** 2) ** 0.5
        bxz[6] = xb2 - (f0 / p0) * ((rad2 - oBv[6]) ** 2 - k0 ** 2) ** 0.5
        byz[0] = yb2 + f0 * k0 / p0
        bxz[1] = (xb2 - bxz[6]) / (7.2 + rad2 - oBv[1]) * 7.2 + bxz[6]
        byz[1] = (int(visota) - yb2 - int(visota) / 2) / (7.2 + rad2 - oBv[1]) * 7.2 + int(visota) / 2
        m1, f1 = bxz[0] - xb1, int(visota) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(visota) - yb2 - int(visota) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(visota) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        if int(visota) < 347:
            txt_ss = txt_ss.replace("w-byz8", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz8", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("bxo2", f'{korx2:.3f}')
            txt_ss = txt_ss.replace("byo2", f'{kory2:.3f}')
            txt_ss = txt_ss.replace("bxz2", '@0.001')
            txt_ss = txt_ss.replace("byz2", '@0.001')
            txt_ss = txt_ss.replace("bxo8", '@0.001')
            txt_ss = txt_ss.replace("byo8", '@0.001')

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            n[i] = BRAMX - rad1 + ((rad1 + oBz[i]) ** 2 - (RAMY + oBz[i] - RAMK) ** 2) ** 0.5
            RAZ[i] = 0.001 if RAMK <= RAMY + oBv[i] else RAMK - RAMY - oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("n" + str(i), f'{n[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))

    elif k[7] == 'Бутыл.' and (140 <= int(visota) < 179):
        txt_ss = open('rs/54/butsl.txt', 'r').read()
        oBv[3] = 17
        if 140 <= int(visota) < 155:
            txt_ss = open('rs/54/butsl2.txt', 'r').read()

        if 154 < int(visota) < 195:
            BRAMX = 78 - (270 - int(visota)) * 0.15
            RAMX = 66
            xb2 = 82 - (241 - int(visota)) * 0.1
        else:
            BRAMX = 65
            RAMX = 51
            xb2 = 69 - (241 - int(visota)) * 0.1

        rad1 = 60 - (320 - int(visota)) * 0.2
        RAMK = int(visota) * 0.025 + 27
        xb1 = BRAMX - rad1
        RAMY = 29.5
        rRr1 = 19.624 - (190 - int(visota)) * 0.32
        rRr2 = 33.72 - (190 - int(visota)) * 0.26
        sin22 = 0.6 - (int(visota) * 0.0015)

        mx1 = 44.5 + rRr2
        my1 = ((rRr1 + rRr2) ** 2 - (mx1 + rRr1 - RAMX) ** 2) ** 0.5 + RAMY
        rRr3 = (int(visota) / 2 - my1) / sin22 - rRr2
        mx2 = mx1 - (((int(visota) / 2 - my1) / sin22) ** 2 - (int(visota) / 2 - my1) ** 2) ** 0.5
        my2 = int(visota) / 2
        mx3 = mx2 + (mx1 - mx2) / (rRr2 + rRr3) * rRr3
        my3 = my2 - (my2 - my1) / (rRr2 + rRr3) * rRr3
        ty0 = (my1 - RAMY) / (rRr1 + rRr2) * rRr1
        tx0 = rRr1 - (mx1 + rRr1 - RAMX) * rRr1 / (rRr1 + rRr2)

        for i in range(10):
            ux[i] = ((rRr1 - tx0) / rRr1) * oBv[i]
            uy[i] = (ty0 / rRr1) * oBv[i]
            h[i] = RAMX - rRr1 + ((rRr1 + oBv[i]) ** 2 - oBv[i] ** 2) ** 0.5
            zy[i] = (my1 - my3) * (rRr2 - oBv[i]) / rRr2
            zx[i] = (mx1 - mx3) * (rRr2 - oBv[i]) / rRr2
            txt_ss = txt_ss.replace("h" + str(i), f'{h[i]:.3f}')
            txt_ss = txt_ss.replace("ux" + str(i), f'{ux[i]:.3f}')
            txt_ss = txt_ss.replace("uy" + str(i), f'{uy[i]:.3f}')
            txt_ss = txt_ss.replace("zy" + str(i), f'{zy[i]:.3f}')
            txt_ss = txt_ss.replace("zx" + str(i), f'{zx[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))

        yb1, rad2 = RAMK, xb2 - 44.5
        yb2 = ((rad1 + rad2) ** 2 - (xb2 - xb1) ** 2) ** 0.5 + RAMK
        xb3 = (xb2 - xb1) / (rad1 + rad2) * rad1 + xb1
        yb3 = (yb2 - yb1) / (rad1 + rad2) * rad1 + yb1
        m0, f0 = 0, int(visota) - 2 * yb2
        p0 = (m0 ** 2 + f0 ** 2) ** 0.5
        k0 = (p0 ** 2 + rad2 ** 2 - rad2 ** 2) / (2 * p0)
        korx0 = xb2 - (f0 / p0) * (rad2 ** 2 - k0 ** 2) ** 0.5
        bxz[0] = xb2 - (f0 / p0) * ((rad2 - oBv[0]) ** 2 - k0 ** 2) ** 0.5
        bxz[3] = xb2 - (f0 / p0) * ((rad2 - oBv[3]) ** 2 - k0 ** 2) ** 0.5

        m1, f1 = bxz[0] - xb1, int(visota) / 2 - yb1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rad1 + oBv[2]) ** 2 - 34.5 ** 2) / (2 * p1)
        korx2 = xb1 + m1 * k1 / p1 + (f1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        kory2 = yb1 + f1 * k1 / p1 - (m1 / p1) * ((rad1 + oBv[2]) ** 2 - k1 ** 2) ** 0.5
        bxz[2] = (xb2 - bxz[0]) / (34.5 + rad2 - oBv[2]) * 34.5 + bxz[0]
        byz[2] = (int(visota) - yb2 - int(visota) / 2) / (34.5 + rad2 - oBv[2]) * 34.5 + int(visota) / 2
        byz[8], bxz[8] = byz[2], bxz[2]

        for i in range(10):
            g[i] = BRAMX - rad1 + ((rad1 + oBv[i]) ** 2 - (RAMY + oBv[i] - RAMK) ** 2) ** 0.5
            n[i] = BRAMX - rad1 + ((rad1 + oBz[i]) ** 2 - (RAMY + oBz[i] - RAMK) ** 2) ** 0.5
            RAZ[i] = 0.001 if RAMK <= RAMY + oBv[i] else RAMK - RAMY - oBv[i]
            bxo[i] = (xb2 - xb1) / (rad1 + rad2) * (rad1 + oBv[i]) + xb1
            byo[i] = (yb2 - yb1) / (rad1 + rad2) * (rad1 + oBv[i]) + yb1
            byo[8], bxo[8] = byo[2], bxo[2]
            txt_ss = txt_ss.replace("g" + str(i), f'{g[i]:.3f}')
            txt_ss = txt_ss.replace("n" + str(i), f'{n[i]:.3f}')
            txt_ss = txt_ss.replace("bxo" + str(i), f'{bxo[i]:.3f}')
            txt_ss = txt_ss.replace("byo" + str(i), f'{byo[i]:.3f}')
            txt_ss = txt_ss.replace("bxz" + str(i), f'{bxz[i]:.3f}')
            txt_ss = txt_ss.replace("byz" + str(i), f'{byz[i]:.3f}')
            txt_ss = txt_ss.replace("oBv" + str(i), str(oBv[i]))
            txt_ss = txt_ss.replace("RAZ" + str(i), f'{RAZ[i]:.3f}')

        txt_ss = txt_ss.replace("xb3", f'{xb3:.3f}')
        txt_ss = txt_ss.replace("yb3", f'{yb3:.3f}')
        txt_ss = txt_ss.replace("korx0", f'{korx0:.3f}')
        txt_ss = txt_ss.replace("rad1", f'{rad1:.3f}')
        txt_ss = txt_ss.replace("rad2", f'{rad2:.3f}')
        txt_ss = txt_ss.replace("BRAMX", str(BRAMX))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))

        txt_ss = txt_ss.replace("tx0", f'{tx0:.3f}')
        txt_ss = txt_ss.replace("ty0", f'{ty0:.3f}')
        txt_ss = txt_ss.replace("rRr1", f'{rRr1:.3f}')
        txt_ss = txt_ss.replace("rRr2", f'{rRr2:.3f}')
        txt_ss = txt_ss.replace("rRr3", f'{rRr3:.3f}')
        txt_ss = txt_ss.replace("mx1",  f'{mx1:.3f}')
        txt_ss = txt_ss.replace("mx2",  f'{mx2:.3f}')
        txt_ss = txt_ss.replace("mx3",  f'{mx3:.3f}')
        txt_ss = txt_ss.replace("my1",  f'{my1:.3f}')
        txt_ss = txt_ss.replace("my2",  f'{my2:.3f}')
        txt_ss = txt_ss.replace("my3",  f'{my3:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", str(Kant))

    elif k[7] == 'Планка' or (k[7] == 'Бутыл.' and int(visota) < 140):
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
