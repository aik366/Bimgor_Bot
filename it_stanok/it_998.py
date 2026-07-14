def it_998(k, dlina, visota, RAM):
    txt_ss = ''

    if k[7] in ('Фасад', 'Хлеб', 'ПСЯ', 'Бутыл.'):
        with open('rs/998_it/f.txt', 'r') as f:
            txt_ss = f.read()
            Kant = '10.4' if k[5] == '18' else '14.8'
            txt_ss = txt_ss.replace("KANT", Kant)
            if "72_txt" in txt_ss:
                if k[7] in ('Фасад', 'Бутыл.'):
                    ram = 71.5 if RAM[2] == 700.0 else RAM[2]
                    rom, cy_temp, num = RAM[1], RAM[0], 0
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
                    txt_ss = txt_ss.replace("72_txt", s)
                elif k[7] in ('Хлеб', 'ПСЯ'):
                    ram = 71.5 if RAM[2] == 700.0 else RAM[2]
                    rom, cy_temp, num = RAM[1], RAM[0], 0
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
                    txt_ss = txt_ss.replace("72_txt", s)

    return txt_ss
