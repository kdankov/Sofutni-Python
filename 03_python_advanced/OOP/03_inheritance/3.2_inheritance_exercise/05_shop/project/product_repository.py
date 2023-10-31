from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = [f'{product.name}: {product.quantity}' for product in self.products]

        return '\n'.join(result)

