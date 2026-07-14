def it_31(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/31_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '60')
        txt_ss = txt_ss.replace('RAMY', '60')

    elif k[7] in ('ПСЯ', 'Бутыл.'):
        txt_ss = open('rs/31_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '60')
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    if k[6] == '24':
        txt_ss = txt_ss.replace("150", "146")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "3, 0, 0,")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("150", "136")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "2, 0, 0,")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("150", "144")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "1.2, 0, 0,")

    return txt_ss
