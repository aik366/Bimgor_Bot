def stol_nc(i, ll, ww, rad, st_v):
    txt_stol = open('pl/16_stol_nc.txt', 'r').read()

    txt_stol = txt_stol.replace('LLL', ll)
    txt_stol = txt_stol.replace('WWW', ww)

    if i[8][:2] == '22':
        txt_stol = txt_stol.replace('t=16.20', 't=22.40')
    elif i[8][:2] == '32':
        txt_stol = txt_stol.replace('t=16.20', 't=32.50')
        txt_stol = txt_stol.replace('ZSTART="0"', 'ZSTART="15"')
        txt_stol = txt_stol.replace('ANZZST="0"', 'ANZZST="2"')
        txt_stol = txt_stol.replace('STUFEN="0"', 'STUFEN="1"')

    txt_st = ''

    if i[4][2] in ("д", 'к'):
        if i[4] == "1 дл ":
            txt_st = open('rs/stol/1d.txt', 'r').read()
        elif i[4] == "2 дл ":
            txt_st = open('rs/stol/2d.txt', 'r').read()
        elif i[4] == "1 кор":
            txt_st = open('rs/stol/1k.txt', 'r').read()
        elif i[4] == "2 кор":
            txt_st = open('rs/stol/2k.txt', 'r').read()

        if i[5] == '18':
            txt_st = txt_st.replace("SEI", "SEN").replace("WRKR", "NoWRK")
            txt_st = txt_st.replace("Y=0.0", "Y=1").replace("X=0.0", "X=1") \
                .replace("Y=w", "Y=w-1").replace("X=l", "X=l-1")

        txt_stol = txt_stol.replace("\MMMMM", txt_st)

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
            txt_st = open('rs/stol/4st_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol/4st_nc.txt', 'r').read()

        txt_stol = txt_stol.replace("\MMMMM", txt_st)

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
            txt_st = open('rs/stol/1d2k_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol/1d2k.txt', 'r').read()

        txt_stol = txt_stol.replace("\MMMMM", txt_st)

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
            txt_st = open('rs/stol/2d1k_18.txt', 'r').read()
        else:
            txt_st = open('rs/stol/2d1k.txt', 'r').read()

        txt_stol = txt_stol.replace("\MMMMM", txt_st)

        if int(i[4][6:]) >= int(ww) / 2:
            radius_4st = str(int(ww) / 2 - 0.001)
        else:
            radius_4st = i[4][6:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace("R4R", rad)
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", '8')
            txt_stol = txt_stol.replace("R4R", '8')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", '12')
            txt_stol = txt_stol.replace("R4R", '12')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)
        else:
            txt_stol = txt_stol.replace("R1R", '5')
            txt_stol = txt_stol.replace("R4R", '5')
            txt_stol = txt_stol.replace("R3R", radius_4st)
            txt_stol = txt_stol.replace("R2R", radius_4st)

    elif i[4][0] == "л" or i[4][0] == "п":
        rr3, rr4 = "R3R", "R4R"
        if i[4][0] == "п":
            rr3, rr4 = "R4R", "R3R"
        if i[5] == '18' and i[4][0] == "п":
            txt_st = open('rs/stol/1d1k_R_18.txt', 'r').read()
        elif i[5] == '18' and i[4][0] == "л":
            txt_st = open('rs/stol/1d1k_L_18.txt', 'r').read()
        elif i[4][0] == "п":
            txt_st = open('rs/stol/1d1k_R.txt', 'r').read()
        else:
            txt_st = open('rs/stol/1d1k_L.txt', 'r').read()

        txt_stol = txt_stol.replace("\MMMMM", txt_st)


        if int(i[4][2:]) >= (int(ww) - int(rad)):
            if i[8][:2] == '22': rad = '8'
            if i[8][:2] == '32': rad = '12'
            if i[4][0] == "п":
                txt_stol = txt_stol.replace("Y=w-R3R", "Y=@0.001")
            else:
                txt_stol = txt_stol.replace("Y=w-R4R", f"Y=w-R4R+{int(rad) + 0.001}")
        if int(i[4][2:]) >= (int(ll) - int(rad)):
            if i[8][:2] == '22': rad = '8'
            if i[8][:2] == '32': rad = '12'
            if i[4][0] == "п":
                txt_stol = txt_stol.replace("X=l-R3R", f"X={int(rad) + 0.001}")
            else:
                txt_stol = txt_stol.replace("X=l-R4R", f"X=l-R4R+{int(rad) + 0.001}")

        radius_4st = i[4][2:]

        if st_v == 1:
            txt_stol = txt_stol.replace("R1R", rad)
            txt_stol = txt_stol.replace(f"{rr3}", rad)
            txt_stol = txt_stol.replace("R2R", rad)
            txt_stol = txt_stol.replace(f"{rr4}", radius_4st)
        elif i[8][:2] == '22':
            txt_stol = txt_stol.replace("R1R", '8')
            txt_stol = txt_stol.replace(f"{rr3}", '8')
            txt_stol = txt_stol.replace("R2R", '8')
            txt_stol = txt_stol.replace(f"{rr4}", radius_4st)
        elif i[8][:2] == '32':
            txt_stol = txt_stol.replace("R1R", '12')
            txt_stol = txt_stol.replace(f"{rr3}", '12')
            txt_stol = txt_stol.replace("R2R", '12')
            txt_stol = txt_stol.replace(f"{rr4}", radius_4st)
        else:
            txt_stol = txt_stol.replace("R1R", '5')
            txt_stol = txt_stol.replace(f"{rr3}", '5')
            txt_stol = txt_stol.replace("R2R", '5')
            txt_stol = txt_stol.replace(f"{rr4}", radius_4st)


    if i[5] == "14":
        txt_stol = txt_stol.replace("AB_0", "0")
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("frez", "151")
            txt_stol = txt_stol.replace("Hfrz", "t-15.4")
        else:
            txt_stol = txt_stol.replace("frez", "151")
            txt_stol = txt_stol.replace("Hfrz", "t-16.3")

    elif i[5] == "15":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "158")
        txt_stol = txt_stol.replace("Hfrz", "t-15.001")

    elif i[5] == "12":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "129")
        txt_stol = txt_stol.replace("Hfrz", "t-16.3")

    elif i[5] == "11":
        txt_stol = txt_stol.replace("AB_0", "0")
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("frez", "155")
            txt_stol = txt_stol.replace("Hfrz", "t-15.2")
        else:
            txt_stol = txt_stol.replace("frez", "158")
            txt_stol = txt_stol.replace("Hfrz", "t-16.3")


    elif i[5] == "13" and i[8][2] == "м":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "143")
        txt_stol = txt_stol.replace("Hfrz", "t-23")

    elif i[5] == "13":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "135")
        txt_stol = txt_stol.replace("Hfrz", "t-15.7")

    elif i[5] == "16":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "136")
        txt_stol = txt_stol.replace("Hfrz", "t-16.301")
        txt_stol = txt_stol.replace('TNO="136"', 'TNO="132"\nEN="0"')

    elif i[5] == "17":
        txt_stol = txt_stol.replace("AB_0", "1.5")
        txt_stol = txt_stol.replace("frez", "144")
        txt_stol = txt_stol.replace("Hfrz", "t-3.5")

    elif i[5] == "18":
        txt_stol = txt_stol.replace("AB_0", "0")
        txt_stol = txt_stol.replace("frez", "150")
        txt_stol = txt_stol.replace("Hfrz", "t-3.5")

    elif i[5] == "19":
        if int(ll) < 75 or int(ww) < 75:
            txt_stol = txt_stol.replace("AB_0", "1.5")
            txt_stol = txt_stol.replace('frez', '144')
            txt_stol = txt_stol.replace('Hfrz', 't-3.5')
        else:
            txt_stol = txt_stol.replace("AB_0", "0")
            txt_stol = txt_stol.replace("frez", "128")
            txt_stol = txt_stol.replace("Hfrz", "t-15.5")

    elif i[5] == "20":
        txt_stol = txt_stol.replace("AB_0", "2")
        txt_stol = txt_stol.replace("frez", "163")
        txt_stol = txt_stol.replace("Hfrz", "t-6.9")


    return txt_stol
