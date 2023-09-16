text = tuple(input())

occ = {}

for ch in text:
    if ch not in occ:
        occ[ch] = text.count(ch)

sorted_occ = dict(sorted(occ.items()))

for key, value in sorted_occ.items():
    print(f'{key}: {value} time/s')
