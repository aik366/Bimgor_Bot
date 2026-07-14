from nc_stanok import nc_91

oBv72nc = [27, 33, 61.5, 13.6001, 22.3001, 11.7301, 20.4301, 27.5, 10.6, 19]


def nc_72(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = oBv72nc.copy()
    if (k[7] == 'Фасад' and int(visota) < 250) or k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2',
                                                           'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ8', 'Бутыл.', 'Планка'):
        return nc_91.nc_91(k, dlina, visota, RAM)

    elif k[7] == 'Фасад' and int(visota) >= 290:
        txt_ss = open('rs/72/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMX + oBv[0]
        rom, cy_temp, num = 55, 100, 0
        temp = int(visota) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={ram}\nY={cy-3}\nZ=t\nKO=0\n\n'
        for i in range(rom_temp - 1):
            num += 4
            s += (f"$E1\nKL\nX=l-{ram}\nY=@0\n\n$E2\nKL\nX=@0\nY={cy}+{rom}*{i}+3\n\n"
                  f"$E3\nKL\nX={ram}\nY=@0\n\n$E4\nKL\nX=@0\nY={cy}+{rom}*{i + 1}-3\n\n")

        s = "\n".join(s.split("\n")[:-7]) + "\n"

        txt_ss = txt_ss.replace("konec", f"{num-1}")
        txt_ss = txt_ss.replace("\TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
        return txt_ss

    elif k[7] == 'Фасад' and int(visota) >= 250:
        txt_ss = open('rs/72/f.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[0]

        s = (f'$E0\nKP\nX={RAMX+oBv[0]}\nY={int(visota)/2 - 3}\nZ=t\nKO=0\n\n'
             f'$E1\nKL\nX=l-{RAMX+oBv[0]}\nY=@0\n\n$E2\nKL\nX=@0\nY={int(visota)/2 + 3}\n\n'
             f'$E3\nKL\nX={RAMX+oBv[0]}\nY=@0\n\n')
        txt_ss = txt_ss.replace('\TTTTT', s)
        txt_ss = txt_ss.replace("konec", "3")

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/72/xl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 55, 100, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={cy-3}\nY={ram}\nZ=t\nKO=0\n\n'
        for i in range(rom_temp - 1):
            num += 4
            s += (f"$E1\nKL\nX=@0\nY=w-{ram}\n\n$E2\nKL\nX={cy}+{rom}*{i}+3\nY=@0\n\n"
                  f"$E3\nKL\nX=@0\nY={ram}\n\n$E4\nKL\nX={cy}+{rom}*{i + 1}-3\nY=@0\n\n")

        s = "\n".join(s.split("\n")[:-7]) + "\n"

        txt_ss = txt_ss.replace("konec", f"{num-1}")
        txt_ss = txt_ss.replace("\TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
        return txt_ss

    elif k[7] == 'ПСЯ' and int(visota) >= 146:
        txt_ss = open('rs/72/ps.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        ram = RAMY + oBv[0]
        rom, cy_temp, num = 55, 89, 0
        temp = int(dlina) - cy_temp * 2
        rom_temp = round(temp / rom)
        rom = round(temp / rom_temp, 3)
        cy = round(cy_temp + rom, 3)
        s = f'$E0\nKP\nX={cy - 3}\nY={ram}\nZ=t\nKO=0\n\n'
        for i in range(rom_temp - 1):
            num += 4
            s += (f"$E1\nKL\nX=@0\nY=w-{ram}\n\n$E2\nKL\nX={cy}+{rom}*{i}+3\nY=@0\n\n"
                  f"$E3\nKL\nX=@0\nY={ram}\n\n$E4\nKL\nX={cy}+{rom}*{i + 1}-3\nY=@0\n\n")

        s = "\n".join(s.split("\n")[:-7]) + "\n"

        txt_ss = txt_ss.replace("konec", f"{num - 1}")
        txt_ss = txt_ss.replace("\TTTTT", s)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))
        return txt_ss

    elif k[7] == 'ПСЯ' and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss
