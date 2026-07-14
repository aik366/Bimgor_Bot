
# with open('22.txt') as f:
# 	for i in [i.strip().split('\n')[:1] for i in f.read().split('#@#')[1:]]:
# 		if i[0].split('|')[13] not in "  .  ":
# 			print(i[0].split('|')[0], i[0].split('|')[13])

# with open('22.txt') as f:
# 	for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
# 		if i[1].split('|')[26] not in "":
# 			print(i[0].split('|')[0], i[1].split('|')[26])

# with open('22.txt') as f:
# 	for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
# 		st0, st1 = i[0].split('|'), i[1].split('|')
# 		if st1[28] not in "":
# 			print(st0[0], st1[28].strip().split(".")[0])

# with open('22.txt') as f:
# 	num = 0
# 	for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
# 		st0, st1 = i[0].split('|'), i[1].split('|')
# 		if st1[28] not in "":
# 			num += int(st1[28].strip().split(".")[0])
# 			print(st0[0], int(st1[28].strip().split(".")[0]))
# print(num)

with open('22.txt') as f:
	num, mesyac = 0, ["08", "09", "10"]
	for i in [i.strip().split('\n')[:2] for i in f.read().split('#@#')[1:]]:
		st0, st1 = i[0].split('|'), i[1].split('|')
		if st1[28] not in "" and st0[14] in mesyac:
			num += int(st1[28].strip().split(".")[0])
			print(st0[0], int(st1[28].strip().split(".")[0]))
print(num)



