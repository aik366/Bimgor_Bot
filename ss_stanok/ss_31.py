def ss_31(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/31/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '60')
        txt_ss = txt_ss.replace('RAMY', '60')

    elif k[7] in ('ПСЯ', 'Бутыл.'):
        txt_ss = open('rs/31/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '60')
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if k[6] == '24':
        txt_ss = txt_ss.replace("150", "146")
        txt_ss = txt_ss.replace("t-2.5", "t-3")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("150", "136")
        txt_ss = txt_ss.replace("t-2.5", "t-2")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("150", "144")
        txt_ss = txt_ss.replace("t-2.5", "t-1.2")

    return txt_ss
