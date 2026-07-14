from ss_stanok import ss_96


def ss_100(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return ss_96(k, dlina, visota, RAM)

    txt_ss = ''
    konec, shag, gl = 0, 38.0, 6

    oBv = [27, 29, 61.5, 13.6, 22.21, 12.2001, 20.7501, 27.5, 22, 19]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/100/f.txt', 'r').read()
        RAMX = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[6] + 3, 3)
        RAMY = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[6] + 3, 3)
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

        txt_ss = txt_ss.replace("gl", f"t-{gl}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('shag', str(round(shag, 3)))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 100:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 100:
        txt_ss = open('rs/100/ps.txt', 'r').read()
        RAMX = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[6] + 3, 3)
        RAMY = RAM[0] - 42.5 if RAM[0] == 44.5 else round(RAM[0] - oBv[6] + 3, 3)
        nachy, nachx, shag = RAMY + oBv[1] + 10, RAMX + oBv[1] + 10, 15

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

        txt_ss = txt_ss.replace("gl", f"t-{gl}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('shag', str(round(shag, 3)))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if RAM[4] == 1:
        txt_ss = txt_ss.replace('Z=t-3', 'Z=t-5')
        if k[9] == 'БПл':
            txt_ss = txt_ss.replace('Z=t-6', 'Z=t-5').replace('ZA="t-6"', 'ZA="t-5"')
        else:
            txt_ss = txt_ss.replace('Z=t-6', 'Z=t-8')

    if k[9] == 'БПл':
        txt_ss = txt_ss.replace('Z=t-6', 'Z=t-3').replace('ZA="t-6"', 'ZA="t-3"')

    return txt_ss