import os

# path = "../rs"
# path = r"\\BS1000046997\Users\Public\Bimgor"

# s1 = '8000, "157", 103, 1, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 5, 0, 20, 80, 60, 0, "", "", "ROUT", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2000, 0, 0.1, 0, 0, 0, 1, 30'
# s2 = '8000, "157", 103, 1, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 5, 0, 20, 80, 60, 0, "", "", "ROUT", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2000, 0, 0.1, 0, 0, 0, 1, 50'

# s1 = '2000, 0, 0.1, 0, 0, 0, 1, 70'
# s2 = '2000, 0, 0.1, 0, 0, 0, 1, 90'



def it_stanok():
    path = r"\\BS1000046997\Users\Public\Bimgor"
    s1 = '@ ROUT, 0 : "158", 0, "1", 0, 14.1'
    s2 = '@ ROUT, 0 : "158", 0, "1", 0, 17.501'

    my_dir, my_file = 0, 0
    for i in os.listdir(path):
        if i[-2:] == 'it':
            my_dir += 1
            for j in os.listdir(f'{path}/{i}'):
                if j[-4:] == ".bpp":
                    my_file += 1
                    with open(f'{path}/{i}/{j}', 'r') as file:
                        s = file.read().replace(s1, s2)
                    with open(f'{path}/{i}/{j}', 'w') as fl:
                        fl.write(s)

    print(f'Папок: {my_dir}\nФайлов: {my_file}')


def nc_stanok():
    path = r"\\BHC111\bimgor"
    s1 = 'ZA="t-14.4"'
    s2 = 'ZA="t-15.001"'
    my_dir, my_file = 0, 0
    for i in os.listdir(path):
        if i[-2:] == 'nc':
            my_dir += 1
            for j in os.listdir(f'{path}/{i}'):
                if j[-4:] == ".mpr":
                    my_file += 1
                    with open(f'{path}/{i}/{j}', 'r') as file:
                        s = file.read().replace(s1, s2)
                    with open(f'{path}/{i}/{j}', 'w') as fl:
                        fl.write(s)

    print(f'Папок: {my_dir}\nФайлов: {my_file}')

if __name__ == '__main__':
    pass
    # it_stanok()
    nc_stanok()