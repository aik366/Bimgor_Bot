def nc_109(k, dlina, visota, RAM):
    txt_ss = ''

    oBv = [27, 33, -1.0301, 22.3001, 20.4051, 32.2001, 20.4051, 34.0701, 27.5, -2.9]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/109/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[0] = oBv[7]
        txt_ss = open('rs/109/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/109/ps.txt', 'r').read()
        RAMX = RAM[0]
        RAMY = RAM[1] if int(visota) < 170 else RAM[1] + 4

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0] + 4
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if k[9] == "БПл":
        txt_ss = txt_ss.replace('Z=t-12', 'Z=t-9')

    return txt_ss