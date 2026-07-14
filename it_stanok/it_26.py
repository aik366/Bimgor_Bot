def it_26(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/26_it/f.txt', 'r').read()

        txt_ss = txt_ss.replace("sX1", '20')
        txt_ss = txt_ss.replace("sY1", '20')
        txt_ss = txt_ss.replace("sX", '70')
        txt_ss = txt_ss.replace("sY", '70')
        txt_ss = txt_ss.replace("xC", f'{int(dlina) / 2:.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 130:
        txt_ss = open('rs/26_it/f.txt', 'r').read()

        txt_ss = txt_ss.replace("sX1", '12')
        txt_ss = txt_ss.replace("sY1", '12')
        txt_ss = txt_ss.replace("sX", '70')
        txt_ss = txt_ss.replace("sY", '30')
        txt_ss = txt_ss.replace("xC", f'{int(dlina) / 2:.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 130:
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    if k[6] == '24':
        txt_ss = txt_ss.replace("150", "131")
        txt_ss = txt_ss.replace("t-2.5", "t-3")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("150", "136")
        txt_ss = txt_ss.replace("t-2.5", "t-2")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("150", "144")
        txt_ss = txt_ss.replace("t-2.5", "t-1.2")

    return txt_ss
