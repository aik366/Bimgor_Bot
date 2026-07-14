def kray_fasad_ss(i, dlina, visota):
    with open('pl/ss.txt', 'r') as g:
        texss = g.read()
        if i[5] == '11':
            if int(dlina) < 75 or int(visota) < 75:
                texss = texss.replace('frez', '155')
                texss = texss.replace('glubina', 't-15.2')
            else:
                texss = texss.replace('frez', '158')
                texss = texss.replace('glubina', 't-16.3')

        elif i[5] == '12':
            if int(dlina) < 75 or int(visota) < 75:
                texss = texss.replace('frez', '155')
                texss = texss.replace('glubina', 't-15.2')
            else:
                texss = texss.replace('frez', '146')
                texss = texss.replace('glubina', 't-34.2')

        elif i[5] == '13':
            if int(dlina) < 75 or int(visota) < 75:
                texss = texss.replace('frez', '151')
                texss = texss.replace('glubina', 't-15.4')
            else:
                txt132ss = open('pl/132_ss.txt', 'r').read()
                texss = texss.replace("/132", txt132ss)
                texss = texss.replace('frez', '135')
                texss = texss.replace('glubina', 't-15.7')

        elif i[5] == '14':
            if int(dlina) < 75 or int(visota) < 75:
                texss = texss.replace('frez', '151')
                texss = texss.replace('glubina', 't-15.4')
            else:
                texss = texss.replace('frez', '151')
                texss = texss.replace('glubina', 't-16.7')

        elif i[5] == '15':
            txt132ss = open('pl/132_ss.txt', 'r').read()
            if int(dlina) < 75 or int(visota) < 75:
                txt132ss = txt132ss.replace('-2', '0.8')
                texss = texss.replace("/132", txt132ss)
                texss = texss.replace('frez', '155')
                texss = texss.replace('glubina', 't-13')
            else:
                texss = texss.replace("/132", txt132ss)
                texss = texss.replace('frez', '158')
                texss = texss.replace('glubina', 't-14.4')

        elif i[5] in ('16', '17', '18'):
            texss = texss.replace('frez', '132')
            texss = texss.replace('glubina', '-2')

        elif i[5] == '19':
            if int(dlina) < 75 or int(visota) < 75:
                txt17ss = open('pl/17_ss.txt', 'r').read()
                texss = texss.replace("/17", txt17ss)
                texss = texss.replace('frez', '132')
                texss = texss.replace('glubina', '0.8')
            elif len(i[8]) != 0 and i[8][:2] == '10':
                txt17ss = open('pl/17_ss.txt', 'r').read()
                texss = texss.replace("/17", txt17ss)
                texss = texss.replace('frez', '132')
                texss = texss.replace('glubina', '-2')
            else:
                txt132ss = open('pl/132_ss.txt', 'r').read()
                texss = texss.replace("/132", txt132ss)
                texss = texss.replace('frez', '128')
                texss = texss.replace('glubina', 't-15.6')

        elif i[5] == '20':
            txt20ss = open('pl/20_ss.txt', 'r').read()
            texss = texss.replace("/17", txt20ss)
            texss = texss.replace('frez', '132')

            if int(dlina) < 75 or int(visota) < 75:
                texss = texss.replace('glubina', '0.8')
            else:
                texss = texss.replace('glubina', '-2')

        return texss
