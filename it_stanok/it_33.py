def it_33(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'СТЕКЛО' or k[7] == 'Хлеб_ст':
        oBv[1] = oBv[8]
        txt_ss = open('rs/33_it/st.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in  ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/33_it/per.txt', 'r').read()
        RAMX, RAMY = 44.5, 44.5
        lxp = (int(dlina) - 106 - 6) / 3 + 106
        lyp = (int(visota) - 106 - 3) / 2 + 106
        dx1 = lxp - 103
        dx2 = (lxp - 103) * 2
        dy1 = lyp - 103

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace('lxp', str(lxp))
        txt_ss = txt_ss.replace('lyp', str(lyp))
        txt_ss = txt_ss.replace('dx1', str(dx1))
        txt_ss = txt_ss.replace('dx2', str(dx2))
        txt_ss = txt_ss.replace('dy1', str(dy1))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    else:
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss