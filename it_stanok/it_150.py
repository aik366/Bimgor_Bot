def it_150(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [29, 41, 10.8, 22, 21.401, 25, -1, 44, 47, 6, 10.4, 1.4]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/150_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', "58.5")
        txt_ss = txt_ss.replace('RAMY', "58.5")
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/150_it/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', "58.5")
        txt_ss = txt_ss.replace('RAMY', "58.5")
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/150_it/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', "58.5")
        txt_ss = txt_ss.replace('RAMY', "23.5")
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    txt_ss = txt_ss.replace("' kr17", "")
    return txt_ss
