from project.meals.meal import Meal


class Starter(Meal):
    TYPE = 'Starter'

    def __init__(self, name: str, price: float, quantity: int = 60):
        super().__init__(name, price, quantity)

    @property
    def meal_type(self):
        return Starter.TYPE
