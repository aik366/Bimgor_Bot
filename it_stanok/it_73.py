from it_stanok import it_92


def it_73(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]

    if (k[7] == 'Фасад' and int(visota) < 230) or k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2',
                                                           'Бутыл.', 'Планка'):
        return it_92.it_92(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 292:
        txt_ss = open('rs/73_it/f.txt', 'r').read()
        Txt_38 = open('rs/73_it/38.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 60
        ty1 = (int(visota) - 2 * 103 - 26) / 2 - RAM / 2
        key = int(ty1 / RAM)
        CY = ty1 - key * RAM + 103 + 13 - 3
        txt_ss = txt_ss.replace('CY', str(CY))

        for x in range(2 * key + 2):
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace('CY', str(CY))
            CY = CY + RAM

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace(str(CY - RAM) + "+" + str(RAM), str(CY - RAM + 7))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад' and int(visota) >= 230:
        txt_ss = open('rs/73_it/f.txt', 'r').read()
        Txt_38 = open('rs/73_it/38.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 6.01

        CY = int(visota) / 2 - 3

        txt_ss = txt_ss.replace("' TTTTT", Txt_38)
        txt_ss = txt_ss.replace('CY', str(CY))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/73_it/xl.txt', 'r').read()
        Txt_38 = open('rs/73_it/38_xl.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[0], 60
        ty1 = (int(dlina) - 2 * 103 - 26) / 2 - RAM / 2
        key = int(ty1 / RAM)
        CY = ty1 - key * RAM + 103 + 13 - 3
        txt_ss = txt_ss.replace('CY', str(CY))

        for x in range(2 * key + 2):
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace('CY', str(CY))
            CY = CY + RAM

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace(str(CY - RAM) + "+" + str(RAM), str(CY - RAM + 7))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/73_it/ps.txt', 'r').read()
        Txt_38 = open('rs/73_it/38_xl.txt', 'r').read()

        RAMX, RAMY, RAM = RAM[0], RAM[1], 60
        ty1 = (int(dlina) - 2 * 89 - 26) / 2 - RAM / 2
        key = int(ty1 / RAM)
        CY = ty1 - key * RAM + 89 + 13 - 3
        txt_ss = txt_ss.replace('CY', str(CY))

        for x in range(2 * key + 2):
            txt_ss = txt_ss.replace("' TTTTT", Txt_38)
            txt_ss = txt_ss.replace('CY', str(CY))
            CY = CY + RAM

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace(str(CY - RAM) + "+" + str(RAM), str(CY - RAM + 7))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) < 146:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
