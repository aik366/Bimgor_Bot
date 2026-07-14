def it_94(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 32.8, 27.5, 2]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/94_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/94_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and 130 <= int(visota) < 155:
        txt_ss = open('rs/94_it/ps2.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[1]

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 155:
        txt_ss = open('rs/94_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss