n = int(input())

periodic_table = set()

for _ in range(n):
    chemical_compounds = input().split()

    for compound in chemical_compounds:
        periodic_table.add(compound)

for comp in periodic_table:
    print(comp)
