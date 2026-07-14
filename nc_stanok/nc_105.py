from nc_stanok import nc_104


def nc_105(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return nc_104(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 32.2001, 60, 13, 22.3001, -6, 20.4051, 27.5, 20.9001, 34.0701]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/105/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146 and int(visota) < 170:
        txt_ss = open('rs/105/pssl.txt', 'r').read()
        oBv[5], oBv[6] = 2, oBv[4] + (oBv[9] - oBv[1])
        RAMX, RAMY = RAM[0], RAM[1] + 4
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 170:
        txt_ss = open('rs/105/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 4
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 4
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss