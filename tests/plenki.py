def main():
    with open('22.txt') as f:
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
            s += f'{k} {round(v, 1)}\n'
        print(s)
        with open('plenki.txt', 'w') as f:
            f.write(s)


if __name__ == '__main__':
    main()
