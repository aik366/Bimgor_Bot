import shutil
from config import fasadit


def xlebnica():
    s = open('../rs/202_it/xl.txt', 'w')
    my_split, a = [], ''
    with open('../rs/202_it/1.txt', 'r') as file:
        for line in file.readlines():
            my_file = line.split('\n')
            if my_file[0][0] == '@' or my_file[0] == '  ' or my_file[0][:11] == '  @ ENDPATH':
                s.write(my_file[0] + '\n')
                print(my_file)
            else:
                my_split = my_file[0].split(':')
                my_zopit = my_split[1].split(',')
                print(my_zopit[0], my_zopit[1])
                my_zopit[0] = my_zopit[0].replace('lpx', 'lpy')
                my_zopit[1] = my_zopit[1].replace('lpy', 'lpx')
                print(my_zopit[0], my_zopit[1])
                print(my_zopit)
                a = '{}:{},{},{}'.format(my_split[0], my_zopit[1], my_zopit[0], ','.join(my_zopit[2:]))
                s.write(a + '\n')


def kopy_fasadMDF_bot():
    with open('../Bimgor.py', 'r', encoding='UTF-8') as bimgor:
        my_bimgor = bimgor.read().split('# --------------split')
        s = ''
        for i in my_bimgor[1].split('\n'):
            s += i.replace('        ', '', 1) + '\n'

    with open(fasadit, 'r', encoding='UTF-8') as xl:
        my_fasadbg = xl.read().split('# --------------split')
        my_fasadbg[1] = s

    open('../tests/fasadit.py', 'w', encoding='UTF-8').write('# --------------split'.join(my_fasadbg))

    shutil.copyfile('../tests/fasadit.py', fasadit)


kopy_fasadMDF_bot()
# xlebnica()
