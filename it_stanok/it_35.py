def it_35(k, dlina, visota, RAM):
    txt_ss = ''
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/35_it/f.txt', 'r').read()

        RAMX = 120 - (280 - int(visota)) * 0.348 if int(visota) < 280 else 120
        RAMY, rRr1 = 45, 30

        if int(visota) > 247:
            rRr2 = (int(visota) - 247) * 0.21
            rRr4 = rRr2
        else:
            rRr2 = (int(visota) - 247) * 0.21
            rRr4 = 0.001

        x1 = RAMX - rRr1 - rRr2

        if int(visota) >= 397:
            tx1 = 14.4 - (int(visota) - 397) * 0.04
        elif 280 <= int(visota) < 397:
            tx1 = 23.44 - (int(visota) - 280) * 0.08
        elif int(visota) < 280:
            tx1 = 23.9295 - (280 - int(visota)) * 0.1375

        ty1 = ((rRr2 + rRr1) ** 2 - ((rRr2 + rRr1) - tx1) ** 2) ** 0.5
        tx2 = RAMX - RAMY - rRr1 - tx1
        ty2 = (int(visota) - 2 * (RAMY + rRr1 + ty1)) / 2
        rRr3 = (tx2 ** 2 + ty2 ** 2) / (2 * tx2)
        ob = 12
        h1 = x1 + ((rRr2 + rRr1 + ob) ** 2 - ob ** 2) ** 0.5
        ux1 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * (rRr1 + rRr2 + ob) + x1
        uy1 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * (rRr1 + rRr2 + ob)

        if int(visota) >= 247:
            ux2 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * rRr2 + x1
            uy2 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * rRr2
        else:
            ux2 = (RAMX - 30)
            uy2 = 75

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr3", str(round(rRr3, 3)))
        txt_ss = txt_ss.replace("rRr4", str(round(rRr4, 3)))
        txt_ss = txt_ss.replace("ux1", str(round(ux1, 3)))
        txt_ss = txt_ss.replace("ux2", str(round(ux2, 3)))
        txt_ss = txt_ss.replace("uy1", str(round(uy1, 3)))
        txt_ss = txt_ss.replace("uy2", str(round(uy2, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("x1", str(round(x1, 3)))
        txt_ss = txt_ss.replace("h1", str(round(h1, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/35_it/st.txt', 'r').read()

        RAMX = 120 - (280 - int(visota)) * 0.348 if int(visota) < 280 else 120
        RAMY, rRr1 = 45, 30

        if int(visota) > 247:
            rRr2 = (int(visota) - 247) * 0.21
            rRr4 = rRr2
        else:
            rRr2 = (int(visota) - 247) * 0.21
            rRr4 = 0.001

        x1 = RAMX - rRr1 - rRr2

        if int(visota) >= 397:
            tx1 = 14.4 - (int(visota) - 397) * 0.04
        elif 280 <= int(visota) < 397:
            tx1 = 23.44 - (int(visota) - 280) * 0.08
        elif int(visota) < 280:
            tx1 = 23.9295 - (280 - int(visota)) * 0.1375

        ty1 = ((rRr2 + rRr1) ** 2 - ((rRr2 + rRr1) - tx1) ** 2) ** 0.5
        tx2 = RAMX - RAMY - rRr1 - tx1
        ty2 = (int(visota) - 2 * (RAMY + rRr1 + ty1)) / 2
        rRr3 = (tx2 ** 2 + ty2 ** 2) / (2 * tx2)
        ob = 12
        h1 = x1 + ((rRr2 + rRr1 + ob) ** 2 - ob ** 2) ** 0.5
        ux1 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * (rRr1 + rRr2 + ob) + x1
        uy1 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * (rRr1 + rRr2 + ob)

        if int(visota) >= 247:
            ux2 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * rRr2 + x1
            uy2 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * rRr2
        else:
            ux2 = (RAMX - 30)
            uy2 = 75

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr3", str(round(rRr3, 3)))
        txt_ss = txt_ss.replace("rRr4", str(round(rRr4, 3)))
        txt_ss = txt_ss.replace("ux1", str(round(ux1, 3)))
        txt_ss = txt_ss.replace("ux2", str(round(ux2, 3)))
        txt_ss = txt_ss.replace("uy1", str(round(uy1, 3)))
        txt_ss = txt_ss.replace("uy2", str(round(uy2, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("x1", str(round(x1, 3)))
        txt_ss = txt_ss.replace("h1", str(round(h1, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] =='Хлеб':
        txt_ss = open('rs/35_it/xl.txt', 'r').read()

        RAMX = 120 - (280 - int(dlina)) * 0.348 if int(dlina) < 280 else 120
        RAMY, rRr1 = 45, 30

        if int(dlina) > 247:
            rRr2 = (int(dlina) - 247) * 0.21
            rRr4 = rRr2
        else:
            rRr2 = (int(dlina) - 247) * 0.21
            rRr4 = 0.001

        x1 = RAMX - rRr1 - rRr2

        if int(dlina) >= 397:
            tx1 = 14.4 - (int(dlina) - 397) * 0.04
        elif 280 <= int(dlina) < 397:
            tx1 = 23.44 - (int(dlina) - 280) * 0.08
        elif int(dlina) < 280:
            tx1 = 23.9295 - (280 - int(dlina)) * 0.1375

        ty1 = ((rRr2 + rRr1) ** 2 - ((rRr2 + rRr1) - tx1) ** 2) ** 0.5
        tx2 = RAMX - RAMY - rRr1 - tx1
        ty2 = (int(dlina) - 2 * (RAMY + rRr1 + ty1)) / 2
        rRr3 = (tx2 ** 2 + ty2 ** 2) / (2 * tx2)
        ob = 12
        h1 = x1 + ((rRr2 + rRr1 + ob) ** 2 - ob ** 2) ** 0.5
        ux1 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * (rRr1 + rRr2 + ob) + x1
        uy1 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * (rRr1 + rRr2 + ob)

        if int(dlina) >= 247:
            ux2 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * rRr2 + x1
            uy2 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * rRr2
        else:
            ux2 = (RAMX - 30)
            uy2 = 75

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr3", str(round(rRr3, 3)))
        txt_ss = txt_ss.replace("rRr4", str(round(rRr4, 3)))
        txt_ss = txt_ss.replace("ux1", str(round(ux1, 3)))
        txt_ss = txt_ss.replace("ux2", str(round(ux2, 3)))
        txt_ss = txt_ss.replace("uy1", str(round(uy1, 3)))
        txt_ss = txt_ss.replace("uy2", str(round(uy2, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("x1", str(round(x1, 3)))
        txt_ss = txt_ss.replace("h1", str(round(h1, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] =='Хлеб_ст':
        txt_ss = open('rs/35_it/xlst.txt', 'r').read()

        RAMX = 120 - (280 - int(dlina)) * 0.348 if int(dlina) < 280 else 120
        RAMY, rRr1 = 45, 30

        if int(dlina) > 247:
            rRr2 = (int(dlina) - 247) * 0.21
            rRr4 = rRr2
        else:
            rRr2 = (int(dlina) - 247) * 0.21
            rRr4 = 0.001

        x1 = RAMX - rRr1 - rRr2

        if int(dlina) >= 397:
            tx1 = 14.4 - (int(dlina) - 397) * 0.04
        elif 280 <= int(dlina) < 397:
            tx1 = 23.44 - (int(dlina) - 280) * 0.08
        elif int(dlina) < 280:
            tx1 = 23.9295 - (280 - int(dlina)) * 0.1375

        ty1 = ((rRr2 + rRr1) ** 2 - ((rRr2 + rRr1) - tx1) ** 2) ** 0.5
        tx2 = RAMX - RAMY - rRr1 - tx1
        ty2 = (int(dlina) - 2 * (RAMY + rRr1 + ty1)) / 2
        rRr3 = (tx2 ** 2 + ty2 ** 2) / (2 * tx2)
        ob = 12
        h1 = x1 + ((rRr2 + rRr1 + ob) ** 2 - ob ** 2) ** 0.5
        ux1 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * (rRr1 + rRr2 + ob) + x1
        uy1 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * (rRr1 + rRr2 + ob)

        if int(dlina) >= 247:
            ux2 = (RAMX - x1 - tx1) / (rRr1 + rRr2) * rRr2 + x1
            uy2 = RAMY + rRr1 + ty1 / (rRr1 + rRr2) * rRr2
        else:
            ux2 = (RAMX - 30)
            uy2 = 75

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr3", str(round(rRr3, 3)))
        txt_ss = txt_ss.replace("rRr4", str(round(rRr4, 3)))
        txt_ss = txt_ss.replace("ux1", str(round(ux1, 3)))
        txt_ss = txt_ss.replace("ux2", str(round(ux2, 3)))
        txt_ss = txt_ss.replace("uy1", str(round(uy1, 3)))
        txt_ss = txt_ss.replace("uy2", str(round(uy2, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("x1", str(round(x1, 3)))
        txt_ss = txt_ss.replace("h1", str(round(h1, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'Бутыл.' and int(visota) > 155:
        txt_ss = open('rs/35_it/but.txt', 'r').read()

        RAMY = 22 if int(visota) <= 170 else 22 + (int(visota) - 170) * 0.14
        RAMX, RAMK, ob = 90, 45, 30
        tx1 = (RAMX - RAMK - ob) / 2
        ty1 = (int(visota) - 2 * (RAMY + ob)) / 4
        rRr = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX
        ya1 = RAMY + ob
        xa2 = RAMK + rRr + ob
        ya2 = int(visota) / 2
        rRr1 = ob
        rRr2 = rRr + ob
        m = xa2 - xa1
        f = ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ks = (p ** 2 + rRr1 ** 2 - rRr2 ** 2) / (2 * p)

        if rRr <= 30:
            korx = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            korx1 = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory1 = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            fx, fy, fr, fx1, fy1 = korx, kory,  0.001, korx, kory
        else:
            korx = RAMX - ob
            kory = RAMY + ob
            korx1 = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            kory1 = ty1 / rRr * (rRr - ob) + RAMY + ob
            fr = rRr - ob
            fy = ty1 / rRr * (rRr - ob) + RAMY + ob
            fx = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            fx1 = (RAMX - ob)
            fy1 = (RAMY + ob)

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace("korx1", str(round(korx1, 3)))
        txt_ss = txt_ss.replace("kory1", str(round(kory1, 3)))
        txt_ss = txt_ss.replace("korx", str(round(korx, 3)))
        txt_ss = txt_ss.replace("kory", str(round(kory, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("fx1", str(round(fx1, 3)))
        txt_ss = txt_ss.replace("fy1", str(round(fy1, 3)))
        txt_ss = txt_ss.replace("fx", str(round(fx, 3)))
        txt_ss = txt_ss.replace("fy", str(round(fy, 3)))
        txt_ss = txt_ss.replace("fr", str(round(fr, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'Бутыл.' and 131 <= int(visota) <= 155:
        txt_ss = open('rs/35_it/butsl.txt', 'r').read()

        RAMY = 22 if int(visota) <= 170 else 22 + (int(visota) - 170) * 0.14
        RAMX, RAMK, ob = 90, 45, 30
        tx1 = (RAMX - RAMK - ob) / 2
        ty1 = (int(visota) - 2 * (RAMY + ob)) / 4
        rRr = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX
        ya1 = RAMY + ob
        xa2 = RAMK + rRr + ob
        ya2 = int(visota) / 2
        rRr1 = ob
        rRr2 = rRr + ob
        m = xa2 - xa1
        f = ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ks = (p ** 2 + rRr1 ** 2 - rRr2 ** 2) / (2 * p)

        if rRr <= 30:
            korx = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            korx1 = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory1 = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            fx, fy, fr, fx1, fy1 = korx, kory,  0.001, korx, kory
        else:
            korx = RAMX - ob
            kory = RAMY + ob
            korx1 = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            kory1 = ty1 / rRr * (rRr - ob) + RAMY + ob
            fr = rRr - ob
            fy = ty1 / rRr * (rRr - ob) + RAMY + ob
            fx = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            fx1 = (RAMX - ob)
            fy1 = (RAMY + ob)

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace("korx1", str(round(korx1, 3)))
        txt_ss = txt_ss.replace("kory1", str(round(kory1, 3)))
        txt_ss = txt_ss.replace("korx", str(round(korx, 3)))
        txt_ss = txt_ss.replace("kory", str(round(kory, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("fx1", str(round(fx1, 3)))
        txt_ss = txt_ss.replace("fy1", str(round(fy1, 3)))
        txt_ss = txt_ss.replace("fx", str(round(fx, 3)))
        txt_ss = txt_ss.replace("fy", str(round(fy, 3)))
        txt_ss = txt_ss.replace("fr", str(round(fr, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'ПСЯ' and int(visota) > 155:
        txt_ss = open('rs/30_it/ps.txt', 'r').read()

        RAMY = 22 if int(visota) <= 170 else 22 + (int(visota) - 170) * 0.14
        RAMX, RAMK, ob = 90, 45, 30
        tx1 = (RAMX - RAMK - ob) / 2
        ty1 = (int(visota) - 2 * (RAMY + ob)) / 4
        rRr = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX
        ya1 = RAMY + ob
        xa2 = RAMK + rRr + ob
        ya2 = int(visota) / 2
        rRr1 = ob
        rRr2 = rRr + ob
        m = xa2 - xa1
        f = ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ks = (p ** 2 + rRr1 ** 2 - rRr2 ** 2) / (2 * p)

        if rRr <= 30:
            korx = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            korx1 = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory1 = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            fx, fy, fr, fx1, fy1 = korx, kory,  0.001, korx, kory
        else:
            korx = RAMX - ob
            kory = RAMY + ob
            korx1 = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            kory1 = ty1 / rRr * (rRr - ob) + RAMY + ob
            fr = rRr - ob
            fy = ty1 / rRr * (rRr - ob) + RAMY + ob
            fx = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            fx1 = (RAMX - ob)
            fy1 = (RAMY + ob)

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace("korx1", str(round(korx1, 3)))
        txt_ss = txt_ss.replace("kory1", str(round(kory1, 3)))
        txt_ss = txt_ss.replace("korx", str(round(korx, 3)))
        txt_ss = txt_ss.replace("kory", str(round(kory, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("fx1", str(round(fx1, 3)))
        txt_ss = txt_ss.replace("fy1", str(round(fy1, 3)))
        txt_ss = txt_ss.replace("fx", str(round(fx, 3)))
        txt_ss = txt_ss.replace("fy", str(round(fy, 3)))
        txt_ss = txt_ss.replace("fr", str(round(fr, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'ПСЯ' and 131 <= int(visota) <= 155:
        txt_ss = open('rs/30_it/pssl.txt', 'r').read()

        RAMY = 22 if int(visota) <= 170 else 22 + (int(visota) - 170) * 0.14
        RAMX, RAMK, ob = 90, 45, 30
        tx1 = (RAMX - RAMK - ob) / 2
        ty1 = (int(visota) - 2 * (RAMY + ob)) / 4
        rRr = (tx1 ** 2 + ty1 ** 2) / (2 * tx1)
        xa1 = RAMX
        ya1 = RAMY + ob
        xa2 = RAMK + rRr + ob
        ya2 = int(visota) / 2
        rRr1 = ob
        rRr2 = rRr + ob
        m = xa2 - xa1
        f = ya2 - ya1
        p = (m ** 2 + f ** 2) ** 0.5
        ks = (p ** 2 + rRr1 ** 2 - rRr2 ** 2) / (2 * p)

        if rRr <= 30:
            korx = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            korx1 = xa1 + m * ks / p - (f / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            kory1 = ya1 + f * ks / p + (m / p) * (rRr1 ** 2 - ks ** 2) ** 0.5
            fx, fy, fr, fx1, fy1 = korx, kory,  0.001, korx, kory
        else:
            korx = RAMX - ob
            kory = RAMY + ob
            korx1 = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            kory1 = ty1 / rRr * (rRr - ob) + RAMY + ob
            fr = rRr - ob
            fy = ty1 / rRr * (rRr - ob) + RAMY + ob
            fx = RAMX - rRr + (rRr - tx1) / rRr * (rRr - ob)
            fx1 = (RAMX - ob)
            fy1 = (RAMY + ob)

        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("RAMK", str(RAMK))
        txt_ss = txt_ss.replace("rRr1", str(rRr1))
        txt_ss = txt_ss.replace("rRr2", str(round(rRr2, 3)))
        txt_ss = txt_ss.replace("rRr", str(round(rRr, 3)))
        txt_ss = txt_ss.replace("korx1", str(round(korx1, 3)))
        txt_ss = txt_ss.replace("kory1", str(round(kory1, 3)))
        txt_ss = txt_ss.replace("korx", str(round(korx, 3)))
        txt_ss = txt_ss.replace("kory", str(round(kory, 3)))
        txt_ss = txt_ss.replace("tx1", str(round(tx1, 3)))
        txt_ss = txt_ss.replace("ty1", str(round(ty1, 3)))
        txt_ss = txt_ss.replace("fx1", str(round(fx1, 3)))
        txt_ss = txt_ss.replace("fy1", str(round(fy1, 3)))
        txt_ss = txt_ss.replace("fx", str(round(fx, 3)))
        txt_ss = txt_ss.replace("fy", str(round(fy, 3)))
        txt_ss = txt_ss.replace("fr", str(round(fr, 3)))
        txt_ss = txt_ss.replace("ob", str(ob))
        txt_ss = txt_ss.replace("KANT", str(Kant))

    elif k[7] == 'Планка' or (k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 131):
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", str(Kant))

    return txt_ss