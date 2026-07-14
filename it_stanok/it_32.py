def it_32(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/32_it/f.txt', 'r').read()
        RAMX, RAMY, RAMK = 105, 73, 35.36 + int(visota) * 0.18
        ty1 = (int(visota) - 2 * RAMK) / 2
        tx1 = RAMX - RAMY
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = int(visota) / 2 - ((rRr2 - rRr1) ** 2 - (rRr2 - rRr1 - tx1) ** 2) ** 0.5
        x1, x2, y1, y2 = rRr2 + RAMY, 63.23, int(visota) / 2, int(visota) / 2
        m1, f1 = x2 - x1, y2 - y1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rRr2 - rRr1) ** 2 - 65.7694 ** 2) / (2 * p1)
        korx = x1 + m1 * k1 / p1 - (f1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5
        kory = y1 + f1 * k1 / p1 + (m1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5

        x1, x2, y1, y2 = RAMX, RAMY + rRr2, RAMY, int(visota) / 2
        m, f = x2 - x1, y2 - y1
        p = (m ** 2 + f ** 2) ** 0.5
        k = (p ** 2 + rRr1 ** 2 - (rRr2 + rRr1) ** 2) / (2 * p)
        korx2 = x1 + m * k / p - (f / p) * (rRr1 ** 2 - k ** 2) ** 0.5
        kory2 = y1 + f * k / p + (m / p) * (rRr1 ** 2 - k ** 2) ** 0.5

        if kory2 <= RAMY:
            h2, xkor, ykor = kory2 + 0.001, korx2, kory2
        else:
            h2 = int(visota) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
            xkor, ykor = RAMX - rRr1, RAMY

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('korx', str(round(korx, 3)))
        txt_ss = txt_ss.replace('kory', str(round(kory, 3)))
        txt_ss = txt_ss.replace('xkor', str(round(xkor, 3)))
        txt_ss = txt_ss.replace('ykor', str(round(ykor, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace('h2', str(round(h2, 3)))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/32_it/st.txt', 'r').read()
        RAMX, RAMY, RAMK = 105, 73, 35.36 + int(visota) * 0.18
        ty1 = (int(visota) - 2 * RAMK) / 2
        tx1 = RAMX - RAMY
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = int(visota) / 2 - ((rRr2 - rRr1) ** 2 - (rRr2 - rRr1 - tx1) ** 2) ** 0.5
        x1, x2, y1, y2 = rRr2 + RAMY, 63.23, int(visota) / 2, int(visota) / 2
        m1, f1 = x2 - x1, y2 - y1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rRr2 - rRr1) ** 2 - 65.7694 ** 2) / (2 * p1)
        korx = x1 + m1 * k1 / p1 - (f1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5
        kory = y1 + f1 * k1 / p1 + (m1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5

        x1, x2, y1, y2 = RAMX, RAMY + rRr2, RAMY, int(visota) / 2
        m, f = x2 - x1, y2 - y1
        p = (m ** 2 + f ** 2) ** 0.5
        k = (p ** 2 + rRr1 ** 2 - (rRr2 + rRr1) ** 2) / (2 * p)
        korx2 = x1 + m * k / p - (f / p) * (rRr1 ** 2 - k ** 2) ** 0.5
        kory2 = y1 + f * k / p + (m / p) * (rRr1 ** 2 - k ** 2) ** 0.5

        if kory2 <= RAMY:
            h2, xkor, ykor = kory2 + 0.001, korx2, kory2
        else:
            h2 = int(visota) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
            xkor, ykor = RAMX - rRr1, RAMY

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('korx', str(round(korx, 3)))
        txt_ss = txt_ss.replace('kory', str(round(kory, 3)))
        txt_ss = txt_ss.replace('xkor', str(round(xkor, 3)))
        txt_ss = txt_ss.replace('ykor', str(round(ykor, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace('h2', str(round(h2, 3)))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/32_it/xl.txt', 'r').read()
        RAMX, RAMY, RAMK = 105, 73, 35.36 + int(dlina) * 0.18
        ty1 = (int(dlina) - 2 * RAMK) / 2
        tx1 = RAMX - RAMY
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = int(dlina) / 2 - ((rRr2 - rRr1) ** 2 - (rRr2 - rRr1 - tx1) ** 2) ** 0.5
        h2 = int(dlina) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
        x1, x2, y1, y2 = rRr2 + RAMY, 63.23, int(dlina) / 2, int(dlina) / 2
        m1, f1 = x2 - x1, y2 - y1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rRr2 - rRr1) ** 2 - 65.7694 ** 2) / (2 * p1)
        korx = x1 + m1 * k1 / p1 - (f1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5
        kory = y1 + f1 * k1 / p1 + (m1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('korx', str(round(korx, 3)))
        txt_ss = txt_ss.replace('kory', str(round(kory, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace('h2', str(round(h2, 3)))

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/32_it/xlst.txt', 'r').read()
        RAMX, RAMY, RAMK = 105, 73, 35.36 + int(dlina) * 0.18
        ty1 = (int(dlina) - 2 * RAMK) / 2
        tx1 = RAMX - RAMY
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        h1 = int(dlina) / 2 - ((rRr2 - rRr1) ** 2 - (rRr2 - rRr1 - tx1) ** 2) ** 0.5
        h2 = int(dlina) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
        x1, x2, y1, y2 = rRr2 + RAMY, 63.23, int(dlina) / 2, int(dlina) / 2
        m1, f1 = x2 - x1, y2 - y1
        p1 = (m1 ** 2 + f1 ** 2) ** 0.5
        k1 = (p1 ** 2 + (rRr2 - rRr1) ** 2 - 65.7694 ** 2) / (2 * p1)
        korx = x1 + m1 * k1 / p1 - (f1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5
        kory = y1 + f1 * k1 / p1 + (m1 / p1) * ((rRr2 - rRr1) ** 2 - k1 ** 2) ** 0.5


        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('korx', str(round(korx, 3)))
        txt_ss = txt_ss.replace('kory', str(round(kory, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))
        txt_ss = txt_ss.replace('h2', str(round(h2, 3)))

    elif (k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146) or k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    elif k[7] == 'ПСЯ':
        txt_ss = open('rs/32_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK, RAML = 73, 49, 27.56 + int(visota) * 0.18, 58
        ty1 = (int(visota) - 2 * RAMK) / 2
        tx1 = RAMX - RAML
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        x1, x2, y1, y2 = RAMX, RAML + rRr2, RAMY, int(visota) / 2
        m, f = x2 - x1, y2 - y1
        p = (m ** 2 + f ** 2) ** 0.5
        k = (p ** 2 + rRr1 ** 2 - (rRr2 + rRr1) ** 2) / (2 * p)
        korx = x1 + m * k / p - (f / p) * (rRr1 ** 2 - k ** 2) ** 0.5
        kory = y1 + f * k / p + (m / p) * (rRr1 ** 2 - k ** 2) ** 0.5

        if kory <= RAMY:
            h1, xkor, ykor = kory + 0.001, korx, kory
        else:
            h1 = int(visota) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
            xkor, ykor = (RAMX - rRr1), RAMY

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('xkor', str(round(xkor, 3)))
        txt_ss = txt_ss.replace('ykor', str(round(ykor, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))

    elif k[7] == 'Бутыл.':
        txt_ss = open('rs/32_it/ps.txt', 'r').read()
        RAMX, RAMY, RAMK, RAML = 105, 49, 27.56 + int(visota) * 0.18, 90
        ty1 = (int(visota) - 2 * RAMK) / 2
        tx1 = RAMX - RAML
        rRr1, rRr2 = 30, (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        x1, x2, y1, y2 = RAMX, RAML + rRr2, RAMY, int(visota) / 2
        m, f = x2 - x1, y2 - y1
        p = (m ** 2 + f ** 2) ** 0.5
        k = (p ** 2 + rRr1 ** 2 - (rRr2 + rRr1) ** 2) / (2 * p)
        korx = x1 + m * k / p - (f / p) * (rRr1 ** 2 - k ** 2) ** 0.5
        kory = y1 + f * k / p + (m / p) * (rRr1 ** 2 - k ** 2) ** 0.5

        if kory <= RAMY:
            h1, xkor, ykor = kory + 0.001, korx, kory
        else:
            h1 = int(visota) / 2 - ((rRr2 + rRr1) ** 2 - (rRr2 + rRr1 - tx1) ** 2) ** 0.5
            xkor, ykor = (RAMX - rRr1), RAMY

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('rRr1', str(rRr1))
        txt_ss = txt_ss.replace('rRr2', str(round(rRr2, 3)))
        txt_ss = txt_ss.replace('tx1', str(round(tx1, 3)))
        txt_ss = txt_ss.replace('ty1', str(round(ty1, 3)))
        txt_ss = txt_ss.replace('xkor', str(round(xkor, 3)))
        txt_ss = txt_ss.replace('ykor', str(round(ykor, 3)))
        txt_ss = txt_ss.replace('h1', str(round(h1, 3)))

    return txt_ss
