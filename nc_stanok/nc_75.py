def nc_75(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]
    Txt65_1 = open('rs/75/65_1.txt', 'r').read()
    Txt65_2 = open('rs/75/65_2.txt', 'r').read()
    Txt65_3 = open('rs/75/65_3.txt', 'r').read()
    Txt65_4 = open('rs/75/65_4.txt', 'r').read()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/75/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f = RAMX + oBv[5] - 7.7
        ko = round(((int(dlina) - 2 * f) / 9), 0)
        j = round(((int(visota) - 2 * f) / 9), 0)
        d = (int(dlina) - 2 * f) / ko
        g = (int(visota) - 2 * f) / j

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round(f - 58.3, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.0f}')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/75/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        f = RAMX + oBv[5] - 7.7
        ko = round(((int(dlina) - 2 * f) / 9), 0)
        j = round(((int(visota) - 2 * f) / 9), 0)
        d = (int(dlina) - 2 * f) / ko
        g = (int(visota) - 2 * f) / j

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round(f - 58.3, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and 120 <= int(visota) < 160:
        txt_ss = open('rs/75/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, m = RAMX + oBv[5] - 7.7, RAMY + 2.8
        ko = round(((int(dlina) - 2 * f) / 9), 0)
        j = round(((int(visota) - 2 * m) / 9), 0)
        d = (int(dlina) - 2 * f) / ko
        g = (int(visota) - 2 * m) / j

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round(f - 58.3, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("m", f'{m:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 160:
        txt_ss = open('rs/75/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1] + 8
        f, m = RAMX + oBv[5] - 7.7, RAMY + 2.8
        ko = round(((int(dlina) - 2 * f) / 9), 0)
        j = round(((int(visota) - 2 * m) / 9), 0)
        d = (int(dlina) - 2 * f) / ko
        g = (int(visota) - 2 * m) / j

        for _ in range(int(ko)):
            txt_ss = txt_ss.replace("\TTTT1\\", str(Txt65_1))
            txt_ss = txt_ss.replace("\TTTT2\\", str(Txt65_2))

        for _ in range(int(j)):
            txt_ss = txt_ss.replace("\TTTT3\\", str(Txt65_3))
            txt_ss = txt_ss.replace("\TTTT4\\", str(Txt65_4))

        oBv[8] = round(f - 58.3, 3)
        oBv[9] = round(oBv[8] - 1.85, 3)

        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("d", f'{d:.3f}')
        txt_ss = txt_ss.replace("m", f'{m:.3f}')
        txt_ss = txt_ss.replace("f", f'{f:.3f}')
        txt_ss = txt_ss.replace("g", f'{g:.3f}')
        txt_ss = txt_ss.replace("j", f'{((j + ko) * 10 + 11):.0f}')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 120:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()
        
    if '75/1' in k[8]:
        txt_ss = txt_ss.replace('EN="1"', 'EN="0"')

    return txt_ss