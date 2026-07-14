def it_116(k, dlina, visota, RAM):
    txt_ss = ''

    konec, d, rost, nach = 0, 0, 14, 64.0

    if k[7] in ('Фасад', 'Бутыл.'):
        txt_ss = open('rs/114_it/f.txt', 'r').read()

        konec = round((int(visota) - 2 * nach) / rost)
        shag = round((int(visota) - 2 * nach) / konec, 4)

        line = (f'  @ START_POINT, 0 : -20, {nach}, 0\n'
                f'  @ LINE_EP, 0 : lpx+20, {nach}, 2, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : lpx+20, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : -20, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx+20, {nach + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] in ('Хлеб', 'ПСЯ'):
        txt_ss = open('rs/114_it/f.txt', 'r').read()

        konec = round((int(dlina) - 2 * nach) / rost)
        shag = round((int(dlina) - 2 * nach) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nach}, -20, 0\n'
                f'  @ LINE_EP, 0 : {nach}, lpy+20, 2, 0, 0, 0, 0, 0, 0\n')

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
