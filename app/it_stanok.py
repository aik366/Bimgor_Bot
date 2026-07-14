import os
import re
from config import put_555it


def add_it_freza(order):
    order = order + "it"
    if order in os.listdir(put_555it):
        for i in os.listdir(f"{put_555it}/{order}"):
            if i.endswith(".bpp"):
                with open(f"{put_555it}/{order}/{i}", "r") as file:
                    with open("pl/132_it.txt", "r") as file_132:
                        s = file.read().replace("' kray", f"{file_132.read()}")

                with open(f"{put_555it}/{order}/{i}", "w", encoding="utf-8") as file:
                    file.write(s)
        return f"В заказе: {order[:4]} добавлен 132-фреза"
    else:
        return "Папка с таким названием отсутствует"


def replace_frezer(line, target_route, new_value):
    # Проверяем, начинается ли строка с шаблона (игнорируя пробелы)
    pattern = rf'\s*@ ROUT, 0 : "{target_route}"'
    if re.match(pattern, line):
        parts = line.split(',')
        if len(parts) > 6:
            # Заменяем 6-й элемент (индекс 5) на новое значение
            parts[5] = re.sub(r'\S+', str(new_value), parts[5])
            return ','.join(parts)
    return line


def replace_tolshina(path_file, number, new_value):
    with open(path_file, "r") as file:
        lines = file.readlines()
    # Ищем и заменяем нужную строку
    for i, line in enumerate(lines):
        if line.startswith("PAN=LPZ|"):
            parts = line.split("|")
            t_volue = float(parts[1])
            if (t_volue-1.0) < number < (t_volue+1.0):
                # Заменяем значение (второй элемент после разделителя)
                parts[1] = str(new_value)
                lines[i] = "|".join(parts)
    # Перезаписываем файл
    with open(path_file, "w") as file:
        file.writelines(lines)


def value_freza(order, freza, value):
    order = order + "it"
    if order in os.listdir(put_555it):
        for i in os.listdir(f"{put_555it}/{order}"):
            if i.endswith(".bpp"):
                with open(f"{put_555it}/{order}/{i}", "r") as file:
                    lines = file.readlines()

                new_lines = []
                for line in lines:
                    # if "PAN=LPZ|16.2" in line:
                    #     new_lines = lines
                    #     break
                    new_lines.append(replace_frezer(line, freza, value))

                with open(f"{put_555it}/{order}/{i}", "w", encoding="utf-8") as file:
                    file.writelines(new_lines)
        return f"Заказ: {order[:4]} изменился"
    else:
        return "Папка с таким названием отсутствует"


def value_tolshina(order, number, new_value):
    order = order + "it"
    if order in os.listdir(put_555it):
        for i in os.listdir(f"{put_555it}/{order}"):
            if i.endswith(".bpp"):
                path_file = f"{put_555it}/{order}/{i}"
                replace_tolshina(path_file, number, new_value)
        return f"Заказ: {order[:4]} изменился"
    else:
        return "Папка с таким названием отсутствует"


if __name__ == '__main__':
    # order = input("Введите номер заказа: ") + "it"
    # mun = float(input("Введите толщину подкладки: ").replace(",", "."))

    print(value_tolshina("2987", "18.22"))
