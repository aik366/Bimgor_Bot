def it_123(k, dlina, visota, RAM):
    txt_ss = ''

    rad, obv0, obv1  = 12.7, 16.4, 14.5
    zaz = 2.6 if RAM[1] == 22.5 else RAM[1]
    vis = 2.0 if RAM[2] > 10 else RAM[2]
    rad = 12.7

    if k[7] == 'Фасад':
        txt_ss = open('rs/123_it/f.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[0]
        nach = RAMY + 26

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : {RAMX+obv0}, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{RAMX+obv0}, {nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{RAMX+obv0}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {RAMX+obv0}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {RAMX+obv0}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{RAMX+obv0}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace('RAMX', str(RAMX)).replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('OBV0', str(obv0)).replace('OBV1', str(obv1))

    elif k[7] == 'Бутыл.' and int(visota) >= 140:
        txt_ss = open('rs/123_it/f.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[1]
        nach = RAMY + 26

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(visota) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(visota) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : {RAMX + obv0}, {nach_sg}, 0\n'
                f'  @ LINE_EP, 0 : lpx-{RAMX + obv0}, {nach_sg}, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : lpx-{RAMX + obv0}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {RAMX + obv0}, {nach_sg + sg * (i + 1):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {RAMX + obv0}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : lpx-{RAMX + obv0}, {nach_sg + sg * (i + 2):.4f}, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace('RAMX', str(RAMX)).replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('OBV0', str(obv0)).replace('OBV1', str(obv1))

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/123_it/f.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[0]
        nach = RAMY + 26

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, {RAMY + obv0}, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{RAMY + obv0}, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace('RAMX', str(RAMX)).replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('OBV0', str(obv0)).replace('OBV1', str(obv1))

    elif k[7] == 'ПСЯ' and int(visota) >= 110:
        txt_ss = open('rs/123_it/f.txt', 'r').read()

        RAMX, RAMY = RAM[0], RAM[1]
        nach = RAMX + 26

        sg_temp = round(2 * (rad ** 2 - (rad - vis) ** 2) ** 0.5, 4)
        line_temp = round((int(dlina) - 2 * (nach - zaz / 2)) / (sg_temp + zaz))
        sg = round((int(dlina) - (2 * nach + zaz * (line_temp - 1))) / line_temp, 4)
        nach_sg = round(nach + sg / 2, 4)

        vis_sg = round(rad - (rad ** 2 - (sg / 2) ** 2) ** 0.5, 4)
        sg += zaz

        line = (f'  @ START_POINT, 0 : {nach_sg}, {RAMY + obv0}, 0\n'
                f'  @ LINE_EP, 0 : {nach_sg}, lpy-{RAMY + obv0}, {vis_sg}, 0, 0, 0, 0, 0, 0\n')
        for i in range(0, line_temp - 1, 2):
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, lpy-{RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 1):.4f}, {RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n')
            if i == line_temp - 2:
                break
            line += (f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, {RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n'
                     f'  @ LINE_EP, 0 : {nach_sg + sg * (i + 2):.4f}, lpy-{RAMY + obv0}, 0, 0, 0, 0, 0, 0, 0\n')
        txt_ss = txt_ss.replace("'vib1", line)
        txt_ss = txt_ss.replace('RAMX', str(RAMX)).replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('OBV0', str(obv0)).replace('OBV1', str(obv1))

    return txt_ss