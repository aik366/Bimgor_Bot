import json
import shutil
from random import randint
from config import put
from time import strftime


month, month_1 = strftime('%y'), str(int(strftime('%y')) - 1)

def read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_json(filename, collection):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(collection, file, ensure_ascii=False, indent=2)


def zamena(oil, zakaz):
    file = read_json('DATA/zamena.json')

    shutil.copyfile(f'{put}{month}.RSB', 'DATA/gmail.txt')
    with open('DATA/gmail.txt', 'r') as f:
        file_22 = f.read().split('#@#')
        for i in range(len(file_22)):
            if zakaz in file_22[i][:5]:
                if oil == 1:
                    file_22[i] = file[zakaz][1]
                    break
                else:
                    file_22[i] = file[zakaz][0]
                    break
        file_22 = '#@#'.join(file_22)

    with open('DATA/gmail.txt', 'w') as f:
        f.write(file_22)
    shutil.copyfile('DATA/gmail.txt', f'{put}{month}.RSB')
    
    
def zamena_gmail(oil, zakaz):
    file = read_json('DATA/zamena.json')

    shutil.copyfile(f'{put}{month}.RSB', 'DATA/gmail.txt')
    with open('DATA/gmail.txt', 'r') as f:
        file_22 = f.read().split('#@#')
        for i in range(len(file_22)):
            if zakaz in file_22[i][:5]:
                if oil == 1:
                    file_22[i] = file[zakaz][1]
                    break
                else:
                    file_22[i] = file[zakaz][0]
                    break
        file_22 = '#@#'.join(file_22)

    with open('DATA/gmail.txt', 'w') as f:
        f.write(file_22)
       

def change_namber(zakaz):
    shutil.copyfile(f'{put}{month}.RSB', 'DATA/gmail.txt')
    with open('DATA/gmail.txt', 'r') as f:
        for i in f.read().split('#@#')[1:]:
            s = i.strip().split('\n')[0:2]
            st1, st2, change_txt = s[0].split('|'), s[1].split('|'), ""

            if st1[0] == zakaz:
                randx, randy = randint(110, 120), randint(450, 500)
                rxy = round(randx*randy/1000000, 2)
                many = str(int(rxy * int(st2[6])))
                my_list0 = f"||||0|      |  .  ||||  .  |--.--|  .  |  .  |  |0||||| 0.0|||{rxy}|1|0.00|{many}|0.00|П/белый|".split(
                    "|")
                my_list1 = f"I  -  16 ст-т||||||||||||{rxy}|0|0|0|0|0| 0| 0| 0| 0| 0| 0|0||||| {many}||".split("|")
                my_list2 = f"1|{randx}|{randy}|1||16|15/БФ|Фасад||{st1[17]}|{rxy}|{rxy}|".split("|")

                for j in (0, 1, 2, 3, 5, 7, 8, 9, 10, 14, 17):
                    my_list0[j] = st1[j]
                for j in (6, 25):
                    my_list1[j] = st2[j]

                my_list = "|".join(my_list0) + "\n" + "|".join(my_list1) + "\n" + "|".join(my_list2)
                temp_json = read_json('DATA/zamena.json')
                temp_json[zakaz] = [i, f"\n{my_list}\n"]
                write_json('DATA/zamena.json', temp_json)
                return


def change_namber_gmail(zakaz):
    shutil.copyfile(f'{put}{month}.RSB', 'DATA/gmail.txt')
    with open('DATA/gmail.txt', 'r') as f:
        for i in f.read().split('#@#')[1:]:
            s = i.strip().split('\n')[0:2]
            st1, st2 = s[0].split('|'), s[1].split('|')

            if st1[0] == zakaz:
                temp_json = read_json('DATA/zamena.json')
              
                my_json = [i.split("|") for i in temp_json[zakaz][1].strip().split("\n")]
                my_list0, my_list1, my_list2 = my_json[0], my_json[1], my_json[2]
                for j in (5, 7, 8, 9, 10, 14):
                    my_list0[j] = st1[j]
                my_list1[25] = st2[25]
                
                my_list = "|".join(my_list0) + "\n" + "|".join(my_list1) + "\n" + "|".join(my_list2)
                temp_json[zakaz] = [i, f"\n{my_list}\n"]
                
                write_json('DATA/zamena.json', temp_json)
                return
            

def order_number():
    return list(read_json('DATA/zamena.json').keys())


def delete_number(zakaz):
    if zakaz in order_number():
        temp_json = read_json('DATA/zamena.json')
        temp_json.pop(zakaz)
        write_json('DATA/zamena.json', temp_json)


if __name__ == '__main__':
    change_namber_gmail("1706")