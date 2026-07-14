from nc_stanok import nc_51


def nc_52(k, dlina, visota, RAM):
    if k[7] in ("СТЕКЛО", "Хлеб_ст", "ПСЯ", "Бутыл.", "ПЕРЕПЛЕТ", "ПЕРЕПЛЕТ2"):
        return nc_51(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/52/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]

        if int(visota) < 267:
            XRAM = 71 + (71 ** 2 - ((int(visota) - 142) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMX + oBv[2]
            YRAM = int(visota) - RAMX - 88.847
            ZRAM = RAMX + 88.847

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/52/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]

        if int(visota) < 267:
            XRAM = 71 + (71 ** 2 - ((int(visota) - 142) / 2) ** 2) ** 0.5
            YRAM = int(visota) / 2
            ZRAM = YRAM + 0.001
        else:
            XRAM = RAMX + oBv[2]
            YRAM = int(visota) - RAMX - 88.847
            ZRAM = RAMX + 88.847

        txt_ss = txt_ss.replace("XRAM", f'{XRAM:.3f}')
        txt_ss = txt_ss.replace("YRAM", f'{YRAM:.3f}')
        txt_ss = txt_ss.replace("ZRAM", f'{ZRAM:.3f}')
        txt_ss = txt_ss.replace("RAMX", str(RAMX))
        txt_ss = txt_ss.replace("RAMY", str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
        
    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
