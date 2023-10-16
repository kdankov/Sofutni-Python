def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []

    for product_name, price in args:
        if budget >= price:
            if product_name in grocery_list and product_name not in bought_products:
                bought_products.append(product_name)
                budget -= price
                grocery_list.remove(product_name)
        else:
            break

    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f'You did not buy all the products. Missing products: {", ".join(grocery_list)}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print()

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print()

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

print()