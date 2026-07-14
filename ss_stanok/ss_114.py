def ss_114(k, dlina, visota, RAM):
    txt_ss = ''
    kray_dict = {"15": 14.0, "16": 10.5, "17": 12.0, "19": 12.0, "11": 20.0, "12": 17.0, "14": 20.0}

    nach = kray_dict[k[5]] if RAM[0] == 44.5 else RAM[0]
    rost = 14.0 if RAM[1] == 22.5 else RAM[1]
    glubina = 2.0 if RAM[2] > 10 else RAM[2]

    if k[7] in ('Фасад', 'Бутыл.'):
        txt_ss = open('rs/114/f.txt', 'r').read()

        konec = round((int(visota) - 2 * nach) / rost)
        shag = round((int(visota) - 2 * nach) / konec, 4)

        line = (f'$E0\nKP\nX=-20\nY={nach}\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=l+20\nY=@0\n\n')
        num = 2
        for i in range(0, konec, 2):
            line += (f'$E{num}\nKL\nX=@0\nY={nach + shag * (i + 1):.4f}\n\n'
                     f'$E{num + 1}\nKL\nX=-20\nY=@0\n\n')
            if i == konec - 1:
                break
            line += (f'$E{num + 2}\nKL\nX=-20\nY={nach + shag * (i + 2):.4f}\n\n'
                     f'$E{num + 3}\nKL\nX=l+20\nY=@0\n\n')
            num += 4

        txt_ss = txt_ss.replace("t-2", f"t-{glubina}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/114/f2.txt', 'r').read()

        konec = round((int(visota) - 2 * nach) / rost)
        shag = round((int(visota) - 2 * nach) / konec, 4)

        line = (f'$E0\nKP\nX=-20\nY={nach}\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX={str(RAM[2])}\nY=@0\n\n')
        num = 2
        for i in range(0, konec, 2):
            line += (f'$E{num}\nKL\nX=@0\nY={nach + shag * (i + 1):.4f}\n\n'
                     f'$E{num + 1}\nKL\nX=-20\nY=@0\n\n')
            if i == konec - 1:
                break
            line += (f'$E{num + 2}\nKL\nX=-20\nY={nach + shag * (i + 2):.4f}\n\n'
                     f'$E{num + 3}\nKL\nX={str(RAM[2])}\nY=@0\n\n')
            num += 4

        line_2 = (f'$E0\nKP\nX={str(RAM[2])}\nY=-20\nZ=t\nKO=0\n\n'
                  f'$E1\nKL\nX=@0\nY=w+20\n\n')

        txt_ss = txt_ss.replace("t-2", f"t-{glubina}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)
        txt_ss = txt_ss.replace("<vib2", line_2)
        txt_ss = txt_ss.replace("WEEKE BHC T.", "На Италянском тоже есть")

    elif k[7] in ('Хлеб', 'ПСЯ'):
        txt_ss = open('rs/114/f.txt', 'r').read()

        konec = round((int(dlina) - 2 * nach) / rost)
        shag = round((int(dlina) - 2 * nach) / konec, 4)

        line = (f'$E0\nKP\nX={nach}\nY=-20\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=@0\nY=w+20\n\n')
        num = 2
        for i in range(0, konec, 2):
            line += (f'$E{num}\nKL\nX={nach + shag * (i + 1):.4f}\nY=@0\n\n'
                     f'$E{num + 1}\nKL\nX=@0\nY=-20\n\n')
            if i == konec - 1:
                break
            line += (f'$E{num + 2}\nKL\nX={nach + shag * (i + 2):.4f}\nY=-20\n\n'
                     f'$E{num + 3}\nKL\nX=@0\nY=w+20\n\n')
            num += 4

        txt_ss = txt_ss.replace("t-2", f"t-{glubina}")
        txt_ss = txt_ss.replace("konec", f"{konec * 2 + 1}")
        txt_ss = txt_ss.replace("<vib1", line)

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss
