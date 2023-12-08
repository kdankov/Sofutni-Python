from typing import List

from project.table.table import Table
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.baked_food.baked_food import BakedFood
from project.baked_food.cake import Cake
from project.baked_food.bread import Bread


class Bakery:
    VALID_FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    VALID_DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    VALID_TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self.VALID_FOOD_TYPES:
            return

        if self.__get_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        new_food = self.VALID_FOOD_TYPES[food_type](name, price)
        self.food_menu.append(new_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in self.VALID_DRINK_TYPES:
            return

        if self.__get_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        new_drink = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
        self.drinks_menu.append(new_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.VALID_TABLE_TYPES:
            return

        if self.__get_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        new_table = self.VALID_TABLE_TYPES[table_type](table_number, capacity)
        self.tables_repository.append(new_table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__get_first_available_table(number_of_people)

        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args: str):
        table = self.__get_table_by_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered_food = [f"Table {table_number} ordered:"]
        not_existing_food = [f"{self.name} does not have in the menu:"]

        for food_name in args:
            current_food = self.__get_food_by_name(food_name)
            if not current_food:
                not_existing_food.append(food_name)
            else:
                table.order_food(current_food)
                ordered_food.append(current_food.__repr__())

        return "\n".join(ordered_food + not_existing_food)

    def order_drink(self, table_number: int, *args: str):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = [f"Table {table_number} ordered:"]
        not_existing_drinks = [f"{self.name} does not have in the menu:"]

        for drink_name in args:
            current_drink = self.__get_drink_by_name(drink_name)
            if not current_drink:
                not_existing_drinks.append(drink_name)
            else:
                table.order_drink(current_drink)
                ordered_drinks.append(current_drink.__repr__())

        return "\n".join(ordered_drinks + not_existing_drinks)

    def leave_table(self, table_number: int):
        table = self.__get_table_by_number(table_number)

        if not table:
            return

        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [table.free_table_info() for table in self.tables_repository if table.free_table_info() is not None]

        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __get_food_by_name(self, name):
        return next(filter(lambda f: f.name == name, self.food_menu), None)

    def __get_drink_by_name(self, name):
        return next(filter(lambda d: d.name == name, self.drinks_menu), None)

    def __get_table_by_number(self, number):
        return next(filter(lambda t: t.table_number == number, self.tables_repository), None)

    def __get_first_available_table(self, people_count):
        return next(filter(lambda t: not t.is_reserved and t.capacity >= people_count,
                           self.tables_repository), None)
