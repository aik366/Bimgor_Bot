def pr_ss(i, length, widthh, Txt, eto_stol):
    length = int(length)
    widthh = int(widthh)


    if 170 <= length < 270 and 140 <= widthh < 170:
        b1= open('ps/b1.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b1)
    elif 170 <= length < 550 and 140 <= widthh < 170:
        b2 = open('ps/mb1.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b2)
    elif widthh < 140 and length < 290:
        m1l = open('ps/m1l.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", m1l)
    elif widthh < 140 and length >= 290 and length < 330:
        m2l = open('ps/m2l.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", m2l)

    elif length >= 140 and length < 170 and widthh >= 170 and widthh < 250:
        b1 = open('ps/b1.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", b1)
    elif length >= 140 and length < 170 and widthh >= 250 and widthh < 330:
        mb1 = open('ps/mb1.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", mb1)
    elif length >= 140 and length < 170 and widthh >= 330 and widthh < 550:
        bb1 = open('ps/bb1.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", bb1)

    elif widthh < 170 and length < 330:
        m1 = open('ps/m1.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m1)
    elif widthh < 170 and length >= 330 and length < 550:
        m2 = open('ps/m2.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m2)
    elif widthh < 170 and length >= 550 and length < 1340:
        m3 = open('ps/m3.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m3)
    elif widthh < 170 and length >= 1340 and length <= 1870:
        m4 = open('ps/m4.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m4)
    elif widthh < 170 and length > 1870 and length <= 2400:
        m5 = open('ps/m5.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m5)
    elif widthh < 170 and length >= 2400 and length < 3001:
        m6 = open('ps/m6.txt', 'r').read()
        Txt = Txt.replace("GGGGG", m6)

    elif widthh >= 170 and widthh < 248 and length < 290:
        b1 = open('ps/b1.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b1)
    elif widthh >= 170 and widthh < 248 and length >= 290 and length < 330:
        b2l = open('ps/b2l.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", b2l)
    elif widthh >= 170 and widthh < 248 and length >= 330 and length < 550:
        b2 = open('ps/b2.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b2)
    elif widthh >= 170 and widthh < 248 and length >= 550 and length < 1340:
        b3 = open('ps/b3.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b3)
    elif  widthh >= 170 and widthh < 248 and length >= 1340 and length <= 1870:
        b4 = open('ps/b4.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b4)
    elif widthh >= 170 and widthh < 248 and length > 1870 and length <= 2400:
        b5 = open('ps/b5.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b5)
    elif widthh >= 170 and widthh < 248 and length >= 2400 and length < 3001:
        b6 = open('ps/b6.txt', 'r').read()
        Txt = Txt.replace("GGGGG", b6)

    elif widthh >= 248 and length < 290:
        mb1 = open('ps/mb1.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb1)
    elif widthh >= 248  and length >= 290 and length < 330:
        mb2l = open('ps/mb2l.txt', 'r').read()
        Txt = Txt.replace('FNX="1"', 'FNX="43"')
        Txt = Txt.replace("GGGGG", mb2l)
    elif widthh >= 248  and length >= 330 and length < 550:
        mb2 = open('ps/mb2.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb2)
    elif widthh >= 248  and length >= 550 and length < 1340:
        mb3 = open('ps/mb3.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb3)
    elif widthh >= 248  and length >= 1340 and length <= 1870:
        mb4 = open('ps/mb4.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb4)
    elif widthh >= 248  and length > 1870 and length <= 2400:
        mb5 = open('ps/mb5.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb5)
    elif widthh >= 248  and length >= 2400 and length < 3001:
        mb6 = open('ps/mb6.txt', 'r').read()
        Txt = Txt.replace("GGGGG", mb6)


    if eto_stol == 1:
        if i[4][0] == '4' and int(i[4][6:]) > 12:
            Txt = Txt.replace('XA="100', 'XA="' + str(int(i[4][6:]) / 4 + 70))
            Txt = Txt.replace('XA="l-70', 'XA="l-70-' + str(int(i[4][6:]) / 4))
            Txt = Txt.replace('YA1="85', 'YA1="' + str(int(i[4][6:]) / 2 + 85), 1)
            Txt = Txt.replace('YA1="86', 'YA1="' + str(int(i[4][6:]) / 2 + 85), 1)
            Txt = Txt.replace('YA2="w-45', 'YA2="w-45-' + str(int(i[4][6:]) / 2), 1)
            Txt = Txt.replace('YA2="w-46', 'YA2="w-46-' + str(int(i[4][6:]) / 2), 1)

        elif i[4][:2] == "2Д" and int(i[4][6:]) > 12:
            Txt = Txt.replace('XA="l-70', 'XA="l-70-' + str(int(i[4][6:]) / 4))
            Txt = Txt.replace('YA1="86', 'YA1="' + str(int(i[4][6:]) / 2 + 85), 1)
            Txt = Txt.replace('YA2="w-46', 'YA2="w-46-' + str(int(i[4][6:]) / 2), 1)

        elif i[4][:2] == "1Д" and int(i[4][6:]) > 12:
            Txt = Txt.replace('XA="100', 'XA="' + str(int(i[4][6:]) / 4 + 70))
            Txt = Txt.replace('XA="l-70', 'XA="l-70-' + str(int(i[4][6:]) / 4))
            Txt = Txt.replace('YA2="w-45', 'YA2="w-45-' + str(int(i[4][6:]) / 2), 1)
            Txt = Txt.replace('YA2="w-46', 'YA2="w-46-' + str(int(i[4][6:]) / 2), 1)

        elif i[4][0] in ('л', 'п'):
            Txt = Txt.replace('XA="l-70', 'XA="l-70-' + str(int(i[4][2:]) / 4))
            Txt = Txt.replace('YA2="w-46', 'YA2="w-46-' + str(int(i[4][2:]) / 2), 1)


    return Txt