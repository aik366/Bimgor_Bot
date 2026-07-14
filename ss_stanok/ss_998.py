def ss_998(k, dlina, visota, RAM):
    txt_ss = ''

    if k[7] in ('Фасад', 'Хлеб', 'ПСЯ', 'Бутыл.'):
        with open('rs/998/f.txt', 'r') as f:
            txt_ss = f.read()
            Kant = '10.4' if k[5] == '18' else '14.8'
            txt_ss = txt_ss.replace("Kant", Kant)
            if "72_txt" in txt_ss:
                if k[7] in ('Фасад', 'Бутыл.'):
                    ram = 71.5 if RAM[2] == 700.0 else RAM[2]
                    rom, cy_temp, num = RAM[1], RAM[0], 0
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
                    txt_ss = txt_ss.replace("72_txt", s)
                elif k[7] in ('Хлеб', 'ПСЯ'):
                    ram = 71.5 if RAM[2] == 700.0 else RAM[2]
                    rom, cy_temp, num = RAM[1], RAM[0], 0
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
                    txt_ss = txt_ss.replace("72_txt", s)

    return txt_ss
