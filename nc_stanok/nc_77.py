def nc_77(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]
    Txt65_1 = open('rs/77/96_1.txt', 'r').read()
    Txt65_2 = open('rs/77/96_2.txt', 'r').read()
    Txt65_3 = open('rs/77/96_3.txt', 'r').read()
    Txt65_4 = open('rs/77/96_4.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/77/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, n = RAMX + oBv[5] - 6, 12
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * f) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * f - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round((f - d - 6) - RAMX - 1.15, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 2 * 9 + 28):.0f}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/77/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, n = RAMX + oBv[5] - 6, 12
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * f) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * f - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round((f - d - 6) - RAMX - 1.15, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 2 * 9 + 28):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 160:
        txt_ss = open('rs/77/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, u, n = RAMX + oBv[5] - 6, RAMY + 6.5, 12
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * u) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * u) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * u - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round((f - d - 6) - RAMX - 1.15, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("u", f'{u:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 2 * 9 + 28):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 160:
        txt_ss = open('rs/77/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, u, n = RAMX + oBv[5] - 6, RAMY + 6.5, 12
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * u) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * u) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * u - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round((f - d - 6) - RAMX - 1.15, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("u", f'{u:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 2 * 9 + 28):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()
        
    if '77/1' in k[8]:
        txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

    return txt_ss