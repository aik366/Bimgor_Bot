def it_77(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6]
    Txt65_1 = open('rs/77_it/96_1.txt', 'r').read()
    Txt65_2 = open('rs/77_it/96_2.txt', 'r').read()
    Txt65_3 = open('rs/77_it/96_3.txt', 'r').read()
    Txt65_4 = open('rs/77_it/96_4.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/77_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, n = RAMX + oBv[6] - 6, 12
        fx, fy, f2x, f2y = f, f, f, f
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * f) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * f - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fx = fx + d + d / 4
            f2x = f2x + d + d / 4

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 4
            f2y = f2y + g + g / 4

        oBv[8] = round((f - d - 6) - RAMX - 1.7, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/77_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, n = RAMX + oBv[6] - 6, 12
        fx, fy, f2x, f2y = f, f, f, f
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * f) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * f - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fx = fx + d + d / 4
            f2x = f2x + d + d / 4

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 4
            f2y = f2y + g + g / 4

        oBv[8] = round((f - d - 6) - RAMX - 1.7, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 160:
        txt_ss = open('rs/77_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, n = RAMX + oBv[6] - 6, 12
        u = RAMY + oBv[6] - 6
        fx, fy, f2x, f2y = f, u, f, u
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * u) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * u - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{u:.3f}')
            fx = fx + d + d / 4
            f2x = f2x + d + d / 4

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 4
            f2y = f2y + g + g / 4

        oBv[8] = round((f - d - 6) - RAMX - 1.7, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("u", f'{u:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 160:
        txt_ss = open('rs/77_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, n = RAMX + oBv[6] - 6, 12
        u = RAMY + oBv[6] - 6
        fx, fy, f2x, f2y = f, u, f, u
        ko = round(((int(dlina) - 2 * f) / n), 0)
        j = round(((int(visota) - 2 * f) / n), 0)
        h = (int(dlina) - 2 * f) / ko * 4 / 5
        m = (int(visota) - 2 * u) / j * 4 / 5
        d = (int(dlina) - 2 * f - h / 2) / ko * 4 / 5
        g = (int(visota) - 2 * u - m / 2) / j * 4 / 5

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{u:.3f}')
            fx = fx + d + d / 4
            f2x = f2x + d + d / 4

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 4
            f2y = f2y + g + g / 4

        oBv[8] = round((f - d - 6) - RAMX - 1.7, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("u", f'{u:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()
        
    if '77/1' in k[8]:
        txt_ss = txt_ss.replace('@ ROUT, 0 : "144_1"', "'" + ' ROUT, 0 : "144_1"')
        txt_ss = txt_ss.replace('@ ROUT, 0 : "150_1"', "'" + ' ROUT, 0 : "150_1"')

    return txt_ss