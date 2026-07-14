from ss_stanok import ss_96

oBv111ss = [27, 32, 61.5, 13.6, 22.21, 12.2001, 20.7501, 28, 10.6, 19]


def ss_111(k, dlina, visota, RAM):
    if k[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2', 'ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl', 'ПЕРЕПЛЕТ8'):
        return ss_96(k, dlina, visota, RAM)

    txt_ss = ''
    oBv = oBv111ss.copy()

    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/111/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] == 'Фасад2':
        txt_ss = open('rs/111/f2.txt', 'r').read()
        RAMX, RAMY, RAMK = RAM[0], RAM[0], RAM[2]
        RAMZ = int(dlina) - RAMK + (RAMX + 16)
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('RAMK', str(RAMK))
        txt_ss = txt_ss.replace('RAMZ', str(RAMZ))
        txt_ss = txt_ss.replace("WEEKE BHC T.", "На Италянском тоже есть")
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        oBv[1] = oBv[7]
        txt_ss = open('rs/111/st.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[0]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 146:
        txt_ss = open('rs/111/f.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        for i in range(10):
            txt_ss = txt_ss.replace('oBv' + str(i), str(oBv[i]))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 146:
        txt_ss = open('rs/91/pssl.txt', 'r').read()
        RAMX, RAMY = RAM[0], RAM[1]
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

    if RAM[4] == 1:
        RAMX, RAMY = RAM[0], RAM[0]
        if k[7] == 'Бутыл.':
            pod_92 = open('pl/92_f.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - (RAM[0] - RAM[1]) - 3.5 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        elif k[7] in ('Фасад', 'Фасад2', 'СТЕКЛО'):
            pod_92 = open('pl/92_f.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.5 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        elif k[7] in ('Хлеб', 'Хлеб_ст', 'ПСЯ'):
            pod_92 = open('pl/92_xl.txt', 'r').read()
            txt_ss = txt_ss.replace("\\pod45\\", pod_92)
            txt_ss = txt_ss.replace('pod92', f'{oBv[6] - 3.5 + 0.01} ')
            txt_ss = txt_ss.replace('92_STR', str(txt_ss.count(']') + 1))
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))

    return txt_ss