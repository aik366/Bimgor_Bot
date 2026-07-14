def ss_74(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 32, 13.6, 22.21, 12.2001, 20.7501, 35.7, 28, 26.15]
    Txt65_1 = open('rs/74/39_1.txt', 'r').read()
    Txt65_2 = open('rs/74/39_2.txt', 'r').read()
    Txt65_3 = open('rs/74/39_3.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/74/f.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = round(RAMY + oBv[5] - 5.75, 3)
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = round((int(visota) - 8 - 2 * fy) / j * 3 / 4, 3)
        fx = round(fy - g, 3)
        ko = round(((int(dlina) - 2 * fx) / 16), 0)
        d = round((int(dlina) - 2 * fx) / ko * 3 / 4, 3)
        oBv[7] = round(fy - d - 11.25, 3)
        oBv[2] = round(fx - 11.25, 3)


        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), f'{oBv[i]:.3f}')

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{(j * 8 + 1):.0f}')
        txt_ss = txt_ss.replace("ko", f'{(ko * 8 + 1):.0f}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = 27.5
        txt_ss = open('rs/74/st.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = round(RAMY + oBv[5] - 5.75, 3)
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = round((int(visota) - 8 - 2 * fy) / j * 3 / 4, 3)
        fx = round(fy - g, 3)
        ko = round(((int(dlina) - 2 * fx) / 16), 0)
        d = round((int(dlina) - 2 * fx) / ko * 3 / 4, 3)
        oBv[7] = round(fy - d - 11.25, 3)
        oBv[2] = round(fx - 11.25, 3)

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{(j * 8 + 1):.0f}')
        txt_ss = txt_ss.replace("ko", f'{(ko * 8 + 1):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 155:
        txt_ss = open('rs/74/ps2.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[1] + 5
        fy = RAMY + 7
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = (int(visota) - 8 - 2 * fy) / j * 3 / 4
        fx = RAMX + 7 - g
        ko = round(((int(dlina) - 2 * fx) / 16), 0)
        d = (int(dlina) - 2 * fx) / ko * 3 / 4
        oBv[8] = fy - d - 6 - RAMY
        oBv[9] = oBv[8] - 1.85

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{(j * 8 + 1):.0f}')
        txt_ss = txt_ss.replace("ko", f'{(ko * 8 + 1):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 155:
        txt_ss = open('rs/74/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0] + 7.5, RAM[0] + 7.5
        fy = round(RAMY + oBv[5] - 5.75, 3)
        j = round(((int(visota) - 8 - 2 * fy) / 16), 0)
        g = round((int(visota) - 8 - 2 * fy) / j * 3 / 4, 3)
        fx = round(fy - g, 3)
        ko = round(((int(dlina) - 2 * fx) / 16), 0)
        d = round((int(dlina) - 2 * fx) / ko * 3 / 4, 3)
        oBv[7] = round(fy - d - 11.25, 3)
        oBv[2] = round(fx - 11.25, 3)

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), f'{oBv[i]:.3f}')

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("fx", f'{fx:.3f}')
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("fy", f'{fy:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{(j * 8 + 1):.0f}')
        txt_ss = txt_ss.replace("ko", f'{(ko * 8 + 1):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()


    return txt_ss