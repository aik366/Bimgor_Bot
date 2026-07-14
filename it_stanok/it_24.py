def it_24(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/24_it/f.txt', 'r').read()

        RAM, ks, lf, wf = 60, 18, 35, 12
        b = int(dlina) / 2 - lf - RAM
        a = int(visota) / 2 - wf - RAM
        xf = b * (a - ks) / a + RAM
        yf = a * (b - ks) / b + RAM
        xf1 = b * (a - 2 * ks) / a + RAM
        yf1 = a * (b - 2 * ks) / b + RAM

        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace('ks', str(ks))
        txt_ss = txt_ss.replace('lf', str(lf))
        txt_ss = txt_ss.replace('wf', str(wf))
        txt_ss = txt_ss.replace('yf1', f'{yf1:.3f}')
        txt_ss = txt_ss.replace('xf1', f'{xf1:.3f}')
        txt_ss = txt_ss.replace('yf', f'{yf:.3f}')
        txt_ss = txt_ss.replace('xf', f'{xf:.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 140:
        txt_ss = open('rs/24_it/ps.txt', 'r').read()

        RAM, RAMY, ks, lf, wf = 60, 30, 12, 20, 8
        b = int(dlina) / 2 - lf - RAM
        a = int(visota) / 2 - wf - RAMY
        xf = b * (a - ks) / a + RAM
        yf = a * (b - ks) / b + RAMY
        xf1 = b * (a - 2 * ks) / a + RAM
        yf1 = a * (b - 2 * ks) / b + RAMY

        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAM', str(RAM))
        txt_ss = txt_ss.replace('ks', str(ks))
        txt_ss = txt_ss.replace('lf', str(lf))
        txt_ss = txt_ss.replace('wf', str(wf))
        txt_ss = txt_ss.replace('yf1', f'{yf1:.3f}')
        txt_ss = txt_ss.replace('xf1', f'{xf1:.3f}')
        txt_ss = txt_ss.replace('yf', f'{yf:.3f}')
        txt_ss = txt_ss.replace('xf', f'{xf:.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 140:
        txt_ss = open('rs/91/pl.txt', 'r').read()

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