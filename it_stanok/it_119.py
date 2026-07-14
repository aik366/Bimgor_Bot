def it_119(k, dlina, visota, RAM):
    txt_ss = ''
    kray_dict = {"15": 7.0, "16": 3, "17": 5.0, "19": 5.0}

    nach = kray_dict[k[5]] if RAM[0] == 44.5 else RAM[0]
    zaz = 2.6 if RAM[1] == 22.5 else RAM[1]
    vis = 4.5 if RAM[2] > 10 else RAM[2]
    rad = 12.7

    if k[7] in ('Фасад', 'Бутыл.'):
        txt_ss = open('rs/119_it/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : -20, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : lpx+20, {nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : lpx+20, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : -20, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : -20, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx+20, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] in ('Хлеб', 'ПСЯ'):
        txt_ss = open('rs/119_it/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, -20, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy+20, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy+20, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, -20, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, -20, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy+20, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss
