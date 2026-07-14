def it_27(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/27_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/27_it/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] in ('Бутыл.', 'ПСЯ') and int(visota) >= 130:
        txt_ss = open('rs/27_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '30')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()


    if k[6] == '24':
        txt_ss = txt_ss.replace("9, 0, 0,", "3, 0, 0,")
    elif k[6] == '26':
        txt_ss = txt_ss.replace("131", "150")
        txt_ss = txt_ss.replace("9, 0, 0,", "2.5, 0, 0,")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("131", "136")
        txt_ss = txt_ss.replace("9, 0, 0,", "2, 0, 0,")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("131", "144")
        txt_ss = txt_ss.replace("9, 0, 0,", "1.2, 0, 0,")

    return txt_ss