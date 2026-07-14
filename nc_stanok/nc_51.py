oBv51nc = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 12, 27.5, 19]

def nc_51(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv51nc.copy()
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/51/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/51/f2.txt', 'r').read()
        RAMX, RAMY, RAMK = RAM[0], RAM[0], RAM[2]
        RAMZ = int(dlina) - RAMK + (RAMX + float(Kant))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("WEEKE BHC T.", "На Италянском тоже есть")
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/51/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'СТЕКЛО':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51/xl_st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz*2) / 3 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ2':
        oBv[1] = oBv[8]
        txt_ss = open('rs/51/perxl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz*2) / 3 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ4':
        oBv[1] = oBv[7]
        txt_ss = open('rs/51/per4.txt', 'r').read()
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

    elif k[7] == 'ПЕРЕПЛЕТ4_xl':
        oBv[1] = oBv[7]
        txt_ss = open('rs/51/per4xl.txt', 'r').read()
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
        txt_ss = open('rs/51/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz*3) / 4 + 106
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
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Бутыл.' and int(visota) >= 146:
        txt_ss = open('rs/51/but.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] == 'Бутыл.' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/butsl.txt', 'r').read()
        RAMX, RAMY = RAM[0], 29.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/51/pssl2.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
