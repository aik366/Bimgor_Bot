from tkinter.messagebox import showinfo

D = 26
oBv96it = [D, 29, D + 34.5, D - 3.701, D - 5.601, D - 12.901, D - 14.801, D - 15, D + 0.5, 22]


def it_96(k, dlina, visota, RAM):
    txt_ss = ''
    konec, shag, gl = 0, 38, 8
    oBv = oBv96it.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/96_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        nachy, nachx = RAMY + oBv[1] + 15, RAMX + oBv[1] + 15

        konec = int((int(visota) - 2 * nachy) / shag) + 1
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nachx}, {nachy}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace(f"lpx-{nachx}, {nachy}, {gl},", f"lpx-{nachx}, {nachy}, {gl-gl/2},", 1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/96_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 60 + (RAM[0] - 44.5)
        lyp = int(dlina) - lxp + zaz
        dx1 = lxp - zaz
        nachy, nachx = RAMY + oBv[1] + 15, RAMX + oBv[1] + 15

        konec = int((int(visota) - 2 * nachy) / shag) + 1
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nachx}, {nachy}, 0\n'
                f'  @ LINE_EP, 0 : {lxp-nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        line2 = (f'  @ START_POINT, 0 : {dx1+nachx}, {nachy}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : {lxp-nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            line2 += (f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {dx1+nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {lxp-nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            line2 += (f'  @ LINE_EP, 0 : {dx1+nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line).replace("'vib2", line2)
        txt_ss = txt_ss.replace(f"{lxp-nachx}, {nachy}, {gl},", f"{lxp-nachx}, {nachy}, {gl - gl / 2},", 1)
        txt_ss = txt_ss.replace(f"lpx-{nachx}, {nachy}, {gl},", f"lpx-{nachx}, {nachy}, {gl - gl / 2},", 1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', str(lxp))
        txt_ss = txt_ss.replace('lyp', str(lyp))
        txt_ss = txt_ss.replace('dx1', str(dx1))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        xdf1_dlina = (RAM[2] - (2 * (RAM[0] + oBv[9] - 2) + 1))
        xdf2_dlina = ((int(dlina) - RAM[2] + zaz) - (2 * (RAM[0] + oBv[9] - 2) + 1))
        xdf_visota = (int(visota) - (2 * (RAM[0] + oBv[9] - 2) + 1))
        showinfo('ХДФ', f'ХДФ {xdf1_dlina}x{xdf_visota} и {xdf2_dlina}x{xdf_visota}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/96_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/96_it/per.txt', 'r').read()
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8
        lxp = (int(dlina) - 106 - zaz * 2) / 3 + 106
        lyp = (int(visota) - 106 - zaz) / 2 + 106
        dx1 = lxp - (106 - zaz)
        dx2 = (lxp - (106 - zaz)) * 2
        dy1 = lyp - (106 - zaz)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/96_it/per4.txt', 'r').read()
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8
        lxp = (int(dlina) - 106 - zaz) / 2 + 106
        lyp = (int(visota) - 106 - zaz) / 2 + 106
        dx1 = lxp - (106 - zaz)
        dx2 = lxp - (106 - zaz)
        dy1 = lyp - (106 - zaz)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[8]
        txt_ss = open('rs/96_it/per8.txt', 'r').read()
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8
        lxp = (int(dlina) - 106 - zaz * 3) / 4 + 106
        lyp = (int(visota) - 106 - zaz) / 2 + 106
        dx1 = lxp - (106 - zaz)
        dx2 = (lxp - (106 - zaz)) * 2
        dx3 = (lxp - (106 - zaz)) * 3
        dy1 = lyp - (106 - zaz)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('lxp', f'{lxp:.3f}')
        txt_ss = txt_ss.replace('lyp', f'{lyp:.3f}')
        txt_ss = txt_ss.replace('dx1', f'{dx1:.3f}')
        txt_ss = txt_ss.replace('dx2', f'{dx2:.3f}')
        txt_ss = txt_ss.replace('dx3', f'{dx3:.3f}')
        txt_ss = txt_ss.replace('dy1', f'{dy1:.3f}')
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 133:
        txt_ss = open('rs/96_it/ps.txt', 'r').read()

        RAMX, RAMY, shag = RAM[0], RAM[1], 15
        nachy, nachx = RAMY + oBv[1] + 10, RAMX + oBv[1] + 10

        if RAM[1] != 22.5 and int(visota) < 162:
            txt_ss = txt_ss.replace('@ ROUT, 0 : "132"', '\' ROUT, 0 : "132"', 1)

        konec_temp = int((int(visota) - 2 * nachy) / shag) + 1
        konec = 1 if konec_temp == 0 else konec_temp
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nachx}, {nachy}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    if RAM[4] == 1 and RAM[2] == 700.0:
        RAMX, RAMY = RAM[0], RAM[0]
        if k[7] in ('Фасад', 'Бутыл.', 'СТЕКЛО'):
            pod_92 = open('pl/92_f_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[4] - 3.5 + 0.01} ')
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl_it.txt', 'r').read()
            txt_ss = txt_ss.replace("' pod45", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[4] - 3.5 + 0.01} ')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    if RAM[4] == 1 and RAM[2] != 700.0:
        txt_ss = txt_ss.replace(", 5, 0, 0, 0,", f", {int(RAM[2])}, 0, 0, 0,")
        txt_ss = txt_ss.replace("0, 8, 0,", f"0, {int(RAM[2]) + 3}, 0,")
        txt_ss = txt_ss.replace('@ ROUT, 0 : "162_1"', '\' ROUT, 0 : "162_1"')

    if k[9] == 'БПл':
        txt_ss = txt_ss.replace("8, 0, 0, 0, 0, 0", "5, 0, 0, 0, 0, 0,")
    return txt_ss
