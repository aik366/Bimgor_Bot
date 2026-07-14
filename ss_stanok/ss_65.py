oBv65ss = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 12, 27.5, 19]


def ss_65(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv65ss.copy()
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/65/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/65/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/65/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz * 2) / 3 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/65/per4xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz) / 2 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[8]
        txt_ss = open('rs/65/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz * 3) / 4 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/51/ps.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 170:
            RAMY = RAM[1]
        else:
            RAMY = RAM[1] + 4
        RAMX = RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/65/but.txt', 'r').read()
        if int(visota) >= 146 and int(visota) < 170:
            RAMY = RAM[1]
        else:
            RAMY = RAM[1] + 4
        RAMX = RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 4
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/65/butsl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 7
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/51/pssl2.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 4
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
