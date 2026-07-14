from it_stanok import it_91

oBv72it = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]


def it_72(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv72it.copy()
    if (k[7] == 'Фасад' and int(visota) < 250) or k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2',
                                                           'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ8', 'Бутыл.', 'Планка'):
        return it_91.it_91(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 290:
        txt_ss = open('rs/72_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 55, 100, 0
        temp = int(visota) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {ram}, {cy - 3}, 0\n'
        for i in range(rom_temp - 1):
            s += (f"  @ LINE_EP, 0 : lpx-{ram}, {cy}+{rom}*{i}-3, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : lpx-{ram}, {cy}+{rom}*{i}+3, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {ram}, {cy}+{rom}*{i}+3, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {ram}, {cy}+{rom}*{i + 1}-3, 0, 0, 0, 0, 0, 0, 0, 0\n")

        s = "\n".join(s.split("\n")[:-2]) + "\n"
        s += '  @ ENDPATH, 0 :\n\n'
        txt_ss = txt_ss.replace("' TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        return txt_ss

    elif k[7] == 'Фасад' and int(visota) >= 250:
        txt_ss = open('rs/72_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        s = (f'@ START_POINT, 0 : {RAMX + oBv[0]}, {int(visota) / 2 - 3}, 0\n'
             f'  @ LINE_EP, 0 : lpx-{RAMX + oBv[0]}, {int(visota) / 2 - 3}, 0, 0, 0, 0, 0, 0, 0, 0\n'
             f'  @ LINE_EP, 0 : lpx-{RAMX + oBv[0]}, {int(visota) / 2 + 3}, 0, 0, 0, 0, 0, 0, 0, 0\n'
             f'  @ LINE_EP, 0 : {RAMX + oBv[0]}, {int(visota) / 2 + 3}, 0, 0, 0, 0, 0, 0, 0, 0\n'
             f'  @ ENDPATH, 0 :\n\n')

        txt_ss = txt_ss.replace("' TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        return txt_ss


    elif k[7] == 'Хлеб':
        txt_ss = open('rs/72_it/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 55, 100, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {cy - 3}, {ram}, 0\n'
        for i in range(rom_temp - 1):
            s += (f"  @ LINE_EP, 0 : {cy}+{rom}*{i}-3, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i}+3, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i}+3, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}-3, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n")

        s = "\n".join(s.split("\n")[:-2]) + "\n"
        s += '  @ ENDPATH, 0 :\n\n'
        txt_ss = txt_ss.replace("' TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        return txt_ss

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/72_it/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 55, 89, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {cy - 3}, {ram}, 0\n'
        for i in range(rom_temp - 1):
            s += (f"  @ LINE_EP, 0 : {cy}+{rom}*{i}-3, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i}+3, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i}+3, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}-3, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n")

        s = "\n".join(s.split("\n")[:-2]) + "\n"
        s += '  @ ENDPATH, 0 :\n\n'
        txt_ss = txt_ss.replace("' TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

        return txt_ss

    elif k[7] == 'ПСЯ' and int(visota) < 146:
        txt_ss = open('rs/91_it/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
