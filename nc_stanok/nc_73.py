from nc_stanok import nc_92


def nc_73(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]

    if (k[7] == 'Фасад' and int(visota) < 230) or k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2',
                                                           'Бутыл.', 'Планка'):
        return nc_92.nc_92(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 292:
        txt_ss = open('rs/73/f.txt', 'r').read()
        Txt_38 = open('rs/73/38.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 60
        ty1 = (int(visota) - 2 * 103 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)
        CY = ty1 - k * RAM

        for x in range(2 * k + 2):
            txt_ss = txt_ss.replace('\TTTTT', Txt_38)

        CP = 2 * (k + 1) * 4 - 1

        txt_ss = txt_ss.replace('CY', str(CY))
        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад' and int(visota) >= 230:
        txt_ss = open('rs/73/f.txt', 'r').read()
        Txt_38 = open('rs/73/38.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 60

        txt_ss = txt_ss.replace('\TTTTT', Txt_38)

        CY = int(visota) / 2 - 116

        txt_ss = txt_ss.replace('CY', str(CY))
        txt_ss = txt_ss.replace('CP', '3')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/73/xl.txt', 'r').read()
        Txt_38 = open('rs/73/38_xl.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 60
        ty1 = (int(dlina) - 2 * 103 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)
        CY = ty1 - k * RAM

        for x in range(2 * k + 2):
            txt_ss = txt_ss.replace('\TTTTT', Txt_38)

        CP = 2 * (k + 1) * 4 - 1

        txt_ss = txt_ss.replace('CY', str(CY))
        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/73/ps.txt', 'r').read()
        Txt_38 = open('rs/73/38_xl.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[1], 60
        ty1 = (int(dlina) - 2 * 89 - 26) / 2 - RAM / 2
        k = int(ty1 / RAM)
        CY = ty1 - k * RAM

        for x in range(2 * k + 2):
            txt_ss = txt_ss.replace('\TTTTT', Txt_38)

        CP = 2 * (k + 1) * 4 - 1

        txt_ss = txt_ss.replace('CY', str(CY))
        txt_ss = txt_ss.replace('CP', str(CP))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
