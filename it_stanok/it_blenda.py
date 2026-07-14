def it_blenda(k, dlina, visota, RAM):
    txt_it = ''

    if k[7] == "Бленда3":
        if "$" in k[8]:
            txt_it = open('rs/blenda/bl_3_2_it.txt', 'r').read()
            txt_it = txt_it.replace('RAM', k[8].split('$')[1])
        else:
            txt_it = open('rs/blenda/bl_3_it.txt', 'r').read()

    elif k[7] == "Бленда2":
        txt_it = open('rs/blenda/bl_2_it.txt', 'r').read()

    elif k[7] == "Бленда4":
        DX = (int(visota) - 2 * 7) / 4
        DY = 45 + (40 * 40 - DX * DX) ** 0.5
        txt_it = open('rs/blenda/bl_4_it.txt', 'r').read()

        txt_it = txt_it.replace('DX', f"{DX:.4f}")
        txt_it = txt_it.replace('DY', f"{DY:.4f}")

    return txt_it