import json


def plenka_json_group():  # Пленка по группам запись
    with open("data_plenka.txt", "r", encoding="UTF-8") as file:
        plenka = [i.split("|")[:3] for i in file.read().strip().split("\n")]

    json_plenka = {}
    for pl in plenka:
        if pl[2] not in json_plenka:
            json_plenka[pl[2]] = [f'{pl[1].capitalize()}|{pl[0]}']
        else:
            json_plenka[pl[2]].append(f'{pl[1].capitalize()}|{pl[0]}')

    with open("plenka_group.json", "w", encoding="UTF-8") as file:
        content = json.dumps(json_plenka, ensure_ascii=False)
        file.write(content)


def plenka_json():  # Пленка по группам запись
    with open("data_plenka.txt", "r", encoding="UTF-8") as file:
        plenka = [i.split("|")[:3] for i in file.read().strip().split("\n")]

    json_plenka = {}
    for pl in plenka:
        json_plenka[pl[0]] = [pl[1].capitalize(), pl[2]]

    with open("plenka.json", "w", encoding="UTF-8") as file:
        content = json.dumps(json_plenka, ensure_ascii=False)
        file.write(content)


def fasad_json():  # фасад запись
    with open("data_fasad.txt", "r", encoding="UTF-8") as file:
        fasad = [i.split("|") for i in file.read().strip().split("\n")]

    json_fasad = {}
    for fs in fasad:
        json_fasad[fs[0]] = int(fs[19])
    with open("fasad.json", "w", encoding="UTF-8") as file:
        content = json.dumps(json_fasad, ensure_ascii=False)
        file.write(content)


def print_plenka_group(group):
    s = ''
    with open('price/plenka_group.json', 'r', encoding='UTF-8') as file:
        js_plenka_group = json.loads(file.read())
        for i in sorted(js_plenka_group[group]):
            k = i.split('|')
            s += f"{k[1]}: {k[0]}|гр.{group}\n"
        return s


def print_plenka_number():
    s = ''
    with open('price/plenka.json', 'r', encoding='UTF-8') as file:
        js_plenka_number = json.loads(file.read())
        for k, v in js_plenka_number.items():
            s += f"{k}: {v[0]}|гр.{v[1]}\n"
        return s


def print_plenka_sort():
    s = ''
    with open('price/plenka.json', 'r', encoding='UTF-8') as file:
        js_plenka_sort = json.loads(file.read())
        js_plenka_sort = dict(sorted(js_plenka_sort.items(), key=lambda item: item[1][0]))
        for k, v in js_plenka_sort.items():
            s += f"{k}: {v[0]}|гр.{v[1]}\n"
        return s


def price_plenka(group):
    with open('price/data.json', 'r', encoding='UTF-8') as file:
        js_plenka = json.loads(file.read())
        return js_plenka['plenka'][group]


def price_tolshina(number):
    with open('price/data.json', 'r', encoding='UTF-8') as file:
        js_tolshina = json.loads(file.read())
        return js_tolshina['tolshina'][number]


def price_fasad(number):
    with open('price/fasad.json', 'r', encoding='UTF-8') as file:
        js_fasad = json.loads(file.read())
        return js_fasad[number]


def price_summ(plenka, tolshina, fasad):
    if fasad == '16':
        return price_plenka(plenka) + price_tolshina(tolshina) + price_fasad(fasad)
    return price_plenka(plenka) + price_tolshina(tolshina) + price_fasad(fasad) + 450


if __name__ == '__main__':
    # plenka_json()
    # plenka_json_group()
    # fasad_json()
    # print_plenka_sort()
    print(print_plenka_group('4'))
    pass
