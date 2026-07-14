import os
import re
from config import put_555nc


def modify_file(filename, freza, speed):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified = False
    i = 0
    while i < len(lines):
        if 'TNO="{freza}"'.format(freza=freza) in lines[i]:
            # Ищем ближайший F_="X" (X=1-8) в последующих строках
            for j in range(i + 1, len(lines)):
                if re.search(r'F_="[1-8]"', lines[j]):
                    lines[j] = re.sub(r'(F_=)"[1-8]"', r'\1"{speed}"'.format(speed=speed), lines[j])
                    modified = True
                    i = j  # Перескакиваем обработанные строки
                    break
                # Прерываем поиск при новых параметрах или конце блока
                elif 'TNO="' in lines[j] or '\\' in lines[j]:
                    break
        i += 1

    if modified:
        with open(filename, 'w') as file:
            file.writelines(lines)
        print("Файл успешно изменён.")
    else:
        print("Изменений не требуется.")


def speed_change(order, freza, speed):
    if order in os.listdir(put_555nc):
        for i in os.listdir(f"{put_555nc}/{order}"):
            if i.endswith(".mpr"):
                modify_file(f"{put_555nc}/{order}/{i}", freza, speed)
        return "Скорость успешно изменена."
    else:
        return "Папка с таким названием отсутствует"


def podkladka(order, mun):
    if order in os.listdir(put_555nc):
        for i in os.listdir("{PATH}\\{order}".format(PATH=put_555nc, order=order)):
            if i.endswith(".mpr"):
                with open("{PATH}\\{order}\\{i}".format(PATH=put_555nc, order=order, i=i), "r") as file:
                    s = file.read().split('tPODK=')
                    podk = s[1].splitlines()
                    podk[0] = '"{mun}"'.format(mun=mun)
                    s = s[0] + 'tPODK=' + '\n'.join(podk)
                with open("{PATH}\\{order}\\{i}".format(PATH=put_555nc, order=order, i=i), "w") as file:
                    file.write(s)
        return f"Подклад заказа: {order[:4]} изменен на {mun}мм"
    else:
        return "Папка с таким названием отсутствует"


def add_nc_freza(order):
    order = order + "nc"
    if order in os.listdir(put_555nc):
        for i in os.listdir(f"{put_555nc}/{order}"):
            if i.endswith(".mpr"):
                with open(f"{put_555nc}/{order}/{i}", "r") as file:
                    with open("pl/15_nc.txt", "r") as file_132:
                        f_132 = file_132.read().replace('F_="8"', 'F_="4"')
                        if f_132.find("19.00+tPODK-7.2") != -1:
                            f_132 = f_132.replace('16.301', '19.301')
                        s = file.read().replace("/PLAST", f"{f_132}")

                with open(f"{put_555nc}/{order}/{i}", "w", encoding="utf-8") as file:
                    file.write(s)
        return f"В заказе: {order[:4]} добавлен 132-фреза"
    else:
        return "Папка с таким названием отсутствует"


if __name__ == '__main__':
    order = input("Введите номер заказа: ") + "nc"
    # mun = float(input("Введите толщину подкладки: ").replace(",", "."))

    print(add_nc_freza(order))

    # order = input("Введите номер заказа: ") + "nc"
    # freza = input("Введите номер фрезы: ")
    # speed = int(input("Введите скорость подачи: "))
    #
    # speed_change(order, freza, speed)
