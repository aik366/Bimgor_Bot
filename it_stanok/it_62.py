from it_stanok import it_51


def it_62(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'Бутыл.', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8') or \
            (k[7] == 'Фасад' and int(visota) < 287):
        return it_51(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 23.301, 21.401, 14.101, 12.201, 12, 27.5, 6, 10.4, 1.4]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/62_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMX + oBv[2]
        rom, cy_temp, num = 50, ram, 0
        temp = int(visota) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {ram}, {cy}, 0\n'
        for i in range(0, rom_temp - 2, 2):
            s += (f"  @ LINE_EP, 0 : lpx-{ram}, {cy}+{rom}*{i}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : lpx-{ram}, {cy}+{rom}*{i + 1}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {ram}, {cy}+{rom}*{i + 1}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {ram}, {cy}+{rom}*{i + 2}, 0, 0, 0, 0, 0, 0, 0, 0\n")
        if rom_temp % 2:
            s = "\n".join(s.split("\n")[:-2]) + "\n"
        else:
            s += f"  @ LINE_EP, 0 : lpx-{ram}, {cy}+{rom}*{rom_temp - 2}, 0, 0, 0, 0, 0, 0, 0, 0\n"
        s += '  @ ENDPATH, 0 :\n\n\' NUM'
        txt_ss = txt_ss.replace("' TTTTT", s)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/62_it/xl.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMX + oBv[2]
        rom, cy_temp, num = 50, ram, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {cy}, {ram}, 0\n'
        for i in range(0, rom_temp - 2, 2):
            s += (f"  @ LINE_EP, 0 : {cy}+{rom}*{i}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 2}, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n")
        if rom_temp % 2:
            s = "\n".join(s.split("\n")[:-2]) + "\n"
        else:
            s += f"  @ LINE_EP, 0 : {cy}+{rom}*{rom_temp - 2}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
        s += '  @ ENDPATH, 0 :\n\n\' NUM'
        txt_ss = txt_ss.replace("' TTTTT", s)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))


    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/62_it/ps.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[1]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 50, 89, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'@ START_POINT, 0 : {cy}, {ram}, 0\n'
        for i in range(0, rom_temp - 2, 2):
            s += (f"  @ LINE_EP, 0 : {cy}+{rom}*{i}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 1}, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
                  f"  @ LINE_EP, 0 : {cy}+{rom}*{i + 2}, {ram}, 0, 0, 0, 0, 0, 0, 0, 0\n")
        if rom_temp % 2:
            s = "\n".join(s.split("\n")[:-2]) + "\n"
        else:
            s += f"  @ LINE_EP, 0 : {cy}+{rom}*{rom_temp - 2}, lpy-{ram}, 0, 0, 0, 0, 0, 0, 0, 0\n"
        s += '  @ ENDPATH, 0 :\n\n\' NUM'
        txt_ss = txt_ss.replace("' TTTTT", s)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        oBv[2] = oBv[0]
        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))


    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51_it/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)
        txt_ss = txt_ss.replace("OBV0", str(oBv[0]))


    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/51_it/pssl2.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("KANT", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51_it/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("KANT", Kant)

    return txt_ss
