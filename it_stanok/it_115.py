def it_115(k, dlina, visota, RAM):
    txt_ss = ''
    kray_dict = {"15": 18.0, "16": 14.5, "17": 16.0, "19": 16.0, "11": 24.0, "12": 21.0, "14": 24.0}

    nach = kray_dict[k[5]] if RAM[0] == 44.5 else RAM[0] + 7.3
    rost = 22.0 if RAM[1] == 22.5 else RAM[1] + 16
    glubina = 2.0 if RAM[2] > 10 else RAM[2]

    if k[7] in ('Фасад', 'Бутыл.'):
        txt_ss = open('rs/115_it/f.txt', 'r').read()

        konec = round((int(visota) - 2 * nach) / rost)
        shag = round((int(visota) - 2 * nach) / konec, 4)

        line = (f'  @ START_POINT, 0 : -20, {nach}, 0\n'
                f'  @ LINE_EP, 0 : lpx+20, {nach}, {glubina}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : lpx+20, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx+20, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/115_it/f2.txt', 'r').read()

        konec = round((int(visota) - 2 * nach) / rost)
        shag = round((int(visota) - 2 * nach) / konec, 4)

        line = (f'  @ START_POINT, 0 : -20, {nach}, 0\n'
                f'  @ LINE_EP, 0 : {str(RAM[2])}, {nach}, {glubina}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : {str(RAM[2])}, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {str(RAM[2])}, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        line_2 = (f'  @ START_POINT, 0 : {str(RAM[2])}, -20, 0\n'
                  f'  @ LINE_EP, 0 : {str(RAM[2])}, lpy+20, {glubina}, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace("'vib2", line_2)

    elif k[7] in ('Хлеб', 'ПСЯ'):
        txt_ss = open('rs/115_it/f.txt', 'r').read()

        konec = round((int(dlina) - 2 * nach) / rost)
        shag = round((int(dlina) - 2 * nach) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nach}, -20, 0\n'
                f'  @ LINE_EP, 0 : {nach}, lpy+20, {glubina}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : {nach + shag * (i + 1):.4f}, lpy+20, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach + shag * (i + 1):.4f}, -20, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : {nach + shag * (i + 2):.4f}, -20, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach + shag * (i + 2):.4f}, lpy+20, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss
