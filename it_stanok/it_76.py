def it_76(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6]
    Txt65_1 = open('rs/76_it/96_1.txt', 'r').read()
    Txt65_2 = open('rs/76_it/96_2.txt', 'r').read()
    Txt65_3 = open('rs/76_it/96_3.txt', 'r').read()
    Txt65_4 = open('rs/76_it/96_4.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/76_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, v = RAMX + oBv[6] - 15, 16
        fx, fy, f2x, f2y = f + v / 2, f + v / 2, f + v / 2, f + v / 2
        ko = round(((int(dlina) - 2 * f - v) / v), 0)
        j = round(((int(visota) - 2 * f - v) / v), 0)
        d = (int(dlina) - 2 * f - v) / ko * 3 / 4
        g = (int(visota) - 2 * f - v) / j * 3 / 4

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fx = fx + d + d / 3
            f2x = f2x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 3
            f2y = f2y + g + g / 3

        oBv[8] = round(f - 50.5 - 1.15, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('v', str(v))
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/76_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f, v = RAMX + oBv[6] - 15, 16
        fx, fy, f2x, f2y = f + v / 2, f + v / 2, f + v / 2, f + v / 2
        ko = round(((int(dlina) - 2 * f - v) / v), 0)
        j = round(((int(visota) - 2 * f - v) / v), 0)
        d = (int(dlina) - 2 * f - v) / ko * 3 / 4
        g = (int(visota) - 2 * f - v) / j * 3 / 4

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fx = fx + d + d / 3
            f2x = f2x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 3
            f2y = f2y + g + g / 3

        oBv[8] = round(oBv[6] - 22, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('v', str(v))
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 160:
        txt_ss = open('rs/76_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, v, m = RAMX + oBv[6] - 15, 16, RAMY + oBv[6] - 15
        fx, fy, f2x, f2y = f + v / 2, m + v / 2, f + v / 2, m + v / 2
        ko = round(((int(dlina) - 2 * f - v) / v), 0)
        j = round(((int(visota) - 2 * m - v) / v), 0)
        d = (int(dlina) - 2 * f - v) / ko * 3 / 4
        g = (int(visota) - 2 * m - v) / j * 3 / 4

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{m:.3f}')
            fx = fx + d + d / 3
            f2x = f2x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 3
            f2y = f2y + g + g / 3

        oBv[8] = round(oBv[6] - 22, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('v', str(v))
        txt_ss = txt_ss.replace("m", f'{m:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 160:
        txt_ss = open('rs/76_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, v, m = RAMX + oBv[6] - 15, 16, RAMY + oBv[6] - 15
        fx, fy, f2x, f2y = f + v / 2, m + v / 2, f + v / 2, m + v / 2
        ko = round(((int(dlina) - 2 * f - v) / v), 0)
        j = round(((int(visota) - 2 * m - v) / v), 0)
        d = (int(dlina) - 2 * f - v) / ko * 3 / 4
        g = (int(visota) - 2 * m - v) / j * 3 / 4

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            txt_ss = txt_ss.replace("'TTTT1", str(Txt65_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt65_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f2x", f'{f2x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("f", f'{m:.3f}')
            fx = fx + d + d / 3
            f2x = f2x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt65_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt65_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f2y", f'{f2y:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            txt_ss = txt_ss.replace("f", f'{f:.3f}')
            fy = fy + g + g / 3
            f2y = f2y + g + g / 3

        oBv[8] = round(oBv[6] - 22, 3)
        oBv[9] = round(oBv[8] - (oBv[3] - oBv[4]), 3)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('v', str(v))
        txt_ss = txt_ss.replace("m", f'{m:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.3f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()
        
    if '76/1' in k[8]:
        txt_ss = txt_ss.replace('@ ROUT, 0 : "144_1"', "'" + ' ROUT, 0 : "144_1"')
        txt_ss = txt_ss.replace('@ ROUT, 0 : "150_1"', "'" + ' ROUT, 0 : "150_1"')

    return txt_ss
