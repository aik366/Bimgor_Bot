def ss_120(k, dlina, visota, RAM):
    txt_ss = ''
    kray_dict = {"15": 7.0, "16": 3, "17": 5.0, "19": 5.0}

    nach = kray_dict[k[5]] if RAM[0] == 44.5 else RAM[0]
    zaz = 2.6 if RAM[1] == 22.5 else RAM[1]
    vis = 4.5 if RAM[2] > 10 else RAM[2]
    rad = 12.7

    if k[7] in ('Фасад', 'Бутыл.'):
        txt_ss = open('rs/119/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'$E0\nKP\nX=-20\nY={nach_sg}\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=l+20\nY=@0\n\n')
        num = 2
        for i in range(0, line_temp - 1, 2):
            line += (f'$E{num}\nKL\nX=@0\nY={nach_sg + sg * (i + 1):.4f}\n\n'
                     f'$E{num + 1}\nKL\nX=-20\nY=@0\n\n')
            if i == line_temp - 2:
                break
            line += (f'$E{num + 2}\nKL\nX=-20\nY={nach_sg + sg * (i + 2):.4f}\n\n'
                     f'$E{num + 3}\nKL\nX=l+20\nY=@0\n\n')
            num += 4

        txt_ss = txt_ss.replace("t-2", f"t-{vis_sg}")
        txt_ss = txt_ss.replace("konec", f"{line_temp * 2 - 1}")
        txt_ss = txt_ss.replace("<vib1", line)

    elif k[7] in ('Хлеб', 'ПСЯ'):
        txt_ss = open('rs/119/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'$E0\nKP\nX={nach_sg}\nY=-20\nZ=t\nKO=0\n\n'
                f'$E1\nKL\nX=@0\nY=w+20\n\n')
        num = 2
        for i in range(0, line_temp - 1, 2):
            line += (f'$E{num}\nKL\nX={nach_sg + sg * (i + 1):.4f}\nY=@0\n\n'
                     f'$E{num + 1}\nKL\nX=@0\nY=-20\n\n')
            if i == line_temp - 2:
                break
            line += (f'$E{num + 2}\nKL\nX={nach_sg + sg * (i + 2):.4f}\nY=-20\n\n'
                     f'$E{num + 3}\nKL\nX=@0\nY=w+20\n\n')
            num += 4

        txt_ss = txt_ss.replace("t-2", f"t-{vis_sg}")
        txt_ss = txt_ss.replace("konec", f"{line_temp * 2 - 1}")
        txt_ss = txt_ss.replace("<vib1", line)

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    return txt_ss
