def read_intcode(i, ps):
    for p, s in ps.items():
        i[p] = s
    for g in range(0, int(len(i) / 4)):
        b = i[g * 4:g * 4 + 4]
        if b[0] == 99:
            break
        elif b[0] not in [1, 2]:
            return '1202 program alarm', i
        i[b[3]] = i[b[1]] + i[b[2]] if b[0] == 1 else i[b[1]] * i[b[2]] if b[0] == 2 else i[b[3]]
    return 'OK', i
