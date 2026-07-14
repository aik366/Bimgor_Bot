def it_25(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад' and int(visota) >= 180:
        txt_ss = open('rs/25_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='Хлеб' and int(visota) >= 180:
        txt_ss = open('rs/25_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='Бутыл.' and int(visota) >= 110:
        txt_ss = open('rs/25_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] =='ПСЯ' and int(visota) >= 110:
        txt_ss = open('rs/25_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('sy', '20')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()


    if k[6] == '24':
        txt_ss = txt_ss.replace("150", "131")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "3, 0, 0,")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("150", "136")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "2, 0, 0,")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("150", "144")
        txt_ss = txt_ss.replace("2.5, 0, 0,", "1.2, 0, 0,")

    return txt_ss