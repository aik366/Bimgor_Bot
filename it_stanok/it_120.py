def it_120(k, dlina, visota, RAM):
    txt_ss = ''

    nach, zaz, vis, rad, nach_zaz = 56.6, 2.6, 3, 12.7, 4.6

    if k[7] == 'Фасад':
        txt_ss = open('rs/120_it/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)

        txt_ss = txt_ss.replace("RAMX", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RAMY", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RRAM", f"{sg / 2 + nach_zaz}")

        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg + sg * (i + 1):.4f}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg}, {nach_sg + sg * (i + 1):.4f}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg}, {nach_sg + sg * (i + 2):.4f}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_sg}, {nach_sg + sg * (i + 2):.4f}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'Бутыл.' and int(visota) >= 140:
        txt_ss = open('rs/120_it/f.txt', 'r').read()
        nach = nach - 22

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)
        nach_x = nach_sg + 22

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)

        txt_ss = txt_ss.replace("RAMX", f"{nach_x - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RAMY", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RRAM", f"{sg / 2 + nach_zaz}")

        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_x}, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n'
                f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg + sg * (i + 1):.4f}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_x}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_x}, {nach_sg + sg * (i + 1):.4f}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_x}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_x}, {nach_sg + sg * (i + 2):.4f}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{nach_x}, {nach_sg + sg * (i + 2):.4f}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/120_it/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)

        txt_ss = txt_ss.replace("RAMX", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RAMY", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RRAM", f"{sg / 2 + nach_zaz}")

        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{nach_sg}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{nach_sg}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{nach_sg}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {nach_sg}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {nach_sg}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {nach_sg}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {nach_sg}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{nach_sg}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{nach_sg}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    elif k[7] == 'ПСЯ' and int(visota) >= 117:
        txt_ss = open('rs/120_it/f.txt', 'r').read()

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)
        nach_y = nach_sg - 22

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)

        txt_ss = txt_ss.replace("RAMX", f"{nach_sg - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RAMY", f"{nach_y - sg / 2 - nach_zaz}")
        txt_ss = txt_ss.replace("RRAM", f"{sg / 2 + nach_zaz}")

        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, {nach_y}, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{nach_y}, {vis_sg}, 0, 0, 0, 0, 0, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{nach_y}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{nach_y}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{nach_y}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {nach_y}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {nach_y}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {nach_y}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {nach_y}, {vis_sg+5}, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{nach_y}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{nach_y}, -{vis_sg+5}, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)

    return txt_ss