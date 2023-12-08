from project.drink.drink import Drink


class Water(Drink):
    PRICE_CONST = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name=name, portion=portion, price=self.PRICE_CONST, brand=brand)
