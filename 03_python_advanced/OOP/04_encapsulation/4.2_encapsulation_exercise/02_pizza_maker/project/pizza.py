from project.topping import Topping
from project.dough import Dough
from typing import Dict


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str, float] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError('The name cannot be an empty string')

        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough: Dough):
        if dough is None:
            raise ValueError('You should add dough to the pizza')

        self.__dough = dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_number_of_toppings: int):
        if max_number_of_toppings <= 0:
            raise ValueError('The maximum number of toppings cannot be less or equal to zero')

        self.__max_number_of_toppings = max_number_of_toppings

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError('Not enough space for another topping')

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> float:
        total_weight = sum([weight for weight in self.toppings.values()]) + self.dough.weight

        return total_weight
