from ss_stanok import ss_28

def ss_29(k, dlina, visota, RAM):
    if k[7] in ('ПСЯ', 'Бутыл.'):
        return ss_28(k, dlina, visota, RAM)

    txt_ss = ''
    if k[7] == 'Фасад':
        txt_ss = open('rs/29/f.txt', 'r').read()
        RAMX = 130 if int(visota) < 315 else 140
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'Хлеб':
        txt_ss = open('rs/29/xl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '140')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'СТЕКЛО':
        txt_ss = open('rs/29/st.txt', 'r').read()
        RAMX = 130 if int(visota) < 315 else 140
        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')

    elif k[7] == 'Хлеб_ст':
        txt_ss = open('rs/29/xlst.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '140')
        txt_ss = txt_ss.replace('RAMY', '70')
        txt_ss = txt_ss.replace('rRr', '50')


    if k[7] in ('СТЕКЛО', 'Хлеб_ст', 'ПЕРЕПЛЕТ', 'Планка'):
        return txt_ss
    elif k[6] == '22':
        txt_ss = txt_ss.replace("146", "137")
    elif k[6] == '23':
        txt_ss = txt_ss.replace("146", "157")
    elif k[6] == '24':
        txt_ss = txt_ss.replace("t-9", "t-3")
    elif k[6] == '26':
        txt_ss = txt_ss.replace("146", "150")
        txt_ss = txt_ss.replace("t-9", "t-2.5")
    elif k[6] == '28':
        txt_ss = txt_ss.replace("146", "136")
        txt_ss = txt_ss.replace("t-9", "t-2")
    elif k[6] == '29':
        txt_ss = txt_ss.replace("146", "144")
        txt_ss = txt_ss.replace("t-9", "t-1.2")
    elif k[6] == '30':
        txt_ss = txt_ss.replace("146", "159")
        txt_ss = txt_ss.replace("t-9", "t-12.9")

    return txt_ss