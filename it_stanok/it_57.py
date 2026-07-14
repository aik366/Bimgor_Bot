from it_stanok import it_51


def it_57(k, dlina, visota, RAM):
    if k[7] in ("ПСЯ", "Бутыл."):
        return it_51(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад' and int(visota) >= 255:
        txt_ss = open('rs/57_it/f.txt', 'r').read()
        RAMX, RAMY, rRr = RAM[0] + 50, RAM[0], 50

        h1 = (rRr * rRr + 2 * rRr * (oBv[1] - oBv[0])) ** 0.5 + RAMY + oBv[0]
        h2 = (rRr * rRr + 2 * rRr * (oBv[2] - oBv[0])) ** 0.5 + RAMY + oBv[0]

        if int(visota) < 298:
            XRAM = 71.5 + (84.5 ** 2 - ((int(visota) - 143) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMY + oBv[2]
            YRAM = h2
            ZRAM = h2

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("h1", f'{h1:.3f}')
        txt_ss = txt_ss.replace("h2", f'{h2:.3f}')
        txt_ss = txt_ss.replace("rRr", str(rRr))
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб' and int(visota) >= 255:
        txt_ss = open('rs/57_it/xl.txt', 'r').read()
        RAMX, RAMY, rRr = RAM[0] + 50, RAM[0], 50

        h1 = (rRr * rRr + 2 * rRr * (oBv[1] - oBv[0])) ** 0.5 + RAMY + oBv[0]
        h2 = (rRr * rRr + 2 * rRr * (oBv[2] - oBv[0])) ** 0.5 + RAMY + oBv[0]

        if int(visota) < 298:
            XRAM = 71.5 + (84.5 ** 2 - ((int(visota) - 143) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMY + oBv[2]
            YRAM = h2
            ZRAM = h2

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("h1", f'{h1:.3f}')
        txt_ss = txt_ss.replace("h2", f'{h2:.3f}')
        txt_ss = txt_ss.replace("rRr", str(rRr))
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/57_it/st.txt', 'r').read()
        RAMX, RAMY, rRr = RAM[0] + 50, RAM[0], 50

        h1 = (rRr * rRr + 2 * rRr * (oBv[1] - oBv[0])) ** 0.5 + RAMY + oBv[0]
        h2 = (rRr * rRr + 2 * rRr * (oBv[2] - oBv[0])) ** 0.5 + RAMY + oBv[0]

        if int(visota) < 298:
            XRAM = 71.5 + (84.5 ** 2 - ((int(visota) - 143) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMY + oBv[2]
            YRAM = h2
            ZRAM = h2

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("h1", f'{h1:.3f}')
        txt_ss = txt_ss.replace("h2", f'{h2:.3f}')
        txt_ss = txt_ss.replace("rRr", str(rRr))
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/57_it/xlst.txt', 'r').read()
        RAMX, RAMY, rRr = RAM[0] + 50, RAM[0], 50

        h1 = (rRr * rRr + 2 * rRr * (oBv[1] - oBv[0])) ** 0.5 + RAMY + oBv[0]
        h2 = (rRr * rRr + 2 * rRr * (oBv[2] - oBv[0])) ** 0.5 + RAMY + oBv[0]

        if int(visota) < 298:
            XRAM = 71.5 + (84.5 ** 2 - ((int(visota) - 143) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMY + oBv[2]
            YRAM = h2
            ZRAM = h2

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("h1", f'{h1:.3f}')
        txt_ss = txt_ss.replace("h2", f'{h2:.3f}')
        txt_ss = txt_ss.replace("rRr", str(rRr))
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))
        
    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss
