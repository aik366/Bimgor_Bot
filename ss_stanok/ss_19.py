def ss_19(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад' and int(visota) >= 180:
        txt_ss = open('rs/19/f.txt', 'r').read()
        txt_ss = txt_ss.replace('rY', '35')

    elif k[7] =='Хлеб' and int(visota) >= 180:
        txt_ss = open('rs/19/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('rY', '35')

    elif k[7] =='Бутыл.' and int(visota) >= 130:
        txt_ss = open('rs/19/but.txt', 'r').read()
        txt_ss = txt_ss.replace('rY', '325')

    elif k[7] =='ПСЯ' and int(visota) >= 100:
        txt_ss = open('rs/19/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('rY', '35')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss