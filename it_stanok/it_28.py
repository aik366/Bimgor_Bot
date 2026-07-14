def it_28(k, dlina, visota, RAM):
    txt_ss = ''
    if (k[7] in ('Фасад', 'Хлеб')) and int(visota) < 260:
        txt_ss = open('rs/28_it/f2.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '120')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '60')

    elif k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/28_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '120')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/28_it/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '120')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'Бутыл.' and int(visota) < 150:
        txt_ss = open('rs/28_it/but.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '110')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('rRr', '40')

    elif k[7] == 'Бутыл.' and int(visota) >= 150:
        txt_ss = open('rs/28_it/but.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '110')
        txt_ss = txt_ss.replace('RAMY', '38')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'Бутыл.' and 140 <= int(visota) < 150:
        txt_ss = open('rs/28_it/but.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '110')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('rRr', '40')

    elif k[7] == 'ПСЯ' and int(visota) >= 150:
        txt_ss = open('rs/28_it/but.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '115')
        txt_ss = txt_ss.replace('RAMY', '38')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'ПСЯ' and 140 <= int(visota) < 150:
        txt_ss = open('rs/28_it/but.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '115')
        txt_ss = txt_ss.replace('RAMY', '30')
        txt_ss = txt_ss.replace('rRr', '40')

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