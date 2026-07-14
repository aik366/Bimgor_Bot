def ss_36(k, dlina, visota, RAM):
    txt_ss = ''
    ram0, ram1 = 27, 36.5

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/36/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('ram0', str(ram0))
        txt_ss = txt_ss.replace('ram1', str(ram1))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/36/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('ram0', str(ram0))
        txt_ss = txt_ss.replace('ram1', str(ram1))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/36/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] - 8
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('ram0', str(ram0))
        txt_ss = txt_ss.replace('ram1', str(ram1))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss
