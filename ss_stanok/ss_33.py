def ss_33(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 27.5, 10.6, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'СТЕКЛО' or k[7] == 'Хлеб_ст':
        oBv[1] = oBv[7]
        txt_ss = open('rs/33/st.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in  ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/33/per.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        zaz = 3
        Lst = (int(dlina) - 106 - zaz * 2) / 3 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    else:
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
