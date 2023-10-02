def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''

    for name, quantities in sorted_dict:
        result += f'{name}\n'
        sorted_quantities = sorted(quantities, reverse=True)
        result += '\n'.join([str(x) for x in sorted_quantities])
        result += '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
