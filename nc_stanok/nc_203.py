def nc_203(k, dlina, visota, RAM, radius):

    mnogo = open('rs/203/mnogo.txt', 'r').read()
    txt_ss = open('rs/203/f.txt', 'r').read()

    number, zaz = 5 if RAM[0] == 44.5 else int(RAM[0]), 20 if RAM[1] == 22.5 else int(RAM[1])
    dl = int(dlina)*number+zaz*(number-1)
    if dlina < visota:
        txt_ss = txt_ss.replace('WWW', f"{visota}").replace('LLL', f"{dl}").replace('RRR', radius)
    else:
        txt_ss = txt_ss.replace('LLL', f"{dl}").replace('WWW', f"{visota}").replace('RRR', radius)

    for i in range(number):
        txt_ss = txt_ss.replace('\\NUM', mnogo)
        txt_ss = txt_ss.replace('RX', dlina)
        txt_ss = txt_ss.replace('RY', visota)
        txt_ss = txt_ss.replace('zaz', f"{zaz}")
        txt_ss = txt_ss.replace('konec', f'{9*number+1}')

    return txt_ss
