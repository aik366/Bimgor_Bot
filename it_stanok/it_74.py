def it_74(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 32.8, 27.5, 34.8]
    Txt39_1 = open('rs/74_it/39_1.txt', 'r').read()
    Txt39_2 = open('rs/74_it/39_2.txt', 'r').read()
    Txt39_3 = open('rs/74_it/39_3.txt', 'r').read()
    Txt39_4 = open('rs/74_it/39_4.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/74_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = RAMY + oBv[6] - 5.75
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = (int(visota) - 8 - 2 * fy) / j * 3 / 4
        fx = fy - g
        k = round(((int(dlina) - 2 * fx) / 16), 0)
        d = (int(dlina) - 2 * fx) / k * 3 / 4
        f1x, f1y = fx, fy
        oBv[9] = fy - d - 11.25
        oBv[8] = fx - 11.25

        for _ in range(int(k)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt39_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt39_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f1x", f'{f1x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1x = f1x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt39_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt39_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f1y", f'{f1y:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1y = f1y + g + g / 3

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[8]
        txt_ss = open('rs/74_it/st.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = RAMY + oBv[6] - 5.75
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = (int(visota) - 8 - 2 * fy) / j * 3 / 4
        fx = fy - g
        k = round(((int(dlina) - 2 * fx) / 16), 0)
        d = (int(dlina) - 2 * fx) / k * 3 / 4
        f1x, f1y = fx, fy
        oBv[9] = fy - d - 11.25
        oBv[8] = fx - 11.25

        for _ in range(int(k)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt39_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt39_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f1x", f'{f1x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1x = f1x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt39_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt39_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f1y", f'{f1y:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1y = f1y + g + g / 3

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 155:
        txt_ss = open('rs/74_it/ps2.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[1] + 5
        fy = RAMY + oBv[6] - 5.75
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = (int(visota) - 8 - 2 * fy) / j * 3 / 4
        fx = RAMX + 7 - g
        k = round(((int(dlina) - 2 * fx) / 16), 0)
        d = (int(dlina) - 2 * fx) / k * 3 / 4
        f1x, f1y = fx, fy
        oBv[3] = -13.6
        oBv[4] = oBv[3] - 1.9

        for _ in range(int(k)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt39_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt39_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f1x", f'{f1x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1x = f1x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt39_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt39_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f1y", f'{f1y:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1y = f1y + g + g / 3

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 155:
        txt_ss = open('rs/74_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = RAMY + oBv[6] - 5.75
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = (int(visota) - 8 - 2 * fy) / j * 3 / 4
        fx = fy - g
        k = round(((int(dlina) - 2 * fx) / 16), 0)
        d = (int(dlina) - 2 * fx) / k * 3 / 4
        f1x, f1y = fx, fy
        oBv[9] = fy - d - 11.25
        oBv[8] = fx - 11.25

        for _ in range(int(k)):
            txt_ss = txt_ss.replace("'TTTT1", str(Txt39_1))
            txt_ss = txt_ss.replace("'TTTT3", str(Txt39_3))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("f1x", f'{f1x:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1x = f1x + d + d / 3

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("'TTTT2", str(Txt39_2))
            txt_ss = txt_ss.replace("'TTTT4", str(Txt39_4))
            txt_ss = txt_ss.replace("d", f'{d:.3f}')
            txt_ss = txt_ss.replace("g", f'{g:.3f}')
            txt_ss = txt_ss.replace("f1y", f'{f1y:.3f}')
            txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
            txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
            f1y = f1y + g + g / 3

        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss