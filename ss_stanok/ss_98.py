from ss_stanok import ss_96


def ss_98(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return ss_96(k, dlina, visota, RAM)
    konec, shag, gl = 0, 38.0, 11

    oBv = [27, 29, 14, 9.21, 22.21, 7.75, 20.7501, 27.5, 22, 19]

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/98/f.txt', 'r').read()
        RAMX, RAMY= RAM[0] + 7, RAM[0] + 7
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

        txt_ss = txt_ss.replace("gl_1", f"t-{gl / 2}").replace("gl_2", f"t-{gl}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('shag', str(round(shag, 3)))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/98/st.txt', 'r').read()
        oBv[1] = oBv[7]
        RAMX, RAMY= RAM[0] + 7, RAM[0] + 7

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 133:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 133:
        txt_ss = open('rs/98/ps.txt', 'r').read()
        RAMX = RAM[0] + 7
        RAMY = RAM[1] + 7 if RAM[1] != 22.5 else RAM[1]
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

    if k[9] == "БПл":
        txt_ss = txt_ss.replace('Z=t-11', 'Z=t-8').replace('ZA="t-11"', 'ZA="t-8"')


    return txt_ss