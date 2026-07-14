from  math import tan, atan, radians, degrees

def it_202(k, dlina, visota, RAM):
    txt_ss = ''
    oBv = [27-6, 33-6, 61.5, 23.301-6, 21.401-6, 14.101-6, 12.201-6, 12, 27.5-6, 6, 10.4, 1.4]


    if k[7] in ('Фасад', 'Хлеб'):
        txt_ss = open('rs/202_it/f.txt', 'r').read()
        RAMX, RAMY = RAM[0]+6, RAM[0]+6

        zaz, vrad = 26, 8
        tangx = (int(dlina) / 2 - RAMX) / (int(visota) / 2 - RAMX)
        tangy = (int(visota) / 2 - RAMX) / (int(dlina) / 2 - RAMX)

        z0 = RAMX + round(oBv[0] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h0 = RAMX + oBv[0] + round((int(dlina) / 2 - z0) * (tan(radians(degrees(atan(tangy))))), 4)
        z1 = RAMX + round(oBv[1] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h1 = RAMX + oBv[1] + round((int(dlina) / 2 - z1) * (tan(radians(degrees(atan(tangy))))), 4)
        z3 = RAMX + round(oBv[3] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h3 = RAMX + oBv[3] + round((int(dlina) / 2 - z3) * (tan(radians(degrees(atan(tangy))))), 4)
        z5 = RAMX + round(oBv[5] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h5 = RAMX + oBv[5] + round((int(dlina) / 2 - z5) * (tan(radians(degrees(atan(tangy))))), 4)
        z4 = RAMX + round(oBv[4] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h4 = RAMX + oBv[4] + round((int(dlina) / 2 - z4) * (tan(radians(degrees(atan(tangy))))), 4)
        z6 = RAMX + round(oBv[6] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h6 = RAMX + oBv[6] + round((int(dlina) / 2 - z6) * (tan(radians(degrees(atan(tangy))))), 4)
        z8 = RAMX + round(oBv[8] / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h8 = RAMX + oBv[8] + round((int(dlina) / 2 - z8) * (tan(radians(degrees(atan(tangy))))), 4)
        z4_xl = RAMX + round((oBv[4]-7) / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h4_xl = RAMX + oBv[4] - 7 + round((int(dlina) / 2 - z4_xl) * (tan(radians(degrees(atan(tangy))))), 4)
        z6_xl = RAMX + round((oBv[6] - 7) / (tan(radians(degrees(atan(tangy)) / 2))), 4)
        h6_xl = RAMX + oBv[6] - 7 + round((int(dlina) / 2 - z6_xl) * (tan(radians(degrees(atan(tangy))))), 4)

        f0 = RAMX + round(oBv[0] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g0 = RAMX + oBv[0] + round((int(visota) / 2 - f0) * (tan(radians(degrees(atan(tangx))))), 4)
        f1 = RAMX + round(oBv[1] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g1 = RAMX + oBv[1] + round((int(visota) / 2 - f1) * (tan(radians(degrees(atan(tangx))))), 4)
        f3 = RAMX + round(oBv[3] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g3 = RAMX + oBv[3] + round((int(visota) / 2 - f3) * (tan(radians(degrees(atan(tangx))))), 4)
        f5 = RAMX + round(oBv[5] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g5 = RAMX + oBv[5] + round((int(visota) / 2 - f5) * (tan(radians(degrees(atan(tangx))))), 4)
        f4 = RAMX + round(oBv[4] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g4 = RAMX + oBv[4] + round((int(visota) / 2 - f4) * (tan(radians(degrees(atan(tangx))))), 4)
        f6 = RAMX + round(oBv[6] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g6 = RAMX + oBv[6] + round((int(visota) / 2 - f6) * (tan(radians(degrees(atan(tangx))))), 4)
        f8 = RAMX + round(oBv[8] / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g8 = RAMX + oBv[8] + round((int(visota) / 2 - f8) * (tan(radians(degrees(atan(tangx))))), 4)
        f4_xl = RAMX + round((oBv[4] - 7) / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g4_xl = RAMX + oBv[4] - 7 + round((int(visota) / 2 - f4_xl) * (tan(radians(degrees(atan(tangx))))), 4)
        f6_xl = RAMX + round((oBv[6] - 7) / (tan(radians(degrees(atan(tangx)) / 2))), 4)
        g6_xl = RAMX + oBv[6] - 7 + round((int(visota) / 2 - f6_xl) * (tan(radians(degrees(atan(tangx))))), 4)

        txt_ss = txt_ss.replace('RAMX', str(RAMX))
        txt_ss = txt_ss.replace('RAMY', str(RAMY))
        txt_ss = txt_ss.replace('zaz', str(zaz))
        txt_ss = txt_ss.replace('VRAD', str(vrad))
        txt_ss = txt_ss.replace("z4_xl", f'{z4_xl:.3f}')
        txt_ss = txt_ss.replace("h4_xl", f'{h4_xl:.3f}')
        txt_ss = txt_ss.replace("z6_xl", f'{z6_xl:.3f}')
        txt_ss = txt_ss.replace("h6_xl", f'{h6_xl:.3f}')
        txt_ss = txt_ss.replace("z0", f'{z0:.3f}')
        txt_ss = txt_ss.replace("h0", f'{h0:.3f}')
        txt_ss = txt_ss.replace("z1", f'{z1:.3f}')
        txt_ss = txt_ss.replace("h1", f'{h1:.3f}')
        txt_ss = txt_ss.replace("z3", f'{z3:.3f}')
        txt_ss = txt_ss.replace("h3", f'{h3:.3f}')
        txt_ss = txt_ss.replace("z5", f'{z5:.3f}')
        txt_ss = txt_ss.replace("h5", f'{h5:.3f}')
        txt_ss = txt_ss.replace("z4", f'{z4:.3f}')
        txt_ss = txt_ss.replace("h4", f'{h4:.3f}')
        txt_ss = txt_ss.replace("z6", f'{z6:.3f}')
        txt_ss = txt_ss.replace("h6", f'{h6:.3f}')
        txt_ss = txt_ss.replace("z8", f'{z8:.3f}')
        txt_ss = txt_ss.replace("h8", f'{h8:.3f}')

        txt_ss = txt_ss.replace("f4_xl", f'{f4_xl:.3f}')
        txt_ss = txt_ss.replace("g4_xl", f'{g4_xl:.3f}')
        txt_ss = txt_ss.replace("f6_xl", f'{f6_xl:.3f}')
        txt_ss = txt_ss.replace("g6_xl", f'{g6_xl:.3f}')
        txt_ss = txt_ss.replace("f0", f'{f0:.3f}')
        txt_ss = txt_ss.replace("g0", f'{g0:.3f}')
        txt_ss = txt_ss.replace("f1", f'{f1:.3f}')
        txt_ss = txt_ss.replace("g1", f'{g1:.3f}')
        txt_ss = txt_ss.replace("f3", f'{f3:.3f}')
        txt_ss = txt_ss.replace("g3", f'{g3:.3f}')
        txt_ss = txt_ss.replace("f5", f'{f5:.3f}')
        txt_ss = txt_ss.replace("g5", f'{g5:.3f}')
        txt_ss = txt_ss.replace("f4", f'{f4:.3f}')
        txt_ss = txt_ss.replace("g4", f'{g4:.3f}')
        txt_ss = txt_ss.replace("f6", f'{f6:.3f}')
        txt_ss = txt_ss.replace("g6", f'{g6:.3f}')
        txt_ss = txt_ss.replace("f8", f'{f8:.3f}')
        txt_ss = txt_ss.replace("g8", f'{g8:.3f}')


        for i in range(10):
            txt_ss = txt_ss.replace('OBV' + str(i), str(oBv[i]))

    elif k[7] == 'Планка':
        txt_ss = open('rs/91_it/pl.txt', 'r').read()

    return txt_ss
