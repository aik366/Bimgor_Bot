from tkinter.messagebox import showinfo
from it_stanok import it_92


def it_107(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_92(k, dlina, visota, RAM)

    txt_ss = ''
    konec, shag, gl = 0, 38, 10.5
    D = 26
    oBv = [D, 29, D + 34.5, D - 3.701, D - 5.601, D - 12.901, D - 14.801, D - 15, D + 0.5, 22]

    if k[7] == 'Фасад':
        txt_ss = open('rs/107_it/f.txt', 'r').read()
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
        txt_ss = txt_ss.replace(f"lpx-{nachx}, {nachy}, {gl},", f"lpx-{nachx}, {nachy}, {gl - gl / 2},", 1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/107_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0], RAM[0], RAM[2], 52
        lyp = int(dlina) - lxp + zaz
        dx1 = lxp - zaz
        nachy, nachx = RAMY + oBv[1] + 15, RAMX + oBv[1] + 15

        konec = int((int(visota) - 2 * nachy) / shag) + 1
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'  @ START_POINT, 0 : {nachx}, {nachy}, 0\n'
                f'  @ LINE_EP, 0 : {lxp - nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        line2 = (f'  @ START_POINT, 0 : {dx1 + nachx}, {nachy}, 0\n'
                 f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy}, {gl}, 0, 0, 0, 0, 0, 0\n')

        for i in range(0, konec, 2):
            line += (f'  @ LINE_EP, 0 : {lxp - nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            line2 += (f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                      f'  @ LINE_EP, 0 : {dx1 + nachx}, {nachy + shag * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == konec - 1:
                break
            line += (f'  @ LINE_EP, 0 : {nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {lxp - nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            line2 += (f'  @ LINE_EP, 0 : {dx1 + nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                      f'  @ LINE_EP, 0 : lpx-{nachx}, {nachy + shag * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')

        txt_ss = txt_ss.replace("'vib1", line).replace("'vib2", line2)
        txt_ss = txt_ss.replace(f"{lxp - nachx}, {nachy}, {gl},", f"{lxp - nachx}, {nachy}, {gl - gl / 2},", 1)
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

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/107_it/xl.txt', 'r').read()
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
        txt_ss = txt_ss.replace(f"lpx-{nachx}, {nachy}, {gl},", f"lpx-{nachx}, {nachy}, {gl - gl / 2},", 1)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/92_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'ПСЯ' and int(visota) >= 133:
        txt_ss = open('rs/107_it/ps.txt', 'r').read()

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

    elif k[7] == 'Бутыл.' and int(visota) >= 133:
        txt_ss = open('rs/107_it/ps.txt', 'r').read()

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

    if k[9] == 'БПл':
        txt_ss = txt_ss.replace("0, 10.001, 0,", "0, 7, 0,")
        txt_ss = txt_ss.replace("0, 10.5, 0,", "0, 7.5, 0,")
    return txt_ss
