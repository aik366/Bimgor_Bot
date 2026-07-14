def nc_94(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 32, 13.6001, 22.3001, 11.7301, 20.4301, 32.8, 27.5, 2]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/94/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/94/st.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and 130 <= int(visota) < 155:
        txt_ss = open('rs/94/ps2.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[1]

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 155:
        txt_ss = open('rs/94/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss