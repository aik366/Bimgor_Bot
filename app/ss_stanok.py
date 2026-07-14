import os
import re
from config import put_555ss


def modify_file(filename, freza, speed):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified = False
    i = 0
    while i < len(lines):
        if f'TNO="{freza}"' in lines[i]:
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
    if order in os.listdir(put_555ss):
        for i in os.listdir(f"{put_555ss}\\{order}"):
            if i.endswith(".mpr"):
                modify_file(f"{put_555ss}\\{order}\\{i}", freza, speed)
        return "Скорость успешно изменена."
    else:
        return "Не удалось найти папку с заказом."


def add_ss_freza(order):
    order = order + "h"
    if order in os.listdir(put_555ss):
        for i in os.listdir(f"{put_555ss}/{order}"):
            if i.endswith(".mpr"):
                with open(f"{put_555ss}/{order}/{i}", "r") as file:
                    with open("pl/15_ss.txt", "r") as file_132:
                        f_132 = file_132.read().replace('t-16.7', '-2')
                        s = file.read().replace("/PLAST", f"{f_132}")

                with open(f"{put_555ss}/{order}/{i}", "w", encoding="utf-8") as file:
                    file.write(s)
        return f"В заказе: {order[:4]} добавлен 132-фреза"
    else:
        return "Папка с таким названием отсутствует"


if __name__ == '__main__':
    order = input("Введите номер заказа: ") + "h"
    # mun = float(input("Введите толщину подкладки: ").replace(",", "."))

    print(add_ss_freza(order))
