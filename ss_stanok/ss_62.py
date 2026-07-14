from ss_stanok import ss_51


def ss_62(k, dlina, visota, RAM):
    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'Бутыл.', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8') or \
            (k[7] == 'Фасад' and int(visota) < 287):
        return ss_51(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = [27, 33, 61.5, 13.6, 22.21, 12.2001, 20.7501, 12, 27.5, 19]
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == 'Фасад':
        txt_ss = open('rs/62/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMX + oBv[2]
        rom, cy_temp, num = 50, ram, 0
        temp = int(visota) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={ram}\nY={cy}\nZ=t\nKO=0\n\n'
        for i in range(0, rom_temp - 2, 2):
            num += 4
            s += (f"$E1\nKL\nX=l-{ram}\nY=@0\n\n$E2\nKL\nX=@0\nY={cy}+{rom}*{i + 1}\n\n"
                  f"$E3\nKL\nX={ram}\nY=@0\n\n$E4\nKL\nX=@0\nY={cy}+{rom}*{i + 2}\n\n")
        if rom_temp % 2:
            num -= 1
            s = "\n".join(s.split("\n")[:-7]) + "\n"
        else:
            num += 1
            s += f"$E5\nKL\nX=l-{ram}\nY=@0\n\n"
        txt_ss = txt_ss.replace("konec", f"{num}")
        txt_ss = txt_ss.replace("<vib1", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/62/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMX + oBv[2]
        rom, cy_temp, num = 50, ram, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={cy}\nY={ram}\nZ=t\nKO=0\n\n'
        for i in range(0, rom_temp - 2, 2):
            num += 4
            s += (f"$E1\nKL\nX=@0\nY=w-{ram}\n\n$E2\nKL\nX={cy}+{rom}*{i + 1}\nY=@0\n\n"
                  f"$E3\nKL\nX=@0\nY={ram}\n\n$E4\nKL\nX={cy}+{rom}*{i + 2}\nY=@0\n\n")
        if rom_temp % 2:
            num -= 1
            s = "\n".join(s.split("\n")[:-7]) + "\n"
        else:
            num += 1
            s += f"$E5\nKL\nX=@0\nY=w-{ram}\n\n"
        txt_ss = txt_ss.replace("konec", f"{num}")
        txt_ss = txt_ss.replace("<vib1", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/62/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 50, 89, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={cy}\nY={ram}\nZ=t\nKO=0\n\n'
        for i in range(0, rom_temp - 2, 2):
            num += 4
            s += (f"$E1\nKL\nX=@0\nY=w-{ram}\n\n$E2\nKL\nX={cy}+{rom}*{i + 1}\nY=@0\n\n"
                  f"$E3\nKL\nX=@0\nY={ram}\n\n$E4\nKL\nX={cy}+{rom}*{i + 2}\nY=@0\n\n")
        if rom_temp % 2:
            num -= 1
            s = "\n".join(s.split("\n")[:-7]) + "\n"
        else:
            num += 1
            s += f"$E5\nKL\nX=@0\nY=w-{ram}\n\n"
        txt_ss = txt_ss.replace("konec", f"{num}")
        txt_ss = txt_ss.replace("<vib1", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))


    elif k[7] == 'ПСЯ' and int(visota) >= 130 and int(visota) < 146:
        txt_ss = open('rs/51/pssl.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)
        txt_ss = txt_ss.replace("oBv0", str(oBv[0]))

    elif k[7] == 'ПСЯ' and int(visota) < 130:
        txt_ss = open('rs/51/pssl2.txt', 'r').read()
        RAMX, RAMY = 44.5, 26.5
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace("Kant", Kant)

    elif k[7] == 'Планка':
        txt_ss = open('rs/51/pl.txt', 'r').read()
        txt_ss = txt_ss.replace("Kant", Kant)

    return txt_ss
