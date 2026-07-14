def it_20(k, dlina, visota, RAM):
    txt_ss = ''

    RAMX = "70" if RAM[0] == 44.5 else str(RAM[0])

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/20_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', RAMX)
        txt_ss = txt_ss.replace('RAMY', RAMX)

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/20_it/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', RAMX)
        txt_ss = txt_ss.replace('RAMY', RAMX)

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 130:
        txt_ss = open('rs/20_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', RAMX)
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/20_it/pssl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', RAMX)
        txt_ss = txt_ss.replace('RAMY', '40')

    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'Планка'):
        return txt_ss
    elif k[6] == '22':
        txt_ss = txt_ss.replace("131", "137")
    elif k[6] == '23':
        txt_ss = txt_ss.replace("131", "157")
    elif k[6] == '24':
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 3, 0,")
    elif k[6] == '26':
        txt_ss = txt_ss.replace("131", "150")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2.5, 0,")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("131", "136")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 2, 0,")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("131", "144")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 1.2, 0,")
    elif k[6] == '30':
        txt_ss = txt_ss.replace("131", "159")
        txt_ss = txt_ss.replace("0, 9, 0,", "0, 12.9, 0,")

    return txt_ss
