def stol_it(i, ll, ww, rad, st_v):
    radius_4st = '5'
    txt_stol = open('pl/16_stol_it.txt', 'r').read()
    if int(ll) < 75 or int(ww) < 75:
        txt_stol = txt_stol.replace('glubina', '-1.5').replace('skvoz', '1')
    else:
        txt_stol = txt_stol.replace('glubina', '1.5').replace('skvoz', '1')

    txt_stol = txt_stol.replace('LLL', ll)
    txt_stol = txt_stol.replace('WWW', ww)

    if i[8][:2] == '22':
        txt_stol = txt_stol.replace('LPZ|16.2', 'LPZ|22.0') if i[5] == '19' else txt_stol.replace('LPZ|16.2', 'LPZ|22.4')
    elif i[8][:2] == '32':
        txt_stol = txt_stol.replace('LPZ|16.2', 'LPZ|32')

    txt_st = ''

    if i[4][2] in ("д", 'к'):
        if i[4] == "1 дл ":
            txt_st = open('rs/stol_it/1d.txt', 'r').read()
        elif i[4] == "2 дл ":
            txt_st = open('rs/stol_it/2d.txt', 'r').read()
        elif i[4] == "1 кор":
            txt_st = open('rs/stol_it/1k.txt', 'r').read()
        elif i[4] == "2 кор":
            txt_st = open('rs/stol_it/2k.txt', 'r').read()

        txt_stol = txt_stol.replace("' kr17", txt_st)

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace("R3R", rad)
            txt_stol = txt_stol.replace("R4R", rad)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", "8")
            txt_stol = txt_stol.replace("R2R", "8")
            txt_stol = txt_stol.replace("R3R", "8")
            txt_stol = txt_stol.replace("R4R", "8")
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", "12")
            txt_stol = txt_stol.replace("R2R", "12")
            txt_stol = txt_stol.replace("R3R", "12")
            txt_stol = txt_stol.replace("R4R", "12")
        else:
            txt_stol = txt_stol.replace("R1R", "5")
            txt_stol = txt_stol.replace("R2R", "5")
            txt_stol = txt_stol.replace("R3R", "5")
            txt_stol = txt_stol.replace("R4R", "5")

    elif i[4][0] == '4':
        if i[5] == '18':
            txt_st = open('rs/stol_it/4st_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol_it/4st.txt', 'r').read()

        txt_stol = txt_stol.replace("' kr17", txt_st)

        if int(i[4][6:]) >= int(ww) / 2:
            radius_4st = str(int(i[4][6:]) - 0.001)
        else:
            radius_4st = i[4][6:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace("R3R", rad)
            txt_stol = txt_stol.replace("R4R", rad)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)
        else:
            txt_stol = txt_stol.replace("R1R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)

    elif i[4][:2] == "1Д":
        if i[5] == '18':
            txt_st = open('rs/stol_it/1d2k_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol_it/1d2k.txt', 'r').read()

        txt_stol = txt_stol.replace("' kr17", txt_st)

        if int(i[4][6:]) >= int(ll) / 2:
            radius_4st = str(int(ll) / 2 - 0.001)
        else:
            radius_4st = i[4][6:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", '8')
            txt_stol = txt_stol.replace("R2R", '8')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", '12')
            txt_stol = txt_stol.replace("R2R", '12')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)
        else:
            txt_stol = txt_stol.replace("R1R", '5')
            txt_stol = txt_stol.replace("R2R", '5')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R4R", radius_4st)

    elif i[4][:2] == "2Д":
        if i[5] == '18':
            txt_st = open('rs/stol_it/2d1k_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol_it/2d1k.txt', 'r').read()

        txt_stol = txt_stol.replace("' kr17", txt_st)

        if int(i[4][6:]) >= int(ww) / 2:
            radius_4st = str(int(ww) / 2 - 0.001)
        else:
            radius_4st = i[4][6:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R3R", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace("R4R", radius_4st)
            txt_stol = txt_stol.replace("R1R", radius_4st)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R3R", '8')
            txt_stol = txt_stol.replace("R2R", '8')
            txt_stol = txt_stol.replace("R4R", radius_4st)
            txt_stol = txt_stol.replace("R1R", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R3R", '12')
            txt_stol = txt_stol.replace("R2R", '12')
            txt_stol = txt_stol.replace("R4R", radius_4st)
            txt_stol = txt_stol.replace("R1R", radius_4st)
        else:
            txt_stol = txt_stol.replace("R3R", '5')
            txt_stol = txt_stol.replace("R2R", '5')
            txt_stol = txt_stol.replace("R4R", radius_4st)
            txt_stol = txt_stol.replace("R1R", radius_4st)

    elif i[4][0] == "л" or i[4][0] == "п":
        rr3, rr4 = "R3R", "R4R"
        if i[4][0] == "п":
            rr3, rr4 = "R4R", "R3R"
        if i[5] == '18' and i[4][0] == "п":
            txt_st = open('rs/stol_it/1d1k_R_18.txt', 'r').read()
        elif i[5] == '18' and i[4][0] == "л":
            txt_st = open('rs/stol_it/1d1k_L_18.txt', 'r').read()
        elif i[4][0] == "п":
            txt_st = open('rs/stol_it/1d1k_R.txt', 'r').read()
        else:
            txt_st = open('rs/stol_it/1d1k_L.txt', 'r').read()

        txt_stol = txt_stol.replace("' kr17", txt_st)

        if i[8][:2] == '22': rad = '8'
        if i[8][:2] == '32': rad = '12'

        radius_4st = i[4][2:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace(f"{rr4}", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace(f"{rr3}", radius_4st)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", '8')
            txt_stol = txt_stol.replace(f"{rr4}", '8')
            txt_stol = txt_stol.replace("R2R", '8')
            txt_stol = txt_stol.replace(f"{rr3}", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", '12')
            txt_stol = txt_stol.replace(f"{rr4}", '12')
            txt_stol = txt_stol.replace("R2R", '12')
            txt_stol = txt_stol.replace(f"{rr3}", radius_4st)
        else:
            txt_stol = txt_stol.replace("R1R", '5')
            txt_stol = txt_stol.replace(f"{rr4}", '5')
            txt_stol = txt_stol.replace("R2R", '5')
            txt_stol = txt_stol.replace(f"{rr3}", radius_4st)

    if i[5] == "14":
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("frez", "151").replace('glubina', '14.4').replace('skvoz', '0')
        else:
            txt_stol = txt_stol.replace("frez", "151").replace('glubina', '16.7').replace('skvoz', '0')

    elif i[5] == "15":
       txt_stol = txt_stol.replace("frez", "155").replace('glubina', '13').replace('skvoz', '0')

    elif i[5] == "12":
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("frez", "155").replace('glubina', '15.2').replace('skvoz', '0')
        else:
            txt_stol = txt_stol.replace("frez", "129").replace('glubina', '15.4').replace('skvoz', '0')

    elif i[5] == "11":
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("frez", "155").replace('glubina', '15.2').replace('skvoz', '0')
        else:
            txt_stol = txt_stol.replace("frez", "158").replace('glubina', '18.9').replace('skvoz', '0')

    elif i[5] == "16":
        txt_stol = txt_stol.replace('@ ROUT, 0 : "frez"', '\' ROUT, 0 : "frez"')

    elif i[5] == "17":
        txt_stol = txt_stol.replace("skvoz, 0, 0, 0, 0, 1, 0, 0,", "0, 0, 0, 0, 0, 1, 0, 1.5,")
        txt_stol = txt_stol.replace("frez", "144").replace('glubina', '3.5')
        txt_stol = txt_stol.replace('"144", 103, 1, 1, 1, 90, 1, 0, 0, 0, 0, 1', '"144", 103, 1, 0, 0, 90, 1, 0, 0, 0, 0, 0')

    elif i[5] == "18":
        txt_stol = txt_stol.replace("frez", "150").replace('glubina', '3.2').replace('skvoz', '0')

    elif i[5] == "19":
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("skvoz, 0, 0, 0, 0, 1, 0, 0,", "0, 0, 0, 0, 0, 1, 0, 1.5,")
            txt_stol = txt_stol.replace("frez", "144").replace('glubina', '3.5')
        else:
            txt_stol = txt_stol.replace("frez", "128").replace('glubina', '19.2').replace('skvoz', '0')

    elif i[5] == "20":
        txt_stol = txt_stol.replace("skvoz, 0, 0, 0, 0, 1, 0, 0,", "0, 0, 0, 0, 0, 1, 0, 2,")
        txt_stol = txt_stol.replace("frez", "163").replace('glubina', '6.9')
        txt_stol = txt_stol.replace('"163", 103, 1, 1, 1, 90, 1, 0, 0, 0, 0, 1', '"163", 103, 1, 0, 0, 90, 1, 0, 0, 0, 0, 0')

    return txt_stol
