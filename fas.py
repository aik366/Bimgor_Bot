import datetime
import time
from datetime import date, timedelta
from time import strftime
import shutil
from config import put
import requests
from pochta import gmail
import os
import json
from random import randint

month, month_1 = strftime('%y'), str(int(strftime('%y')) - 1)
month_dict = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь',
              '07': 'Июль', '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
mesyac = {'Январь': '01', 'Февраль': '02', 'Март': '03', 'Апрель': '04', 'Май': '05', 'Июнь': '06', 'Июль': '07',
          'Август': '08', 'Сентябрь': '09', 'Октябрь': '10', 'Ноябрь': '11', 'Декабрь': '12'}


def read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_json(filename, collection):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(collection, file, ensure_ascii=False, indent=2)


def two_years_month(moon):
    if month_dict[moon] in ('Январь', 'Февраль', 'Март', 'Апрель'):
        shutil.copyfile(f'{put}{month}.RSB', f'DATA/two_years_month.txt')
        shutil.copyfile(f'{put}{month_1}.RSB', f'DATA/{month_1}_shef.txt')
        with open(f'DATA/{month_1}_shef.txt', 'r+') as files:
            with open(f'DATA/two_years_month.txt', 'a') as filess:
                filess.write(files.read())
    else:
        shutil.copyfile(f'{put}{month}.RSB', f'DATA/two_years_month.txt')


def two_years():
    shutil.copyfile(f'{put}{month}.RSB', f'DATA/two_years.txt')
    shutil.copyfile(f'{put}{month_1}.RSB', f'DATA/{month_1}_shef.txt')
    with open(f'DATA/{month_1}_shef.txt', 'r+') as files:
        with open(f'DATA/two_years.txt', 'a') as filess:
            filess.write(files.read())


async def send_msg_cron(e):
    gmail.gmail_bimgor()


async def shutdown(e):
    os.system("shutdown -t 0 -r -f")


async def zamen_smol(e):
    if order_number():
        for zakaz in order_number():
            change_namber(zakaz)
            zamena(1, zakaz)
    else:
        return


async def zamen_big(e):
    if order_number():
        for zakaz in order_number():
            zamena(0, zakaz)
    else:
        return


async def taskkill(e):
    process_name = "iSpy.exe"
    result = os.system(f"taskkill /f /im {process_name}")
    if result == 0:
        print(f"Instance deletion successful: {process_name}")
    else:
        print("Error occurred while deleting the instance.")


async def update_func(e):
    shutil.copyfile(f'{put}{month}.RSB', 'DATA/22.txt')
    shutil.copyfile(f'DATA/22.txt', f'DATA/two_years.txt')
    shutil.copyfile(f'DATA/22.txt', f'DATA/{month}_client.txt')
    shutil.copyfile(f'{put}{month_1}.RSB', f'DATA/{month_1}_client.txt')
    with open(f'DATA/{month_1}_client.txt', 'r+') as files:
        with open(f'DATA/two_years.txt', 'a') as filess:
            filess.write(files.read())
    print("Обновлено!!!")


def fasad(zakaz):
    with open('DATA/22.txt') as file:
        f = file.read().split('#@#')
        k = []
        for i in f:
            if i[1:5] == zakaz:
                for j in i.split('\n')[3:-1]:
                    k += [j.replace('|ш|', '||', 1).replace('||', '|', 1).replace('/', '|', 1).split('|')[:10]]
                break
    return k


def serd_nomer(zakaz, surname):
    with open('DATA/22.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:][::-1]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() == surname and st0[16][:4] == zakaz[1:]:
                return st0[0]


def serd_nomer_4(zakaz, surname):
    with open('DATA/22.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:][::-1]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() == surname and st0[16][:4] == zakaz:
                return st0[0]


def serdyuch(order):
    with open('DATA/22.txt') as f:
        k22 = ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1, srochno = i[0].split('|'), i[1].split('|'), ''
            if st0[0] == order:
                if st1[25][5] != "1":
                    if st1[28] not in '':
                        srochno = f'✌{round(float(st1[28].lstrip()))}✌|'
                    pl2 = f'{st0[18]}|' if st0[18] else ''
                    pl3 = f'{st0[19]}|' if st0[19] else ''
                    k22 += (
                        f'{st0[0]}|{st0[1].strip()}|{st0[16]}|\n{st0[2]} ➡️ {st0[3]}|{srochno}\nцвет {st0[17]}|{pl2}{pl3}'
                        f'метраж {st0[23]}|кол. {st0[24]}|\n')
                    ch1 = f'[{st0[8]}]' if st1[25][1] == '1' else '-'
                    ch2 = f'[{st0[9]}]' if st1[25][2] == '1' else '-'
                    ch3 = f'[{st0[10]}]' if st1[25][3] == '1' else '-'
                    k22 += f'раскрой{ch1}|фрезер{ch2}|пресс{ch3}\n{25 * "-"}\n'
                    for s in i[2:]:
                        s = s.replace('/', '|').split('|')
                        k22 += f'{s[0]}|{s[1]}|{s[2]}|{s[3]}|{s[5]}|{s[6]}|{s[7]}|{s[8]}|{s[9]}\n'
                    break
                else:
                    pl2 = f'{st0[18]}|' if st0[18] else ''
                    pl3 = f'{st0[19]}|' if st0[19] else ''
                    k22 += (
                        f'{st0[0]}|{st0[1].strip()}|{st0[16]}|\n{st0[2]} ➡️ {st0[3]}\nцвет {st0[17]}|{pl2}{pl3}'
                        f'метраж {st0[23]}|кол. {st0[24]}|\n')
                    k22 += f'*Этот заказ снят с производства*\n{25 * "-"}\n'
                    for s in i[2:]:
                        s = s.replace('/', '|').split('|')
                        k22 += f'{s[0]}|{s[1]}|{s[2]}|{s[3]}|{s[5]}|{s[6]}|{s[7]}|{s[8]}|{s[9]}\n'
                    break
        else:
            return "нет такого заказа"

        return k22


def order_name(order, name):
    with open('DATA/22.txt') as f:
        k22 = ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1, srochno = i[0].split('|'), i[1].split('|'), ''
            if st0[0] == order and name == st0[1].strip():
                if st1[25][5] != "1":
                    if st1[28] not in '':
                        srochno = f'✌{round(float(st1[28].lstrip()))}✌|'
                    pl2 = f'{st0[18]}|' if st0[18] else ''
                    pl3 = f'{st0[19]}|' if st0[19] else ''
                    k22 += (
                        f'{st0[0]}|{st0[1].strip()}|{st0[16]}|\n{st0[2]} ➡️ {st0[3]}|{srochno}\nцвет {st0[17]}|{pl2}{pl3}'
                        f'метраж {st0[23]}|кол. {st0[24]}|\n')
                    ch1 = f'[{st0[8]}]' if st1[25][1] == '1' else '-'
                    ch2 = f'[{st0[9]}]' if st1[25][2] == '1' else '-'
                    ch3 = f'[{st0[10]}]' if st1[25][3] == '1' else '-'
                    k22 += f'раскрой{ch1}|фрезер{ch2}|пресс{ch3}\n{25 * "-"}\n'
                    for s in i[2:]:
                        s = s.replace('/', '|').split('|')
                        k22 += f'{s[0]}|{s[1]}|{s[2]}|{s[3]}|{s[5]}|{s[6]}|{s[7]}|{s[8]}|{s[9]}\n'
                    break
                else:
                    pl2 = f'{st0[18]}|' if st0[18] else ''
                    pl3 = f'{st0[19]}|' if st0[19] else ''
                    k22 += (
                        f'{st0[0]}|{st0[1].strip()}|{st0[16]}|\n{st0[2]} ➡️ {st0[3]}\nцвет {st0[17]}|{pl2}{pl3}'
                        f'метраж {st0[23]}|кол. {st0[24]}|\n')
                    k22 += f'*Этот заказ снят с производства*\n{25 * "-"}\n'
                    for s in i[2:]:
                        s = s.replace('/', '|').split('|')
                        k22 += f'{s[0]}|{s[1]}|{s[2]}|{s[3]}|{s[5]}|{s[6]}|{s[7]}|{s[8]}|{s[9]}\n'
                    break
        else:
            return "нет такого заказа"

        return k22


def otmetka_program(zak_az):
    shutil.copyfile(f'{put}{month}.RSB', f'DATA/temp{month}.txt')
    with open('DATA/22.txt', 'r') as file:
        a = file.readlines()
        for j in zak_az:
            for line in range(len(a)):
                if a[line].strip()[:4] == j:
                    st0, st1 = a[line].split("|"), a[line + 1].split("|")
                    st0[7] = strftime('%d.%m')
                    st1[25] = f"2{st1[25][1:]}"
                    a[line], a[line + 1] = "|".join(st0), "|".join(st1)
                    break
    with open('DATA/temp.txt', 'w') as file:
        file.writelines(a)
    shutil.copyfile('DATA/temp.txt', f'{put}{month}.RSB')


def net_otchot(zakaz):
    a = open('DATA/22.txt', 'r+').readlines()
    for line in range(len(a)):
        S = a[line].split('|')
        if S[0] == zakaz:
            S_2 = a[line + 1].split('|')[:-1]
            a[line + 1] = '|'.join(S_2) + "|0\n"
            break
    open('DATA/temp.txt', 'w', ).writelines(a)
    shutil.copyfile('DATA/temp.txt', f'{put}{month}.RSB')


def net_program():
    b, n_zak = '', ''
    with open('DATA/22.txt', 'r') as f:
        for i in f.read().split('#@#')[1:]:
            s = i.strip().split('\n')[0:2]
            st1, st2, srochno = s[0].split('|'), s[1].split('|'), ''
            if st2[25][0] == '0' and st2[25][5] != '1':
                if st2[28] not in '':
                    srochno = f'✌{round(float(st2[28].lstrip()))}✌|'
                b += '|{}|{}|{}|{}\n'.format(st1[0], st1[1].strip(), st1[16], srochno)
                n_zak += st1[0] + '|'
        open('DATA/n_zak.txt', 'w').write(n_zak)
        return b if len(b) != 0 else 'нет заказов!'


def srochnost():
    two_years_month(strftime('%m'))
    with open('DATA/two_years_month.txt', 'r') as file:
        a = file.readlines()
        srochno = 0
        for line in range(len(a)):
            S = a[line].split('|')
            if len(S) > 14 and S[5][:2] == strftime("%y") and S[14] == strftime("%m"):
                s_sled = a[line + 1].split('|')
                if s_sled[28] not in '':
                    srochno += round(float(s_sled[28].lstrip()))
    return f'{srochno:,} 👉 {srochno // 3:,} 👉 {srochno // 3 // 10:,} 👉 {srochno // 3 - srochno // 3 // 10:,}'


def srochnost_bud():
    two_years_month(strftime('%m'))
    with open('DATA/two_years_month.txt', 'r') as file:
        a = file.readlines()
        srochno_bud, d, itogo = 0, {}, ''
        for line in range(len(a)):
            S = a[line].split('|')
            if len(S) > 14 and len(S[0]) == 4 and S[14] == '  ' and S[12] == '  .  ':
                s_bud = a[line + 1].split('|')
                if len(s_bud) > 28 and s_bud[28] not in '':
                    srochno_sum = round(float(s_bud[28].lstrip()))
                    srochno_bud += srochno_sum
                    if S[2][:5] not in d:
                        d[S[2][:5]] = [f'{S[0]}|{S[1].rstrip()}|{srochno_sum}']
                    else:
                        d[S[2][:5]].append(f'{S[0]}|{S[1].rstrip()}|{srochno_sum}')
    for k, v in d.items():
        if len(v) > 1:
            itogo += "----\n"
        for num, i in enumerate(v, 1):
            itogo += f"({num}) {k}: {i}\n"
        if len(v) > 1:
            itogo += f'---- Итого: {k} = {sum(int(j.split("|")[2]) for j in v):,} ----\n'
    return f'Сумма: {srochno_bud:,}\n----\n{itogo}'


def rasxodi_new(data):
    with open(u'DATA/ras.txt', 'r') as file:
        for i in file.read().split('##')[1:]:
            if i.splitlines()[0] == f"{data}.{strftime('%Y')}":
                rasxod = i.splitlines()
                summ = sum(int(''.join(j.split()[:2])) for j in rasxod[1:])
                rasxod = f"Расходы за {rasxod[0]}\n" + '\n'.join(rasxod[1:])
                return rasxod, summ
    return "Нет данных", 0


def otchet(data):
    d_time = datetime.datetime(int(strftime('%Y')), int(data[-2:]), int(data[:2]))
    data_d = {5: 'Суббота', 6: 'Воскресение'}
    if d_time.weekday() in (5, 6):
        return f"{data} {data_d[d_time.weekday()]}"
    if data[-2:] in ('01', '02', '03', '04'):
        shutil.copyfile(f'{put}{month}.RSB', f'DATA/{month}_shef.txt')
        shutil.copyfile(f'{put}{month_1}.RSB', f'DATA/{month_1}_shef.txt')
        with open(f'DATA/{month_1}_shef.txt', 'r+') as files:
            with open(f'DATA/{month}_shef.txt', 'a') as filess:
                filess.write(files.read())
    with open(f'DATA/{month}_shef.txt') as f:
        predoplata = srochno = summa = 0
        metraj = oplata = skidka = 0.0
        oplata_str = "Заказы оплачены сегодня\n"
        pred_str = 'Предоплата\n'
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st1[26] == data and st0[5][-2:] == month:
                metraj += float(st0[23])
                oplata += float(st1[29])
                summa += int(st0[26])
                if st1[24] != '0':
                    sro_chno = round(float(st1[28].lstrip())) if st1[28] not in '' else 0.0
                    skidka += (float(st0[26]) - float(st1[29]) + sro_chno)
                if st1[28] not in '':
                    srochno += round(float(st1[28].lstrip()))
                oplata_str += f'{st0[0]}|{st0[1].strip()}|{st1[29]}\n'
            if st0[2][:5] == data and st0[27] != "0.00" and st0[2][-2:] == month:
                predoplata += int(float(st0[27]))
                pred_str += f'{st0[0]}|{st0[1].strip()}|{st0[27]}\n'
                metraj += float(st0[23])
                summa += int(st0[26])
                if st1[28] not in '':
                    srochno += round(float(st1[28].lstrip()))
        kassa = round(oplata, 0) + predoplata + rasxodi_new(data)[1]
        itogo = (f"Отчет за {data}\n"
                 f"Общий Метраж: {round(metraj, 2)}\n"
                 f"Сумма Заказов: {summa}\n"
                 f"Предоплата: {predoplata}\n"
                 f"Оплата: {round(oplata, 0)}\n"
                 f"Срочность: {srochno}\n"
                 f"Скидки: {round(skidka, 1)}\n"
                 f"Расходы: {rasxodi_new(data)[1]}\n"
                 f"Касса: {kassa}\n\n{pred_str}\n{oplata_str}\n"
                 f"{rasxodi_new(data)[0]}")
        shutil.copyfile(f'{put}{month}.RSB', f'DATA/{month}_shef.txt')
        return itogo


def client(letter, year):
    d = {}
    with open(f'DATA/{year}_client.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1, summ_temp = i[0].split('|'), i[1].split('|'), 0.0
            if st0[1][0].upper() == letter and st0[12] == '  .  ' and st1[31] == "":
                sro_chno = 0.0 if st1[28] == '' else round(float(st1[28].lstrip()))
                if st0[25] != '0.00':
                    summ_temp = round(float(st0[27]) + float((st1[29]).strip()))
                else:
                    summ_temp = round(float(st0[26]) + sro_chno)
                if st0[1].strip() in d:
                    d[st0[1].strip()] += summ_temp
                else:
                    d[st0[1].strip()] = summ_temp
        return dict(sorted(d.items()))


# def client_user(user):
#     list1, summ1 = [], 0.0
#     with open(f'DATA/{month}_shef.txt') as f:
#         for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
#             st0, st1, summ_temp = i[0].split('|'), i[1].split('|'), 0.0
#             if st0[1].strip() == user and st0[12] == '  .  ' and st1[31] == "":
#                 sro_chno = 0.0 if st1[28] == '' else round(float(st1[28].lstrip()))
#                 summ_temp = round(float(st0[26]) + sro_chno)
#                 summ1 += summ_temp
#                 list1.append((st0[0], st0[2][:5], summ_temp))
#
#         return list1, int(summ1)

def client_user(user, year):
    mesyac = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь',
              '07': 'Июль', '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
    dict_name, month_sum, all_str = {}, {}, f"{user}\n\n"
    with open(f'DATA/{year}_client.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1, summ_temp = i[0].split('|'), i[1].split('|'), 0.0
            if st0[1].strip() == user and st0[12] == '  .  ' and st1[31] == "":
                sro_chno = 0.0 if st1[28] == '' else round(float(st1[28].lstrip()))
                if st0[25] != '0.00':
                    summ_temp = round(float(st0[27]) + float((st1[29]).strip()))
                else:
                    summ_temp = round(float(st0[26]) + sro_chno)
                if st0[2][3:5] not in dict_name:
                    month_sum[st0[2][3:5]] = summ_temp
                    dict_name[st0[2][3:5]] = [[st0[0], st0[2], summ_temp, summ_temp]]
                else:
                    month_sum[st0[2][3:5]] += summ_temp
                    dict_name[st0[2][3:5]].append([st0[0], st0[2], summ_temp, month_sum[st0[2][3:5]]])
        for k, v in dict_name.items():
            all_str += f"{mesyac[k]} - {month_sum[k]: ,}\n"
            for i in v:
                all_str += f"{i[0]}|{i[1]}|{i[2]: ,}\n"
            all_str += f"\n"
        all_str += f"Итого - {sum(month_sum.values()): ,}"
        return all_str


def dolgi_serdyuch(number_1, number_2):
    with open(f'DATA/{month}_shef.txt') as f:
        lst, summ = [], 0
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() == 'Сердюченко' and st0[12] == '  .  ' and st0[2][-2:] == month and int(number_1) <= int(
                    st0[16][:4]) <= int(number_2):
                lst.append(f'{st0[16][:4]}|{st0[0]}|{st0[2][:5]}|{round(float(st1[29])): ,}')
                summ += round(float(st1[29]))
    return summ, sorted(lst, key=lambda n: n[:4])


def dolgi_ser_data(data_1, data_2):
    with open(f'DATA/{month}_shef.txt') as f:
        lst, lst_d, summ, d = [], [], 0, ''
        d1 = date(int(strftime('%Y')), int(data_1[-2:]), int(data_1[:2]))  # начальная дата
        d2 = date(int(strftime('%Y')), int(data_2[-2:]), int(data_2[:2]))  # конечная дата
        delta = d2 - d1  # timedelta
        for j in range(delta.days + 1):
            d = str(d1 + timedelta(j))
            lst_d.append(f'{d[-2:]}.{d[5:7]}.{d[:4]}')
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() == 'Сердюченко' and st0[12] == '  .  ' and st0[2] in lst_d:
                lst.append(f'{st0[16][:4]}|{st0[0]}|{st0[2][:5]}|{round(float(st1[29])): ,}')
                summ += round(float(st1[29]))
    return summ, sorted(lst, key=lambda n: n[:4])


def today_func():
    today = date.today()
    friday = str(today + timedelta((4 - today.weekday()) % 7) - timedelta(7))
    if strftime('%a') in ('Sat', 'Sun'):
        return f'{friday[-2:]}.{friday[5:7]}'
    return strftime('%d.%m')


# def zarplata_2(mesec, year):
#     count, metraj, spisok, srochno = 1, 0.0, '', ''
#     col_Rost, col_R16 = 0, 0
#     P, R = [0.0] * 10, [0.0] * 4
#     if mesec in ('Январь', 'Февраль', 'Март', 'Апрель'):
#         shutil.copyfile(f'{put}{int(year) - 1}.RSB', f'DATA/{int(year) - 1}_shef.txt')
#         with open(f'DATA/{int(year) - 1}_shef.txt', 'r+') as files:
#             with open(f'DATA/{year}_shef.txt', 'a') as filess:
#                 filess.write(files.read())
#     a = open(f'DATA/{year}_shef.txt', 'r+').readlines()
#     for line in range(len(a) - 2):
#         B, A, C = a[line].split('|'), a[line + 1].split('|'), a[line + 2].split('|'),
#         if len(B[0]) == 4 and B[0].isdigit() and B[14] == mesyac[mesec] \
#                 and B[5][:2] == year and B[12] == '  .  ':
#             st_dart = ["Агаджанов", "Ростов", "Сорокин", "Миша Москва", "Кузнецов С"]
#             if len(C[9]) > 3 and B[1].strip() in st_dart and C[9][3] == "`":
#                 A[0] = "I  -  16 не ст-т"
#
#             K = [0.0] * 6
#             if A[0][9:11] == 'не':
#                 P[0] += float(A[12])
#                 K[0] += float(A[12])
#             elif A[0][9:11] == 'ст':
#                 P[1] += float(A[12])
#                 K[1] += float(A[12])
#             elif A[0][9:11] == 'АР':
#                 P[2] += float(A[12])
#                 K[2] += float(A[12])
#             elif A[0][4:6] == 'Фр':
#                 P[4] += float(A[12])
#                 K[4] += float(A[12])
#
#             if A[1][9:11] == 'не':
#                 P[0] += float(A[13])
#                 K[0] += float(A[13])
#             elif A[1][9:11] == 'ст':
#                 P[1] += float(A[13])
#                 K[1] += float(A[13])
#             elif A[1][9:11] == 'АР':
#                 P[2] += float(A[13])
#                 K[2] += float(A[13])
#             elif A[1][4:6] == 'Фр':
#                 P[4] += float(A[13])
#                 K[4] += float(A[13])
#
#             if A[2][9:11] == 'не':
#                 P[0] += float(A[14])
#                 K[0] += float(A[14])
#             elif A[2][9:11] == 'ст':
#                 P[1] += float(A[14])
#                 K[1] += float(A[14])
#             elif A[2][9:11] == 'АР':
#                 P[2] += float(A[14])
#                 K[2] += float(A[14])
#             elif A[2][4:6] == 'Фр':
#                 P[4] += float(A[14])
#                 K[4] += float(A[14])
#
#             if A[3][9:11] == 'не':
#                 P[0] += float(A[15])
#                 K[0] += float(A[15])
#             elif A[3][9:11] == 'ст':
#                 P[1] += float(A[15])
#                 K[1] += float(A[15])
#             elif A[3][9:11] == 'АР':
#                 P[2] += float(A[15])
#                 K[2] += float(A[15])
#             elif A[3][4:6] == 'Фр':
#                 P[4] += float(A[15])
#                 K[4] += float(A[15])
#
#             if A[4][9:11] == 'не':
#                 P[0] += float(A[16])
#                 K[0] += float(A[16])
#             elif A[4][9:11] == 'ст':
#                 P[1] += float(A[16])
#                 K[1] += float(A[16])
#             elif A[4][9:11] == 'АР':
#                 P[2] += float(A[16])
#                 K[2] += float(A[16])
#             elif A[4][4:6] == 'Фр':
#                 P[4] += float(A[16])
#                 K[4] += float(A[16])
#
#             K[5] = K[0] + K[1] + K[2] + K[3] + K[4]
#             if A[28] == '':
#                 P[6] += float(B[26])
#             else:
#                 P[6] += float(B[26]) + float(A[28])
#
#             # КАРНИЗЫ
#             if A[0][4:6] == "Кар":
#                 P[2] += float(A[12])
#
#             # Закатка
#             if A[0][4:6] == "За":
#                 P[5] += float(A[12])
#
#             # радиус
#             if A[19] != ' 0':
#                 for i in range(line, line + 50):
#                     D = a[i].split('|')
#                     if D[0][:3] == '#@#':
#                         break
#                     if len(D[5]) > 0 and D[5][0] == 'R' and D[5][1:3] != '16' and D[5] != 'RКАРНИЗ':
#                         col_Rost += int(D[3])
#                     if D[5] == 'R16':
#                         col_R16 += int(D[3])
#
#             # срочно
#             if A[28] != '':
#                 if A[28] == '1000.00': A[28] = '1000'
#                 P[3] += float(A[28])
#                 srochno += f'{B[0]}|{B[1].strip()}: {A[28].strip()}\n'
#
#             spisok += f'{B[0]}|{B[1].strip()}: {B[26]}\n'
#
#             count += 1
#             metraj = str(round(P[0] + P[1] + P[2] + P[4] + P[5], 2))
#     itogo = (f'Зарплата за {mesec} месяц 20{year} года\n\n'
#              f'ОБЩИЙ_МЕТРАЖ: {metraj}\n'
#              f'СТАНДАРТ: {P[1]:.2f}\n'
#              f'НЕ_СТАНДАРТ: {P[0]:.2f}\n'
#              f'КАРНИЗЫ: {P[2]:.2f}\n'
#              f'ЗАКАТКА: {P[5]:.2f}\n'
#              f'ФРЕЗЕРОВКА: {P[4]:.2f}\n'
#              f'Радиус_мыло: {col_R16}\n'
#              f'Радиус_остр.: {col_Rost}\n'
#              f'СРОЧНО: {round(P[3]): ,}\n'
#              f'ОБЩАЯ_СУММА: {round(P[6]): ,}')
#
#     return itogo, f'{spisok}\nсрочность\n\n{srochno}'


def zarplata(mesec, year):
    shutil.copyfile(f'{put}{year}.RSB', f'DATA/{year}_shef.txt')

    chist_name = ["Сергеева. Е.Г.", "Гребенюк", "Добрынин", "Дениченко", "ИВАНКИН А В", "Павленко", "Мусьяченко",
                  "Эллион", ]

    if mesec in ('Январь', 'Февраль', 'Март', 'Апрель'):
        shutil.copyfile(f'{put}{int(year) - 1}.RSB', f'DATA/{int(year) - 1}_shef.txt')
        with open(f'DATA/{int(year) - 1}_shef.txt', 'r+') as files:
            with open(f'DATA/{year}_shef.txt', 'a') as filess:
                filess.write(files.read())
    with open(f'DATA/{year}_shef.txt') as f:
        karniz, r_karniz, r_fasad, metraj, srochno, zakatka, num = 0.0, [0, 0], [0, 0], [], [], 0, 1
        summ, max_summ, bez_plenki, petli_summ, chist, chist_ser, str_obr = 0.0, 0.0, 0.0, 0, 0.0, 0.0, ''
        max_srochno, max_metraj, str_kor, str_dlino = 0, 0.0, f'Зарплата за {mesec} месяц {year} года', ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1, petli = i[0].split('|'), i[1].split('|'), i[-1].split('|')

            if st0[5][:2] == year and st0[12] == '  .  ' and st0[14] == mesyac[mesec]:

                max_metraj += float(st0[23])  # max Общий метраж
                if st1[28] == '':
                    summ = float(st0[26])
                else:
                    summ = float(st0[26]) + float(st1[28])
                metraj.append([num, st0[0], st0[1], float(st0[23]), round(summ)])
                max_summ += summ

                if st0[1].rstrip() in chist_name:  # Обр.чис
                    chist += float(st0[23])

                if st0[1].rstrip() == "Сердюченко" and "чист" in st0[16].lower():  # Обр.чис Сердюченко
                    chist_ser += float(st0[23])

                if st1[28] not in '':  # Срочность
                    srochno.append([num, st0[0], st0[1], round(float(st1[28].lstrip()))])
                    max_srochno += round(float(st1[28].lstrip()))

                if st1[0][4:6] == "За":  # Закатка
                    zakatka += float(st1[12])

                if st1[18] != " 0":  # Радиусний фасад
                    r_fasad[0] += int(st1[18])
                    r_fasad[1] += int(st1[20])

                if st1[21] != " 0":  # Радиусний карниз
                    r_karniz[0] += int(st1[21])
                    r_karniz[1] += int(st1[23])

                for j in range(6):
                    if st1[j][4:6] == 'Фр':  # Без пленки
                        bez_plenki += float(st1[j + 12])

                    if st1[j][-8:-1] == "КАРНисп":  # карниз
                        karniz += float(st1[j + 12])

                num += 1

        str_kor += f'\n\nМетраж {round(max_metraj, 2)} км.\n'
        str_kor += f'Карниз {round(karniz, 2)} км.\n'
        str_kor += (f'R_Карниз {r_karniz[0]} шт.\n'
                    f'R_Фасад {r_fasad[0]} шт.\n'
                    f'Закатка {round(zakatka, 2)} км.\n'
                    f'Фрезеровка {round(bez_plenki, 2)} км.\n'
                    f'Срочность {max_srochno: ,}\n'
                    f'Общая_сумма {int(max_summ): ,}\n')

        str_obr += (f'Обр.чист. {round(chist, 2)} км.\n'
                    f'Обр.чист._Серд. {round(chist_ser, 2)} км.\n')

        str_dlino = str_kor + '\n'
        for i in metraj:
            str_dlino += f'{i[1]}|{i[2].rstrip()}: {i[4]}\n'

        str_dlino += '\n          Срочные_Заказы\n'
        for i in srochno:
            str_dlino += f'{i[1]}|{i[2].rstrip()}: {i[3]}\n'

        return str_kor, str_dlino, str_obr


def currency():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    bitcoin = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()
    eth = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=ETH').json()

    usd = data['Valute']['USD']['Value']
    eur = data['Valute']['EUR']['Value']
    amd = data['Valute']['AMD']['Value']

    bitcoin = bitcoin['data']['rates']['USD']
    eth = eth['data']['rates']['USD']

    return f'''
USD - {usd:.2f}
EUR - {eur:.2f}
AMD - {100 / amd * 1000:.0f}

BITCOIN - {bitcoin}
ETH - {eth}
            '''


def dolgi_user():
    with open(f'DATA/two_years.txt') as f:
        d1, d2, d3 = {}, {}, {}
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() != 'Сердюченко' and st0[12] == '  .  ' and st1[26] == '' and st1[
                29] != ' 0' and st1[31] == "":  # st0[5][:2] != '  '

                if st0[1].strip() in d1:
                    d1[st0[1].strip()] += round(float(st1[29]))
                else:
                    d1[st0[1].strip()] = round(float(st1[29]))

    return dict(sorted(d1.items()))


def dolgi_user_2(user):
    with open(f'DATA/two_years.txt') as f:
        list1, list2, sum1, sum2 = [], [], 0, 0
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[1].strip() == user and st0[12] == '  .  ' and st1[26] == '' and st1[29] != ' 0' and st1[31] == "":
                if st0[5][:2] != '  ':
                    list1.append((st0[0], st0[2], round(float(st1[29]))))
                    sum1 += round(float(st1[29]))
                else:
                    list2.append((st0[0], st0[2], round(float(st1[29]))))
                    sum2 += round(float(st1[29]))

    return list1, list2, sum1, sum2


def raskroy():
    with open('DATA/22.txt') as f:
        d, a = {}, ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[12] == '  .  ' and st1[25][1] == '0':
                d[st0[0]] = [st0[3][:5], st0[23], st0[17]]
                if st0[18] != '': d[st0[0]].append(st0[18])
                if st0[19] != '': d[st0[0]].append(st0[19])
                if st0[11] == '  .  ':
                    patina = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(patina)[-2:]}.{str(patina)[5:7]}.{str(patina)[:4]}'
                if st1[28] != '' or st1[25][5] == '3':
                    sr_per = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(7)
                    st0[3] = f'{str(sr_per)[-2:]}.{str(sr_per)[5:7]}.{str(sr_per)[:4]}'
                if st1[0] == 'I  -Зак.Пл.Кл.':
                    zak_pl = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(zak_pl)[-2:]}.{str(zak_pl)[5:7]}.{str(zak_pl)[:4]}'
                today, d1 = date.today(), date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2]))
                d[st0[0]].append(str(-(today - d1).days))
        d = dict(sorted(d.items(), key=lambda item: int(item[1][-1])))
        for k, v in d.items():
            a += f'{k}|{"|".join(v)}\n'
        return a


def raskroy_ost():
    summ, kol, stroka = 0, 0, ''
    with open('DATA/22.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st1[25][1] == '0' and st0[12] == '  .  ' and st1[0][4:10] != 'Зак.Пл':
                kol += 1
                summ += float(st0[23])
                stroka += f'{st0[0]}|{st0[1].strip()}: {float(st0[23])}\n'
    return f"{stroka}Заказов: {kol} на {round(summ, 2)} км"


def raskroy_zarplata():
    summ, kol, stroka = 0, 0, ''
    with open('DATA/22.txt') as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[12] == '  .  ' and st1[25][1] == '1' and st0[14] == '  ':
                kol += 1
                summ += float(st0[23])
                stroka += f'{st0[0]}|{st0[1].strip()}: {float(st0[23])}\n'
    return f"{stroka}Заказов: {kol} на {round(summ, 2)} км"


def frezer():
    with open('DATA/22.txt') as f:
        d, a = {}, ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[12] == '  .  ' and st1[25][1] == '1' and st1[25][2] == '0':
                d[st0[0]] = [st0[3][:5], st0[23], st0[17]]
                if st0[18] != '': d[st0[0]].append(st0[18])
                if st0[19] != '': d[st0[0]].append(st0[19])
                if st0[11] == '  .  ':
                    patina = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(patina)[-2:]}.{str(patina)[5:7]}.{str(patina)[:4]}'
                if st1[28] != '' or st1[25][5] == '3':
                    sr_per = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(7)
                    st0[3] = f'{str(sr_per)[-2:]}.{str(sr_per)[5:7]}.{str(sr_per)[:4]}'
                if st1[0] == 'I  -Зак.Пл.Кл.':
                    zak_pl = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(zak_pl)[-2:]}.{str(zak_pl)[5:7]}.{str(zak_pl)[:4]}'
                today, d1 = date.today(), date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2]))
                d[st0[0]].append(str(-(today - d1).days))
        d = dict(sorted(d.items(), key=lambda item: int(item[1][-1])))
        for k, v in d.items():
            a += f'{k}|{"|".join(v)}\n'
        return a


def press():
    with open('DATA/22.txt') as f:
        d, a = {}, ''
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[12] == '  .  ' and st1[25][1] == '1' and st1[25][2] == '1' and st1[25][3] == '0':
                d[st0[0]] = [st0[3][:5], st0[23], st0[17]]
                if st0[18] != '': d[st0[0]].append(st0[18])
                if st0[19] != '': d[st0[0]].append(st0[19])
                if st0[11] == '  .  ':
                    patina = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(patina)[-2:]}.{str(patina)[5:7]}.{str(patina)[:4]}'
                if st1[28] != '' or st1[25][5] == '3':
                    sr_per = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(7)
                    st0[3] = f'{str(sr_per)[-2:]}.{str(sr_per)[5:7]}.{str(sr_per)[:4]}'
                if st1[0] == 'I  -Зак.Пл.Кл.':
                    zak_pl = date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2])) - timedelta(3)
                    st0[3] = f'{str(zak_pl)[-2:]}.{str(zak_pl)[5:7]}.{str(zak_pl)[:4]}'
                today, d1 = date.today(), date(int(st0[3][-4:]), int(st0[3][3:5]), int(st0[3][:2]))
                d[st0[0]].append(str(-(today - d1).days))
        d = dict(sorted(d.items(), key=lambda item: int(item[1][-1])))
        for k, v in d.items():
            a += f'{k}|{"|".join(v)}\n'
        return a


def zakaz_one(zak_str, zak_number='9990'):
    s = (f'#@#\n{zak_number}|ПРОСЧЕТ|||0|||||||||||0||1||| 0.6|||.4|2|0.00||||\n'
         f'||||||||||||.4|0|0|0|0|0| 0| 0| 0| 0| 0| 0|0|200010000|||| 0||\n')
    for n, i in enumerate(zak_str.split('\n'), 1):
        k = i.split('.')
        lst = f'{n}|{k[0]}|{k[1]}|1||{k[2]}|{k[3]}/{k[4]}|{k[5]}|{k[6]}|498|.5|.5|'
        s += f'{lst}\n'
    open('DATA/22.txt', 'a', ).write(s)


def statistics_plenka():
    with open('DATA/22.txt') as f:
        d = {}
        for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[17] not in '' and st0[20] not in '' and st0[12] == '  .  ':
                if st0[17].strip() not in d:
                    d[st0[17].strip()] = float(st0[20])
                else:
                    d[st0[17].strip()] += float(st0[20])
            if st0[18] not in '' and st0[21] not in '' and st0[12] == '  .  ':
                if st0[18].strip() not in d:
                    d[st0[18].strip()] = float(st0[21])
                else:
                    d[st0[18].strip()] += float(st0[21])
            if st0[19] not in '' and st0[22] not in '' and st0[12] == '  .  ':
                if st0[19].strip() not in d:
                    d[st0[19].strip()] = float(st0[22])
                else:
                    d[st0[19].strip()] += float(st0[22])
        value_sorted = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        s = ''
        for k, v in value_sorted.items():
            s += f'Пленка №: {k} = {round(v, 1)} м2\n'

        return s


def statistics_fasad():
    f = open('DATA/22.txt').read().split('#@#')
    d = {}
    for i in f:
        for j in i.split('\n')[3:-1]:
            tmp = [j.replace('|ш|', '|', 1).replace('||', '|', 1).replace('/', '|', 1).split('|')[4:11]]
            if len(tmp[0][0]) > 2 and tmp[0][0][2] in ("L", "R"):
                tmp[0][0] = tmp[0][0][:2]
            if tmp[0][0][:2].isdigit() and tmp[0][-1] not in "":
                if int(tmp[0][0]) not in d:
                    d[int(tmp[0][0])] = float(tmp[0][-1])
                else:
                    d[int(tmp[0][0])] += float(tmp[0][-1])
    s = ''
    for k, v in sorted(d.items()):
        s += f'Фасад {k} = {round(v, 1)} м2\n'
    return s


def statistics_mdf():
    f = open('DATA/22.txt').read().split('#@#')
    d = {10: 0.0, 16: 0.0, 19: 0.0, 22: 0.0, 32: 0.0}
    for i in f:
        for j in i.split('\n')[3:-1]:
            tmp = [j.replace('|ш|', '|', 1).replace('||', '|', 1).replace('/', '|', 1).split('|')[8:11]]
            if (tmp[0][0] == "" or tmp[0][0][:2] not in ("10", "19", "22", "32")) and tmp[0][-1] not in "":
                d[16] += float(tmp[0][-1])
            if tmp[0][0] not in "" and tmp[0][0][:2] == "10" and tmp[0][-1] not in "":
                d[10] += float(tmp[0][-1])
            if tmp[0][0] not in "" and tmp[0][0][:2] == "19" and tmp[0][-1] not in "":
                d[19] += float(tmp[0][-1])
            if tmp[0][0] not in "" and tmp[0][0][:2] == "22" and tmp[0][-1] not in "":
                d[22] += float(tmp[0][-1])
            if tmp[0][0] not in "" and tmp[0][0][:2] == "32" and tmp[0][-1] not in "":
                d[32] += float(tmp[0][-1])
    s = ''
    for k, v in d.items():
        s += f'МДФ {k}мм. = {round(v, 1)} м2\n'
    return s


# def change_open():
#     change_file = """# change_open
#     scheduler.add_job(zamen_smol, 'cron', day_of_week='mon-fri', hour=16, minute=50,
#                       start_date=datetime.now(), args=(dp,))
#     scheduler.add_job(zamen_big, 'cron', day_of_week='mon-fri', hour=17, minute=10,
#                       start_date=datetime.now(), args=(dp,))
#     # change_open"""

#     with open('bot_telegram.py', 'r', encoding='utf-8') as f:
#         change_bot = f.read()
#         if '# change_close' in change_bot:
#             change_bot = change_bot.replace('# change_close', change_file)

#             with open('bot_telegram.py', 'w', encoding='utf-8') as f:
#                 f.write(change_bot)
        

# def change_close():
#     with open('bot_telegram.py', 'r', encoding='utf-8') as f:
#         change_bot = f.read()
#         if '# change_open' in change_bot:
#             change_bot = change_bot.split('# change_open')
#             change_bot[1] = '# change_close'
#             change_bot = ''.join(change_bot)

#             with open('bot_telegram.py', 'w', encoding='utf-8') as f:
#                 f.write(change_bot)


if __name__ == '__main__':
    pass
