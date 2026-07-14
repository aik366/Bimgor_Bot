# with open('22.txt') as f:
#     num, mesyac = 0, ["08", "09", "10"]
#     for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
#         st0, st1 = i[0].split('|'), i[1].split('|')
#         if st1[28] not in "" and st0[14] in mesyac:
#             num += int(st1[28].strip().split(".")[0])
#             print(st0[0], int(st1[28].strip().split(".")[0]))
# print(num)

with open('22.txt') as f:
    for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
        st0, st1 = i[0].split('|'), i[1].split('|')
        if st0[1].strip() == "Сердюченко" and st1[25][5] == "1":
            print(st0[16][:4], st1[25][5])

