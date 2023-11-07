from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from typing import List


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def find_object_by_id(object_id, array):
        for obj in array:
            if obj.id == object_id:
                return obj

    def subscription_info(self, subscription_id: int):
        subscription = self.find_object_by_id(subscription_id, self.subscriptions)
        customer = self.find_object_by_id(subscription.customer_id, self.customers)
        trainer = self.find_object_by_id(subscription.trainer_id, self.trainers)
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipment = self.find_object_by_id(plan.equipment_id, self.equipment)

        result = (f"{subscription}\n"
                  f"{customer}\n"
                  f"{trainer}\n"
                  f"{equipment}\n"
                  f"{plan}\n")

        return result
