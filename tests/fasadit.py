import fas
from it_stanok import *
from ss_stanok import *
from nc_stanok import *
from kray.kray_it import kray_fasad_it
from kray.kray_ss import kray_fasad_ss
from kray.kray_nc import kray_fasad_nc
from ps.prisoski import pr_ss
import os


def fasad_italiya(zak, radius, fr_157=0, fr_1441=0, fr_1442=0, fr_1443=0, fr_pod_45=0,
                  fr_1361=0, fr_1362=0, fr_1363=0, bez_xdf=0, ram_y=0, fr_pod_92=0):
    stol_v, eto_stol = 0, 0

    for num in fas.fasad(zak):

        ram = [44.5, 22.5, 700.0, fr_pod_45, fr_pod_92]

        if bez_xdf == 1:  # без ХДФ
            num[9] = 'БПл'

        if ram_y == 1:  # ПСЯ как фасад
            ram[1] = 44.5
        
# --------------split

        l_th, w_th = num[1], num[2]
        if num[0] == 'R' or num[5] == '.' or num[4] == 'РИСУНОК':
            continue
        if (int(num[2]) > int(num[1])) and num[7] == 'Фасад':
            num[7] = 'Хлеб'
        elif (int(num[2]) > int(num[1])) and num[7] == 'СТЕКЛО':
            num[7] = 'Хлеб_ст'
        elif (int(num[2]) > int(num[1])) and num[7] == 'ПЕРЕПЛЕТ':
            num[7] = 'ПЕРЕПЛЕТ2'

        if num[7] == '' and int(num[1]) >= int(num[2]):
            num[7] = 'Фасад'
        elif num[7] == '' and int(num[1]) < int(num[2]):
            num[7] = 'Хлеб'

        if int(num[2]) > int(num[1]):
            num[1], num[2] = num[2], num[1]

        dlina, visota = num[1], num[2]  # длина, ширина

        txtit = kray_fasad_it(num, dlina, visota)  # край (11, 12, 13, 14, 15, 16, 17, 18)
        txtss = kray_fasad_ss(num, dlina, visota)
        txtnc = kray_fasad_nc(num, dlina, visota)

        if int(dlina) <= 200 or int(visota) <= 200:
            freza_it = {'11': '158', '14': '151', '19': '128'}
            if num[5] in freza_it.keys():
                txt15nc = open('pl/15_nc.txt', 'r').read()
                txtnc = txtnc.replace("/PLAST", txt15nc)
                txtnc = txtnc.replace('TNO="132"', f'TNO="{freza_it[num[5]]}"')
                if num[5] == '19':
                    txtnc = txtnc.replace('t-16.301', 't-14.5')
            txtnc = txtnc.replace('t-16.301', 't-15.3')



        if num[4][0] == 'R':
            w_th, num[2], visota, num[4] = '491', '491', '491', num[4][1:]
            txtit = txtit.replace('LPZ|16.2', 'LPZ|16.7').replace('WWW', num[2])

        rad_us = ['R1', 'R2', 'R3', 'R4', 'Р1', 'Р2', 'Р3', 'Р4']
        if num[8] != '':
            for x in rad_us:
                if x in num[8].upper():
                    radius = x[-1]
                    stol_v = 1
                    break

        if len(num[4]) > 2 and num[4][2] not in ('L', 'R') and num[4].isdigit() == False:
            eto_stol = 1
            txtss = stol_ss(num, dlina, visota, radius, stol_v)
            txtnc = stol_nc(num, dlina, visota, radius, stol_v)

        txtit = txtit.replace('LLL', dlina).replace('WWW', visota).replace('RRR', radius)
        txtss = txtss.replace('LLL', dlina).replace('WWW', visota).replace('RRR', radius)
        txtnc = txtnc.replace('LLL', dlina).replace('WWW', visota).replace('RRR', radius)

        if len(num[4]) > 2 and num[4][2:4] == 'LR':
            txtss = txtss.replace("WEEKE BHC T.", "БАЗА 8 и 5 попалам")
            num[4] = num[4][:2]
        elif len(num[4]) > 2 and num[4][2] == 'L':
            txtss = txtss.replace("WEEKE BHC T.", "БАЗА № 5")
            num[4] = num[4][:2]
        elif len(num[4]) > 2 and num[4][2] == 'R':
            txtss = txtss.replace("WEEKE BHC T.", "БАЗА № 8")
            num[4] = num[4][:2]

        if num[7] == 'Фасад2' or num[4] in ('998', '999'):
            txtss = txtss.replace("WEEKE BHC T.", "На Италянском тоже есть")

        print(*num)

        if int(dlina) < 75 or int(visota) < 75:
            txtss = txtss.replace('F_="8', 'F_="4').replace('ZA="-2', 'ZA="0.8')
            txtnc = txtnc.replace('F_="8', 'F_="4').replace('ZA="t-16.7', 'ZA="t-15.3')

        Steklo_kray = ['16', '17', '18', '19', '21', '22', '23', '24',
                       '25', '26', '31', '114', '115', '116', '119']
        if (num[7] == 'СТЕКЛО' or num[7] == 'Хлеб_ст') and (num[4] in (Steklo_kray)):
            txtss = txtss.replace("\MMMMM", steklo16(num, dlina, visota, ram))
            txtnc = txtnc.replace("\MMMMM", steklo16nc(num, dlina, visota, ram))

        if num[7] in ('ПЕРЕПЛЕТ', 'ПЕРЕПЛЕТ2'):
            for i in ['R4', 'r4', 'Р4', 'р4']:
                if i in num[8]:
                    num[8] = num[8].replace(i, '')
            if num[4] == "16": num[4] = "20"
            if num[8] != '' and ('8' in num[8]):
                num[7] = 'ПЕРЕПЛЕТ8'
            elif num[8] != '' and ('4' in num[8]) and num[7] == 'ПЕРЕПЛЕТ':
                num[7] = 'ПЕРЕПЛЕТ4'
            elif num[8] != '' and ('4' in num[8]) and num[7] == 'ПЕРЕПЛЕТ2':
                num[7] = 'ПЕРЕПЛЕТ4_xl'

        if len(num[7]) != 0 and num[7][:-1] == 'Бленда':
            txtss = txtss.replace("\FFFFF", ss_blenda(num, dlina, visota))
            if num[7] == 'Бленда2' and num[5] == '11':
                txtss = txtss.replace('t-19', 't-34.2')
                txtss = txtss.replace('158', '146')
        elif num[4] == '11':
            txtit = txtit.replace("' kray", it_11(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_11(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_11(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '12':
            txtit = txtit.replace("' kray", it_12(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_12(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_12(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '13':
            txtit = txtit.replace("' kray", it_13(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_13(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_13(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '14':
            txtit = txtit.replace("' kray", it_14(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_14(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_14(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '17' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_17(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_17(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_17(num, dlina, visota))
        elif num[4] == '18' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_18(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_18(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_18(num, dlina, visota))
        elif num[4] == '19' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_19(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_19(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_19(num, dlina, visota))
        elif num[4] == '20':
            txtit = txtit.replace("' kray", it_20(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_20(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", ss_20(num, dlina, visota, ram))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '21' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_21(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_21(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_21(num, dlina, visota))
        elif num[4] == '22' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_22(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_22(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_22(num, dlina, visota))
        elif num[4] == '23' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_23(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_23(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_23(num, dlina, visota))
        elif num[4] == '24' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_24(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_24(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_24(num, dlina, visota))
        elif num[4] == '25' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_25(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_25(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_25(num, dlina, visota))
        elif num[4] == '26' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_26(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_26(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_26(num, dlina, visota))
        elif num[4] == '27':
            txtit = txtit.replace("' kray", it_27(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_27(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_27(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '28':
            txtit = txtit.replace("' kray", it_28(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_28(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_28(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '29':
            txtit = txtit.replace("' kray", it_29(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_29(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_29(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '30':
            txtit = txtit.replace("' kray", it_30(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_30(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_30(num, dlina, visota))
        elif num[4] == '31' and num[7] not in ('СТЕКЛО', 'Хлеб_ст'):
            txtit = txtit.replace("' kray", it_31(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_31(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_31(num, dlina, visota))
        elif num[4] == '32':
            txtit = txtit.replace("' kray", it_32(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_32(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_32(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '33':
            txtit = txtit.replace("' kray", it_33(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_33(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_33(num, dlina, visota))
        elif num[4] == '34':
            txtit = txtit.replace("' kray", it_34(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_34(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_34(num, dlina, visota))
            txtnc = txtnc.replace("146", "131")
        elif num[4] == '35':
            txtit = txtit.replace("' kray", it_35(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_35(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", ss_35(num, dlina, visota))
        elif num[4] == '36':
            # txtit = txtit.replace("' kray", it_36(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_36(num, dlina, visota, ram))
            # txtnc = txtnc.replace("\FFFFF", nc_36(num, dlina, visota, ram))
        elif num[4] == '51':
            txtit = txtit.replace("' kray", it_51(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_51(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_51(num, dlina, visota, ram))
        elif num[4] == '52':
            txtit = txtit.replace("' kray", it_52(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_52(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_52(num, dlina, visota, ram))
        elif num[4] == '53':
            txtit = txtit.replace("' kray", it_53(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_53(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_53(num, dlina, visota, ram))
        elif num[4] == '54':
            txtit = txtit.replace("' kray", it_54(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_54(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_54(num, dlina, visota))
        elif num[4] == '55':
            txtit = txtit.replace("' kray", it_55(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_55(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_55(num, dlina, visota))
        elif num[4] == '56':
            txtit = txtit.replace("' kray", it_56(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_56(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_56(num, dlina, visota))
        elif num[4] == '57':
            txtit = txtit.replace("' kray", it_57(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_57(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_57(num, dlina, visota, ram))
        elif num[4] == '58':
            txtit = txtit.replace("' kray", it_58(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_58(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_58(num, dlina, visota))
        elif num[4] == '59':
            txtit = txtit.replace("' kray", it_59(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_59(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_59(num, dlina, visota))
        elif num[4] == '60':
            txtit = txtit.replace("' kray", it_60(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_60(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_60(num, dlina, visota))
        elif num[4] == '62':
            txtit = txtit.replace("' kray", it_62(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_62(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_62(num, dlina, visota, ram))
        elif num[4] == '63':
            txtit = txtit.replace("' kray", it_63(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_63(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_63(num, dlina, visota))
        elif num[4] == '64':
            txtit = txtit.replace("' kray", it_64(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_64(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_64(num, dlina, visota))
        elif num[4] == '65':
            txtit = txtit.replace("' kray", it_65(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_65(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_65(num, dlina, visota))
        elif num[4] == '66':
            txtit = txtit.replace("' kray", it_66(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_66(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_66(num, dlina, visota, ram))
        elif num[4] == '67':
            txtit = txtit.replace("' kray", it_67(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_67(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_67(num, dlina, visota, ram))
        elif num[4] == '68':
            txtit = txtit.replace("' kray", it_68(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_68(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_68(num, dlina, visota))
        elif num[4] == '69':
            txtit = txtit.replace("' kray", it_69(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_69(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_69(num, dlina, visota))
        elif num[4] == '70':
            txtit = txtit.replace("' kray", it_70(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_70(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_70(num, dlina, visota))
        elif num[4] == '71':
            txtit = txtit.replace("' kray", it_71(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_71(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_71(num, dlina, visota))
        elif num[4] == '72':
            txtit = txtit.replace("' kray", it_72(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_72(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_72(num, dlina, visota, ram))
        elif num[4] == '73':
            txtit = txtit.replace("' kray", it_73(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_73(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_73(num, dlina, visota, ram))
        elif num[4] == '74':
            txtit = txtit.replace("' kray", it_74(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_74(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_74(num, dlina, visota, ram))
        elif num[4] == '75':
            txtit = txtit.replace("' kray", it_75(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_75(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_75(num, dlina, visota, ram))
        elif num[4] == '76':
            txtit = txtit.replace("' kray", it_76(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_76(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_76(num, dlina, visota, ram))
        elif num[4] == '77':
            txtit = txtit.replace("' kray", it_77(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_77(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_77(num, dlina, visota, ram))
        elif num[4] == '78':
            txtit = txtit.replace("' kray", it_78(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_78(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_78(num, dlina, visota, ram))
        elif num[4] == '91':
            txtit = txtit.replace("' kray", it_91(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_91(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_91(num, dlina, visota, ram))
        elif num[4] == '92':
            txtit = txtit.replace("' kray", it_92(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_92(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_92(num, dlina, visota, ram))
        elif num[4] == '93':
            txtit = txtit.replace("' kray", it_93(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_93(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_93(num, dlina, visota, ram))
        elif num[4] == '94':
            txtit = txtit.replace("' kray", it_94(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_94(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_94(num, dlina, visota, ram))
        elif num[4] == '95':
            txtit = txtit.replace("' kray", it_95(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_95(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_95(num, dlina, visota))
        elif num[4] == '96':
            txtit = txtit.replace("' kray", it_96(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_96(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_96(num, dlina, visota, ram))
        elif num[4] == '97':
            txtit = txtit.replace("' kray", it_97(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_97(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_97(num, dlina, visota, ram))
        elif num[4] == '98':
            txtit = txtit.replace("' kray", it_98(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_98(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_98(num, dlina, visota, ram))
        elif num[4] == '99':
            txtit = txtit.replace("' kray", it_99(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_99(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_99(num, dlina, visota, ram))
        elif num[4] == '100':
            txtit = txtit.replace("' kray", it_100(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_100(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_100(num, dlina, visota, ram))
        elif num[4] == '103':
            txtit = txtit.replace("' kray", it_103(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_103(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_103(num, dlina, visota, ram))
        elif num[4] == '104':
            txtit = txtit.replace("' kray", it_104(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_104(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_104(num, dlina, visota, ram))
        elif num[4] == '105':
            txtit = txtit.replace("' kray", it_105(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_105(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_105(num, dlina, visota, ram))
        elif num[4] == '106':
            txtit = txtit.replace("' kray", it_106(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_106(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_106(num, dlina, visota, ram))
        elif num[4] == '107':
            txtit = txtit.replace("' kray", it_107(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_107(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_107(num, dlina, visota, ram))
        elif num[4] == '108':
            txtit = txtit.replace("' kray", it_108(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_108(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_108(num, dlina, visota, ram))
        elif num[4] == '109':
            txtit = txtit.replace("' kray", it_109(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_109(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_109(num, dlina, visota, ram))
        elif num[4] == '110':
            txtit = txtit.replace("' kray", it_110(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_110(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_110(num, dlina, visota, ram))
        elif num[4] == '111':
            txtit = txtit.replace("' kray", it_111(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_111(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_111(num, dlina, visota, ram))
        elif num[4] == '112':
            txtit = txtit.replace("' kray", it_112(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_112(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_112(num, dlina, visota, ram))
        elif num[4] == '113':
            txtit = txtit.replace("' kray", it_113(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_113(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_113(num, dlina, visota, ram))
        elif num[4] == '114':
            txtit = txtit.replace("' kray", it_114(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_114(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_114(num, dlina, visota, ram))
        elif num[4] == '115':
            txtit = txtit.replace("' kray", it_115(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_115(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_115(num, dlina, visota, ram))
        elif num[4] == '116':
            txtit = txtit.replace("' kray", it_116(num, dlina, visota))
            txtss = txtss.replace("\FFFFF", ss_116(num, dlina, visota))
            txtnc = txtnc.replace("\FFFFF", nc_116(num, dlina, visota))
        elif num[4] == '117':
            txtit = txtit.replace("' kray", it_117(num, dlina, visota, ram))
            # txtss = txtss.replace("\FFFFF", ss_117(num, dlina, visota, ram))
            # txtnc = txtnc.replace("\FFFFF", nc_117(num, dlina, visota, ram))
        elif num[4] == '118':
            txtit = txtit.replace("' kray", it_118(num, dlina, visota, ram))
            # txtss = txtss.replace("\FFFFF", ss_118(num, dlina, visota, ram))
            # txtnc = txtnc.replace("\FFFFF", nc_118(num, dlina, visota, ram))
        elif num[4] == '119':
            txtit = txtit.replace("' kr119", it_119(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_119(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_119(num, dlina, visota, ram))
        elif num[4] == '120':
            txtit = txtit.replace("' kr119", it_120(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_120(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_120(num, dlina, visota, ram))
        elif num[4] == '125':
            txtit = txtit.replace("' kray", it_125(num, dlina, visota, ram))
            # txtss = txtss.replace("\FFFFF", ss_119(num, dlina, visota))
            # txtnc = txtnc.replace("\FFFFF", nc_119(num, dlina, visota))
        elif num[4] == '150':
            txtit = txtit.replace("' kr17", it_150(num, dlina, visota, ram))
            # txtss = txtss.replace("\FFFFF", ss_119(num, dlina, visota))
            # txtnc = txtnc.replace("\FFFFF", nc_119(num, dlina, visota))
        elif num[4] == '201':
            txtss = txtss.replace("\FFFFF", ss_201(num, ram))
        elif num[4] == '202':
            txtit = txtit.replace("' kray", it_202(num, dlina, visota, ram))
        elif num[4] == '203':
            txtnc = nc_203(num, l_th, w_th, ram, radius)
        elif num[4] == '998':
            txtit = txtit.replace("' kray", it_998(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_998(num, dlina, visota, ram))
            txtnc = txtnc.replace("\FFFFF", nc_998(num, dlina, visota, ram))
        elif num[4] == '999':
            txtit = txtit.replace("' kray", it_999(num, dlina, visota, ram))
            txtss = txtss.replace("\FFFFF", ss_999(num, dlina, visota, ram))

        # край купе
        if "kupe" in num[8].lower():
            rm = num[8].split()
            with open('pl/kupe_it.txt', 'r', encoding='utf-8') as file_it:
                kupe_it = file_it.read().replace("vis", f"LPZ-{rm[-2]}").replace("shir", f"{rm[-1]}")
                txtit = txtit.replace("' kr17", kupe_it)
            with open('pl/kupe_ss.txt', 'r', encoding='utf-8') as file_ss:
                kupe_ss = file_ss.read().replace("vis", f"{rm[-2]}").replace("shir", f"{rm[-1]}")
                txtss = txtss.replace("/17", kupe_ss)
                txtss = txtss.replace('kupe_ss', str(txtss.count(']')))
                txtss = txtss.replace("WEEKE BHC T.", "На Италянском тоже есть")

        if num[5] == '17':  # 17 ий край
            Txt17it = open('pl/17_it.txt', 'r').read()
            # if "' kray18" in txtit:
            #     txtit = txtit.replace("' kray18", Txt17it)
            # else:
            #     txtit = txtit.replace("' kr17", Txt17it)
            txtit = txtit.replace("' kr17", Txt17it)

            Txt17ss = open('pl/17_ss.txt', 'r').read()
            Txt17nc = open('pl/17_nc.txt', 'r').read()
            if "/18_kray" in txtss:
                txtss = txtss.replace("/18_kray", Txt17ss)
                txtnc = txtnc.replace("/18_kray", Txt17nc)
                txtss = txtss.replace('18_KR', str(txtss.count(']')))
                txtnc = txtnc.replace('18_KR', str(txtnc.count(']')))
            else:
                txtss = txtss.replace("/17", Txt17ss)
                txtnc = txtnc.replace("/17", Txt17nc)
                txtss = txtss.replace('18_KR', str(txtss.count(']')))
                txtnc = txtnc.replace('18_KR', str(txtnc.count(']')))

        if num[5] == '18':  # 18 ий край
            Txt18it = open('pl/18_it.txt', 'r').read()
            # if "' kray18" in txtit:
            #     txtit = txtit.replace("' kray18", Txt18it)
            # else:
            #     txtit = txtit.replace("' kr17", Txt18it)
            txtit = txtit.replace("' kr17", Txt18it)

            Txt18ss = open('pl/18_ss.txt', 'r').read()
            if "/18_kray" in txtss:
                txtss = txtss.replace("/18_kray", Txt18ss)
                txtnc = txtnc.replace("/18_kray", Txt18ss)
                txtss = txtss.replace('18_KR', str(txtss.count(']')))
                txtnc = txtnc.replace('18_KR', str(txtnc.count(']')))
            else:
                txtss = txtss.replace("/17", Txt18ss)
                txtnc = txtnc.replace("/17", Txt18ss)
                txtss = txtss.replace('18_KR', str(txtss.count(']')))
                txtnc = txtnc.replace('18_KR', str(txtnc.count(']')))

        if int(visota) > 799 and int(dlina) > 799:  # большие детали на 1-ую базу
            txtit = txtit.replace('PAN=ORLST|"5"|', 'PAN=ORLST|"1"|')
            txtit = txtit.replace('@ OFFSET, 0 : 1.5, -1.5', '@ OFFSET, 0 : 1.5, 1.5')

        if len(num[8]) != 0 and num[8][:2] == '19':
            txtit = txtit.replace('LPZ|16.2', 'LPZ|19.2')
            txtit = txtit.replace('0, 15.2, 0,', '0, 18.2, 0,')
            txtss = txtss.replace('t=16.20', 't=19.0')
            txtss = txtss.replace('t-15.3', 't-18.2')
            txtnc = txtnc.replace('16.20+tPODK', '19.00+tPODK')
            txtnc = txtnc.replace('t-15.3', 't-18.2')
            txtnc = txtnc.replace('t-16.301', 't-19.3')

        if len(num[8]) != 0 and num[8][:2] == '22':
            txtit = txtit.replace('LPZ|16.2', 'LPZ|22.4')
            txtit = txtit.replace('0, 15.2, 0,', '0, 21.2, 0,')
            txtss = txtss.replace('t=16.20', 't=22.4')
            txtss = txtss.replace('t-15.3', 't-21.2')
            txtnc = txtnc.replace('16.20+tPODK', '22.4+tPODK')
            txtnc = txtnc.replace('t-15.3', 't-21.2')
            txtnc = txtnc.replace('t-16.301', 't-22.7')

        if int(dlina) >= 75 and int(visota) >= 75:
            if len(num[8]) != 0 and num[8][:2] == '19' and (num[5] in ('11', '14', '19')):
                Txt19it = open('pl/19_it.txt', 'r').read()
                txtit = txtit.replace("' kr19", Txt19it)

            if len(num[8]) != 0 and num[8][:2] == '22' and (num[5] in ('11', '14', '19')):
                Txt19it = open('pl/19_it.txt', 'r').read()
                txtit = txtit.replace("' kr19", Txt19it)

            if len(num[8]) != 0 and num[8][:2] == '19' and (num[5] in ('14', '15', '19')):
                Txt19ss = open('pl/19_ss.txt', 'r').read()
                txtss = txtss.replace("/PLAST", Txt19ss)

            if len(num[8]) != 0 and num[8][:2] == '22' and (num[5] in ('11', '14', '15', '19')):
                Txt19ss = open('pl/19_ss.txt', 'r').read()
                txtss = txtss.replace("/PLAST", Txt19ss)

            if len(num[8]) != 0 and num[8][:2] == '19' and (num[5] in ('11', '14', '19')):
                Txt19nc = open('pl/19_nc.txt', 'r').read()
                txtnc = txtnc.replace("/PLAST", Txt19nc)

            if len(num[8]) != 0 and num[8][:2] == '22' and (num[5] in ('11', '14', '19')):
                Txt19nc = open('pl/19_nc.txt', 'r').read()
                txtnc = txtnc.replace("/PLAST", Txt19nc)

        if len(num[8]) != 0 and num[8][:2] == '10':
            txtss = txtss.replace('t=16.20', 't=10.0')
            txtnc = txtnc.replace('16.20+tPODK', '10.00+tPODK')
            txtit = txtit.replace('LPZ|16.2', 'LPZ|10.0')

        # Италянский станок T_9, T_3
        txtit = txtit.replace('T_9', '9')
        txtit = txtit.replace('T_3', '3.06')
        txtit = txtit.replace('T_7.5', '7.5')
        txtit = txtit.replace('T_1.5', '1.56')

        # nc станок T_9, T_3
        txtnc = txtnc.replace('T_3', '3.07')
        txtnc = txtnc.replace('T_1.5', '1.57')

        # ss станок T_9, T_3
        txtss = txtss.replace('T_3', '3')
        txtss = txtss.replace('T_1.5', '1.5')

        
# --------------split

        # без расширения
        if fr_157 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "156"', "'" + ' ROUT, 0 : "156"')
            txtss = txtss.replace('TNO="156"', 'TNO="156"\nEN="0"')
            txtnc = txtnc.replace('TNO="156"', 'TNO="156"\nEN="0"')

        # без 144_1
        if fr_1441 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "144_1"', "'" + ' ROUT, 0 : "144_1"')
            txtit = txtit.replace('@ ROUT, 0 : "150_1"', "'" + ' ROUT, 0 : "150_1"')
            txtss = txtss.replace('EN="1"', 'EN="0"')
            txtnc = txtnc.replace('EN="1"', 'EN="0"')
            txtss = txtss.replace("<144_1", 'EN="0"')
            txtnc = txtnc.replace("<144_1", 'EN="0"')

        # без 144_2
        if fr_1442 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "144_2"', "'" + ' ROUT, 0 : "144_2"')
            txtit = txtit.replace('@ ROUT, 0 : "150_2"', "'" + ' ROUT, 0 : "150_2"')
            txtss = txtss.replace("<144_2", 'EN="0"')
            txtnc = txtnc.replace("<144_2", 'EN="0"')

        # без 144_3
        if fr_1443 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "144_3"', "'" + ' ROUT, 0 : "144_3"')
            txtss = txtss.replace("<144_3", 'EN="0"')
            txtnc = txtnc.replace("<144_3", 'EN="0"')

        # без 136_1
        if fr_1361 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "136_1"', "'" + ' ROUT, 0 : "136_1"')
            txtss = txtss.replace("\\136_1\\", 'EN="0"')
            txtnc = txtnc.replace("\\136_1\\", 'EN="0"')

        # без 136_2
        if fr_1362 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "136_2"', "'" + ' ROUT, 0 : "136_2"')
            txtss = txtss.replace("\\136_2\\", 'EN="0"')
            txtnc = txtnc.replace("\\136_2\\", 'EN="0"')

        # без 136_3
        if fr_1363 == 1:
            txtit = txtit.replace('@ ROUT, 0 : "136_3"', "'" + ' ROUT, 0 : "136_3"')
            txtss = txtss.replace("\\136_3\\", 'EN="0"')
            txtnc = txtnc.replace("\\136_3\\", 'EN="0"')

        # под 45
        if fr_pod_45 == 1:
            pod_45 = open('pl/pod45.txt', 'r').read()
            txtss = txtss.replace("\\pod45\\", pod_45)
            txtnc = txtnc.replace("\\pod45\\", pod_45)
            txtss = txtss.replace("888", str(txtss.count(']')))
            txtnc = txtnc.replace("888", str(txtnc.count(']')))
            pod_45_it = open('pl/pod45_it.txt', 'r').read()
            txtit = txtit.replace("' pod45", pod_45_it)


        if 170 <= int(dlina) < 550 and 146 <= int(visota) < 170:
            TxtKORD = open('pl/kord.txt', 'r').read()
            txtss = txtss.replace("KO=0", "KO=04")
            txtss = txtss.replace("<KORD", TxtKORD)
            txtss = txtss.replace("X=l", "X=" + dlina)
            txtss = txtss.replace("Y=w", "Y=" + visota)
            txtss = txtss.replace("XKORD", visota)
            txtss = txtss.replace('FNX="1"', 'FNX="43"')
            txtss = txtss.replace("l=" + dlina, "l=" + visota, 1)
            txtss = txtss.replace("w=" + visota, "w=" + dlina, 1)
            txtss = txtss.replace('FN=""', 'FN=""\nEN="0"')

        txtss = pr_ss(num, dlina, visota, txtss, eto_stol)  # присоски

        poz, difis = "_poz", ''
        if num[7][:6] in ('ПЕРЕПЛ', 'СТЕКЛО', 'Хлеб_с'): poz = "_St_poz"
        if not os.path.isdir('it/' + zak + "it"):
            os.mkdir('it/' + zak + "it")
        if not os.path.isdir('ss/' + zak + "h"):
            os.mkdir('ss/' + zak + "h")
        if not os.path.isdir('nc/' + zak + "nc"):
            os.mkdir('nc/' + zak + "nc")

        if len(num[8]) != 0 and num[8][:2] == '22': difis = 's'
        if len(num[8]) != 0 and num[8][:2] == '32': difis = '_'

        with open('it/' + zak + "it/" + difis + l_th + "x" + w_th + poz + num[0] + ".bpp", "w") as file_it:
            file_it.write(txtit)

        with open('ss/' + zak + "h/" + difis + l_th + "x" + w_th + poz + num[0] + ".mpr", "w") as file_ss:
            file_ss.write(txtss)

        with open('nc/' + zak + "nc/" + difis + l_th + "x" + w_th + poz + num[0] + ".mpr", "w") as file_nc:
            file_nc.write(txtnc)

        radius, stol_v, eto_stol = '5', 0, 0
