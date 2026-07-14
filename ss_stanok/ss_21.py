def ss_21(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/21/f.txt', 'r').read()
        sU, sS, sS1 = 60, 30, 15
        dxD, dxK, dyD, dyK  = 165, 106, 118, 57

        txt_ss = txt_ss.replace("sU", str(sU))
        txt_ss = txt_ss.replace("sS1", str(sS1))
        txt_ss = txt_ss.replace("sS", str(sS))
        txt_ss = txt_ss.replace("dxD", str(dxD))
        txt_ss = txt_ss.replace("dxK", str(dxK))
        txt_ss = txt_ss.replace("dyD", str(dyD))
        txt_ss = txt_ss.replace("dyK", str(dyK))

    elif k[7] =='Хлеб':
        txt_ss = open('rs/21/f.txt', 'r').read()
        sU, sS, sS1 = 60, 30, 15
        dxD, dxK, dyD, dyK = 118, 57, 165, 106

        txt_ss = txt_ss.replace("sU", str(sU))
        txt_ss = txt_ss.replace("sS1", str(sS1))
        txt_ss = txt_ss.replace("sS", str(sS))
        txt_ss = txt_ss.replace("dxD", str(dxD))
        txt_ss = txt_ss.replace("dxK", str(dxK))
        txt_ss = txt_ss.replace("dyD", str(dyD))
        txt_ss = txt_ss.replace("dyK", str(dyK))

    elif k[7]in ('Бутыл.', 'ПСЯ') and int(visota) >= 146:
        txt_ss = open('rs/21/but.txt', 'r').read()
        sU, sS, sS1, sU1 = 60, 30, 15, 35
        dxD, dxK, dyD, dyK = 120, 54, 88, 27

        txt_ss = txt_ss.replace("sU1", str(sU1))
        txt_ss = txt_ss.replace("sU", str(sU))
        txt_ss = txt_ss.replace("sS1", str(sS1))
        txt_ss = txt_ss.replace("sS", str(sS))
        txt_ss = txt_ss.replace("dxD", str(dxD))
        txt_ss = txt_ss.replace("dxK", str(dxK))
        txt_ss = txt_ss.replace("dyD", str(dyD))
        txt_ss = txt_ss.replace("dyK", str(dyK))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss