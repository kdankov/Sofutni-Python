from project.drink.drink import Drink


class Tea(Drink):
    PRICE_CONST = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name=name, portion=portion, price=self.PRICE_CONST, brand=brand)
