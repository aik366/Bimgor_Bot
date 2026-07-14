from it_stanok import it_109


def it_110(k, dlina, visota, RAM):
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return it_109(k, dlina, visota, RAM)

    txt_ss = ''
    konec, shag, gl = 0, 38, 10.001
    D = 26
    oBv = [D, 29, D - 28.5, D - 4.601, D - 5.601, 0, D - 6.501, 0, 22, -2.9]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/110_it/f.txt', 'r').read()
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

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/109_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
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
        txt_ss = open('rs/110_it/ps.txt', 'r').read()

        RAMX, RAMY, shag = RAM[0], RAM[1], 15
        nachy, nachx = RAMY + oBv[1] + 10, RAMX + oBv[1] + 10

        if RAM[1] != 22.5:
            txt_ss = txt_ss.replace('\' ROUT, 0 : "144_1"', '@ ROUT, 0 : "144_1"', 1)
            if int(visota) < 162:
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
        txt_ss = txt_ss.replace("10.001, 0, 0, 0, 0, 0", "7, 0, 0, 0, 0, 0,")
    return txt_ss
