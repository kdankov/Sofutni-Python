def shopping_cart(*args):
    products_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    result = []

    for el in args:
        if el == 'Stop':
            break

        meal_type = el[0]
        meal_product = el[1]

        if meal_product not in products_dict[meal_type]:
            if meal_type == 'Soup' and len(products_dict['Soup']) < 3:
                products_dict[meal_type].append(meal_product)
            elif meal_type == 'Pizza' and len(products_dict['Pizza']) < 4:
                products_dict[meal_type].append(meal_product)
            elif meal_type == 'Dessert' and len(products_dict['Dessert']) < 2:
                products_dict[meal_type].append(meal_product)

    for value in products_dict.values():
        if value:
            break
    else:
        return 'No products in the cart!'

    sorted_products = sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for m_type, m_products in sorted_products:
        result.append(f'{m_type}:')
        for product in sorted(m_products):
            result.append(f' - {product}')

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
