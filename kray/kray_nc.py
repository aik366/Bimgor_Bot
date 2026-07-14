def kray_fasad_nc(i, dlina, visota):
    with open('pl/nc.txt', 'r') as g:
        texnc = g.read()
        if len(i[8]) != 0 and i[8][:2] == '10':
            i[5] = '17' if i[5] != '16' else i[5]
            texnc = texnc.replace('frez', '132')
            if int(dlina) < 75 or int(visota) < 75:
                texnc = texnc.replace('glubina', 't-9.0')
            else:
                texnc = texnc.replace('glubina', 't-10.301')
            return texnc
        if i[5] == '11':
            if int(dlina) < 75 or int(visota) < 75:
                texnc = texnc.replace('frez', '155')
                texnc = texnc.replace('glubina', 't-15.2')
            else:
                texnc = texnc.replace('frez', '158')
                texnc = texnc.replace('glubina', 't-16.3')

        elif i[5] == '12':
            if int(dlina) < 75 or int(visota) < 75:
                texnc = texnc.replace('frez', '155')
                texnc = texnc.replace('glubina', 't-15.2')
            else:
                txt12nc = open('pl/15_nc.txt', 'r').read()
                texnc = texnc.replace("/PLAST", txt12nc)
                texnc = texnc.replace('frez', '129')
                texnc = texnc.replace('glubina', 't-16.3')

        # elif i[5] == '13':
        #     txt13ss = open('pl/13_ss.txt', 'r').read()
        #     texnc = texnc.replace("/17", txt13ss)
        #     texnc = texnc.replace('frez', '132')
        #     texnc = texnc.replace('glubina', '-2')

        elif i[5] == '14':
            if int(dlina) < 75 or int(visota) < 75:
                texnc = texnc.replace('frez', '151')
                texnc = texnc.replace('glubina', 't-15.4')
            else:
                texnc = texnc.replace('frez', '151')
                texnc = texnc.replace('glubina', 't-16.3')

        elif i[5] == '15':
            txt15nc = open('pl/15_nc.txt', 'r').read()
            texnc = texnc.replace("/PLAST", txt15nc)
            texnc = texnc.replace('frez', '158')
            texnc = texnc.replace('glubina', 't-14.401')

        elif i[5] in ('16', '17', '18'):
            texnc = texnc.replace('frez', '132')
            texnc = texnc.replace('glubina', 't-16.301')

        elif i[5] == '19':
            if int(dlina) < 75 or int(visota) < 75:
                txt17nc = open('pl/17_nc.txt', 'r').read()
                texnc = texnc.replace("/17", txt17nc)
                texnc = texnc.replace('frez', '132')
                if i[8][:2] == '19':
                    texnc = texnc.replace('glubina', 't-18.2')
                elif i[8][:2] == '22':
                    texnc = texnc.replace('glubina', 't-21.2')
                else:
                    texnc = texnc.replace('glubina', 't-15.2')
            else:
                txt12nc = open('pl/15_nc.txt', 'r').read()
                texnc = texnc.replace("/PLAST", txt12nc)
                texnc = texnc.replace('frez', '128')
                texnc = texnc.replace('glubina', 't-15.5')

        elif i[5] == '20':
            txt20nc = open('pl/20_nc.txt', 'r').read()
            texnc = texnc.replace("/17", txt20nc)
            texnc = texnc.replace('frez', '132')

            if int(dlina) < 75 or int(visota) < 75:
                texnc = texnc.replace('glubina', 't-15.2')
            else:
                texnc = texnc.replace('glubina', 't-16.301')

        return texnc
