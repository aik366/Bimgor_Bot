import math
from it_stanok import it_96


def it_100(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_96(k, dlina, visota, RAM)

    txt_ss = ''
    konec, shag, gl = 0, 38, 6
    D = 26
    oBv = [D, 29, D + 34.5, D - 3.701, D - 5.601, D - 12.901, D - 14.801, D - 15, D + 0.5, 22]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/100_it/f.txt', 'r').read()
        RAMX = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[4] + 2.9, 3)
        RAMY = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[4] + 2.9, 3)

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

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 100:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 100:
        txt_ss = open('rs/100_it/ps.txt', 'r').read()
        RAMX = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[4] + 2.9, 3)
        RAMY = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[4] + 2.9, 3)
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

    if RAM[4] == 1:
        txt_ss = txt_ss.replace(", 3, 0, 0, 0,", ", 5, 0, 0, 0,")
        if k[9] == 'БПл':
            txt_ss = txt_ss.replace("6, 0, 0, 0, 0, 0", "5, 0, 0, 0, 0, 0,")
        else:
            txt_ss = txt_ss.replace("6, 0, 0, 0, 0, 0", "8, 0, 0, 0, 0, 0,")

    if k[9] == 'БПл':
        txt_ss = txt_ss.replace("6, 0, 0, 0, 0, 0", "3, 0, 0, 0, 0, 0,")

    return txt_ss