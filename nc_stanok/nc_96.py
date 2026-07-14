oBv96nc = [27, 29, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 22, 19]


def nc_96(k, dlina, visota, RAM):
    txt_ss = ''
    konec, shag, gl = 0, 38.0, 8

    oBv = oBv96nc.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/96/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        nachy, nachx = RAMY + oBv[1] + 15, RAMX + oBv[1] + 15

        konec = int((int(visota) - 2 * nachy) / shag) + 1
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'$E0\nKP\nX={nachx}\nY={nachy}\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=l-{nachx}\nY=@0\n\n')
        num = 2
        for i in range(0, konec, 2):
            line += (f'$E{num}\nKL\nX=@0\nY={nachy + shag * (i + 1):.4f}\n\n'
                     f'$E{num + 1}\nKL\nX={nachx}\nY=@0\n\n')
            if i == konec - 1:
                break
            line += (f'$E{num + 2}\nKL\nX=@0\nY={nachy + shag * (i + 2):.4f}\n\n'
                     f'$E{num + 3}\nKL\nX=l-{nachx}\nY=@0\n\n')
            num += 4

        txt_ss = txt_ss.replace("gl_1", f"t-{gl/2}").replace("gl_2", f"t-{gl}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('shag', str(round(shag, 3)))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/96/st.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY = RAM[0], RAM[0]

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
        txt_ss = open('rs/96/per.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8

        txt_ss = txt_ss.replace('Lst', str((int(dlina) - 106 - 2 * zaz) / 3 + 106))
        txt_ss = txt_ss.replace('Wst', str((int(visota) - 106 - zaz) / 2 + 106))

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/96/per4.txt', 'r').read()
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8
        Lst = (int(dlina) - 106 - zaz) / 2 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        oBv[1] = oBv[7]
        txt_ss = open('rs/96/per8.txt', 'r').read()
        RAMX, RAMY, zaz = RAM[0], RAM[0], -8
        Lst = (int(dlina) - 106 - zaz*3) / 4 + 106
        Wst = (int(visota) - 106 - zaz) / 2 + 106

        txt_ss = txt_ss.replace("Lst", f'{Lst:.3f}')
        txt_ss = txt_ss.replace("Wst", f'{Wst:.3f}')
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 133:
        txt_ss = open('rs/96/ps.txt', 'r').read()
        RAMX, RAMY, shag = RAM[0], RAM[1], 15
        nachy, nachx = RAMY + oBv[1] + 10, RAMX + oBv[1] + 10

        if RAM[1] != 22.5 and int(visota) < 162:
            txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

        konec_temp = int((int(visota) - 2 * nachy) / shag) + 1
        konec = 1 if konec_temp == 0 else konec_temp
        shag = round((int(visota) - 2 * nachy) / konec, 4)

        line = (f'$E0\nKP\nX={nachx}\nY={nachy}\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=l-{nachx}\nY=@0\n\n')
        num = 2
        for i in range(0, konec, 2):
            line += (f'$E{num}\nKL\nX=@0\nY={nachy + shag * (i + 1):.4f}\n\n'
                     f'$E{num + 1}\nKL\nX={nachx}\nY=@0\n\n')
            if i == konec - 1:
                break
            line += (f'$E{num + 2}\nKL\nX=@0\nY={nachy + shag * (i + 2):.4f}\n\n'
                     f'$E{num + 3}\nKL\nX=l-{nachx}\nY=@0\n\n')
            num += 4

        txt_ss = txt_ss.replace("gl_1", f"t-{gl / 2}").replace("gl_2", f"t-{gl}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('shag', str(round(shag, 3)))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if RAM[4] == 1 and RAM[2] == 700.0:
        RAMX, RAMY = RAM[0], RAM[0]
        if k[7] in ('Фасад', 'Бутыл.', 'СТЕКЛО'):
            pod_92 = open('pl/92_f.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.5 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.5 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    if RAM[4] == 1 and RAM[2] != 700.0:
        txt_ss = txt_ss.replace('TNO="162_1"', 'EN="0"')
        txt_ss = txt_ss.replace('Z=t-5', f'Z=t-{int(RAM[2])}')
        txt_ss = txt_ss.replace('Z=t-8', f'Z=t-{int(RAM[2]) + 3}')

    if k[9] == "БПл":
        txt_ss = txt_ss.replace('Z=t-8', 'Z=t-5').replace('ZA="t-8"', 'ZA="t-5"')

    return txt_ss