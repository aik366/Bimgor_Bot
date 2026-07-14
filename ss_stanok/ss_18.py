def ss_18(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад' and int(visota) >= 180:
        txt_ss = open('rs/18/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAM', '70')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='Хлеб' and int(visota) >= 180:
        txt_ss = open('rs/18/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAM', '70')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='Бутыл.' and int(visota) >= 110:
        txt_ss = open('rs/18/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAM', '40')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='ПСЯ' and int(visota) >= 100:
        txt_ss = open('rs/18/ps.txt', 'r').read()
        txt_ss = txt_ss.replace('RAM', '70')
        txt_ss = txt_ss.replace('sy', '20')

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