def add_132():
    with open('pl/132_it.txt', 'r') as kr:
        return kr.read()


def kray_fasad_it(i, dlina, visota):
    with open('pl/it.txt', 'r') as g:
        texit = g.read()

        if len(i[8]) != 0 and i[8][:2] == '10':
            i[5] = '17' if i[5] != '16' else i[5]
            texit = texit.replace('frez', '132')
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '-1.5')
            else:
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '1.5')
            return texit

        if i[5] == '11':
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('frez', '155')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.2')
            else:
                # texit = texit.replace("' kr19", '').replace("' kr17", '')
                # texit = texit.replace("' kr132", add_132())
                texit = texit.replace('frez', '158')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '18.9')

        elif i[5] == '12':
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('frez', '155')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.2')
            else:
                texit = texit.replace("' kr19", '').replace("' kr17", '')
                texit = texit.replace("' kr132", add_132())
                texit = texit.replace('frez', '129')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.4')

        elif i[5] == '13':
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('frez', '135')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.2')
            else:
                texit = texit.replace("' kr19", '').replace("' kr17", '')
                texit = texit.replace("' kr132", add_132())
                texit = texit.replace('frez', '135')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.7')

        elif i[5] == '14':
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('frez', '151')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '15.4')
            else:
                texit = texit.replace('frez', '151')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '16.7')

        elif i[5] == '15':
            if int(dlina) < 75 or int(visota) < 75:
                txt15it = open('pl/155_it.txt', 'r').read()
                texit = texit.replace("' kr17", txt15it)
                texit = texit.replace('frez', '132')
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '-1.5')
            else:
                # texit = texit.replace("' kr19", '').replace("' kr17", '')
                # texit = texit.replace("' kr132", add_132())
                texit = texit.replace('frez', '158')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '17.0')

        elif i[5] in ('16', '17', '18'):
            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('frez', '132')
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '-1.5')
            else:
                texit = texit.replace('frez', '132')
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '1.5')

        elif i[5] == '19':
            if int(dlina) < 75 or int(visota) < 75:
                txt17it = open('pl/17_it.txt', 'r').read()
                texit = texit.replace("' kr17", txt17it)
                texit = texit.replace('frez', '132')
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '-1.5')
            elif len(i[8]) != 0 and i[8][:2] == '10':
                txt17it = open('pl/17_it.txt', 'r').read()
                texit = texit.replace("' kr17", txt17it)
                texit = texit.replace('frez', '132')
                texit = texit.replace('skvoz', '1')
                texit = texit.replace('glubina', '1.5')
            else:
                texit = texit.replace('frez', '128')
                texit = texit.replace('skvoz', '0')
                texit = texit.replace('glubina', '19.2')

        elif i[5] == '20':
            txt20it = open('pl/20_it.txt', 'r').read()
            texit = texit.replace("' kr17", txt20it)
            texit = texit.replace('frez', '132')
            texit = texit.replace('skvoz', '1')

            if int(dlina) < 75 or int(visota) < 75:
                texit = texit.replace('glubina', '-1.5')
            else:
                texit = texit.replace('glubina', '1.5')

        return texit
