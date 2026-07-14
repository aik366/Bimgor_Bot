def nc_blenda(k, dlina, visota, RAM):
    txt_ss = ''
    Kant = '10.4' if k[5] == '18' else '14.8'

    if k[7] == "Бленда1":
        txt_ss = open('rs/blenda/bl.txt', 'r').read()

        txt_ss = txt_ss.replace('tx1', '90')
        txt_ss = txt_ss.replace('tx2', '70')
        txt_ss = txt_ss.replace('tx3', '56.5')
        txt_ss = txt_ss.replace('tx4', '23.5')
        txt_ss = txt_ss.replace('tx5', '18.5')
        txt_ss = txt_ss.replace('rRr', '16.2')
        txt_ss = txt_ss.replace('Kant', Kant)

    elif k[7] == "Бленда2":
        txt_ss = open('rs/blenda/bl_2.txt', 'r').read()

    elif k[7] == "Бленда3":
        if "$" in k[8]:
            txt_ss = open('rs/blenda/bl_3_2.txt', 'r').read()
            txt_ss = txt_ss.replace('RAM', k[8].split('$')[1])
        else:
            txt_ss = open('rs/blenda/bl_3.txt', 'r').read()

    elif k[7] == "Бленда4":
        DX = (int(visota) - 2 * 7) / 4
        DY = 45 + (40 * 40 - DX * DX) ** 0.5
        txt_ss = open('rs/blenda/bl_4.txt', 'r').read()

        txt_ss = txt_ss.replace('DX', str(DX))
        txt_ss = txt_ss.replace('DY', str(DY))

    return txt_ss