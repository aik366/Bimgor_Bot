def it_17(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/17_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] =='Хлеб':
        txt_ss = open('rs/17_it/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] =='Бутыл.' and int(visota) >= 110:
        txt_ss = open('rs/17_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] =='ПСЯ' and int(visota) >= 110:
        txt_ss = open('rs/17_it/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '38')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()


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