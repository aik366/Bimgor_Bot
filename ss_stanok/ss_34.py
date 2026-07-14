def ss_34(k, dlina, visota, RAM):
    txt_ss = ''
    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/34/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] in ('СТЕКЛО', 'Хлеб_ст'):
        txt_ss = open('rs/34/st.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '70')

    elif k[7] == 'ПЕРЕПЛЕТ':
        txt_ss = open('rs/34/per.txt', 'r').read()
        rAm, pEr, rR1, rR = 70, 30, '4', '3'
        xX = (int(dlina) - rAm * 2 - pEr * 2) / 3
        yY = (int(visota) - rAm * 2 - pEr) / 2

        txt_ss = txt_ss.replace("rAm", str(rAm))
        txt_ss = txt_ss.replace("pEr", str(pEr))
        txt_ss = txt_ss.replace("gLub", 't-15.3')
        txt_ss = txt_ss.replace("rR1", rR1)
        txt_ss = txt_ss.replace("rR", rR)
        txt_ss = txt_ss.replace("xX", str(round(xX, 3)))
        txt_ss = txt_ss.replace("yY", str(round(yY, 3)))

    elif k[7] in ('ПЕРЕПЛЕТ4', 'ПЕРЕПЛЕТ4_xl'):
        txt_ss = open('rs/34/per4.txt', 'r').read()
        rAm, pEr, rR1, rR = 70, 30, '4', '3'
        xX = (int(dlina) - rAm * 2 - pEr) / 2
        yY = (int(visota) - rAm * 2 - pEr) / 2

        txt_ss = txt_ss.replace("rAm", str(rAm))
        txt_ss = txt_ss.replace("pEr", str(pEr))
        txt_ss = txt_ss.replace("gLub", 't-15.3')
        txt_ss = txt_ss.replace("rR1", rR1)
        txt_ss = txt_ss.replace("rR", rR)
        txt_ss = txt_ss.replace("xX", str(round(xX, 3)))
        txt_ss = txt_ss.replace("yY", str(round(yY, 3)))

    elif k[7] == 'ПЕРЕПЛЕТ8':
        txt_ss = open('rs/34/per8.txt', 'r').read()
        rAm, pEr, rR1, rR = 70, 30, '4', '3'
        xX = (int(dlina) - rAm * 2 - pEr * 3) / 4
        yY = (int(visota) - rAm * 2 - pEr) / 2

        txt_ss = txt_ss.replace("rAm", str(rAm))
        txt_ss = txt_ss.replace("pEr", str(pEr))
        txt_ss = txt_ss.replace("gLub", 't-15.3')
        txt_ss = txt_ss.replace("rR1", rR1)
        txt_ss = txt_ss.replace("rR", rR)
        txt_ss = txt_ss.replace("xX", str(round(xX, 3)))
        txt_ss = txt_ss.replace("yY", str(round(yY, 3)))

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) >= 140:
        txt_ss = open('rs/34/f.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] in ('ПСЯ', 'Бутыл.') and int(visota) < 140:
        txt_ss = open('rs/34/pssl.txt', 'r').read()
        txt_ss = txt_ss.replace('RAMX', '70')
        txt_ss = txt_ss.replace('RAMY', '40')

    elif k[7] == 'Планка':
        txt_ss = open('rs/91/pl.txt', 'r').read()

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