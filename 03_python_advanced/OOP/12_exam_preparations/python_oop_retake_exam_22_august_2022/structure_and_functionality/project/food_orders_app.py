from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter
from project.client import Client
from project.meals.meal import Meal
from copy import copy
from typing import List


class FoodOrdersApp:
    MEAL_TYPES = {
        "Dessert": Dessert,
        "MainDish": MainDish,
        "Starter": Starter}

    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        if self._get_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.MEAL_TYPES.keys():
                self.menu.append(meal)

    def show_menu(self):
        self._check_menu_ready()
        return "\n".join(list(meal.details() for meal in self.menu))

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_menu_ready()

        client = self._get_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self._get_client_by_phone_number(client_phone_number)

        for meal_name, ordered_quantity in meal_names_and_quantities.items():
            meal = self._get_meal_by_name(meal_name)
            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < ordered_quantity:
                raise Exception(f"Not enough quantity of {meal.meal_type}: {meal_name}!")

        for meal_name, ordered_quantity in meal_names_and_quantities.items():
            meal = self._get_meal_by_name(meal_name)
            meal.quantity -= ordered_quantity

            client_meal = copy(meal)
            client_meal.quantity = ordered_quantity
            client.shopping_cart.append(client_meal)
            client.bill += client_meal.price * client_meal.quantity

        return (f"Client {client_phone_number} successfully ordered "
                f"{', '.join(n.name for n in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for client_meal in client.shopping_cart:
            meal = self._get_meal_by_name(client_meal.name)
            meal.quantity += client_meal.quantity

        client.bill = 0
        client.shopping_cart.clear()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart.clear()
        self.receipt_id += 1

        return (f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def _get_client_by_phone_number(self, phone_number):
        return next((c for c in self.clients_list if c.phone_number == phone_number), None)

    def _get_meal_by_name(self, meal_name):
        return next((m for m in self.menu if m.name == meal_name), None)

    def _check_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
