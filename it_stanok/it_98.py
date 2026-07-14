from it_stanok import it_96
from tkinter.messagebox import showinfo

def it_98(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_96(k, dlina, visota, RAM)
    konec, shag, gl = 0, 38, 11
    D = 26
    oBv = [D, 29, D-13, D-3.701, D-5.601, D-17.7, D-19.6, 0, D+0.5, 22]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/98_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7, RAM[0] + 7
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
        txt_ss = open('rs/98_it/f2.txt', 'r').read()
        RAMX, RAMY, lxp, zaz = RAM[0] + 7, RAM[0] + 7, RAM[2], 36
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

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/98_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7, RAM[0] + 7
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 133:
        txt_ss = open('rs/98_it/ps.txt', 'r').read()
        RAMX = RAM[0] + 7
        RAMY = RAM[1] + 7 if RAM[1] != 22.5 else RAM[1]
        nachy, nachx, shag = RAMY + oBv[1] + 10, RAMX + oBv[1] + 10, 15

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
        txt_ss = txt_ss.replace("11, 0, 0, 0, 0, 0", "8, 0, 0, 0, 0, 0,")
    return txt_ss