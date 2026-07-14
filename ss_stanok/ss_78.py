def ss_78(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 35.4, 61.5, 13.6, 22.21, 12.2001, 20.7501, 27.5, 10.6, 19]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/78/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/78/f2.txt', 'r').read()
        RAMX, RAMY, RAMK = RAM[0], RAM[0], RAM[2]
        RAMZ = int(dlina) - RAMK + (RAMX + 9)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("WEEKE BHC T.", "На Италянском тоже есть")
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/78/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/78/per.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz * 2) / 3 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/78/per4.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz) / 2 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[7]
        txt_ss = open('rs/78/per8.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        zaz = 3
        Lst = (int(dlina) - 106 - zaz*3) / 4 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/78/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] - 6
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()
        
    if RAM[4] == 1:
        RAMX, RAMY = RAM[0], RAM[0]
        if k[7] in ('Фасад', 'Бутыл.', 'СТЕКЛО'):
            pod_92 = open('pl/92_f.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[5] - 3.07 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[5] - 3.07 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
