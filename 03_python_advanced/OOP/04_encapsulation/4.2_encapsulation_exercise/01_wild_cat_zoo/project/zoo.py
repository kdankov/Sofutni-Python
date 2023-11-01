from typing import List
from project.animal import Animal
from project.worker import Worker

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return 'Not enough budget'

        if len(self.animals) >= self.__animal_capacity:
            return 'Not enough space for animal'

        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f'There is no {worker_name} in the zoo'

        self.workers.remove(worker)
        return f'{worker_name} fired successfully'

    def pay_workers(self) -> str:
        salaries_sum = sum([worker.salary for worker in self.workers])

        if salaries_sum > self.__budget:
            return 'You have no budget to pay your workers. They are unhappy'

        self.__budget -= salaries_sum
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self) -> str:
        taxes_sum = sum([animal.money_for_care for animal in self.animals])

        if taxes_sum > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= taxes_sum
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"

        for animal_type in ["Lion", "Tiger", "Cheetah"]:
            animals = [a for a in self.animals if a.__class__.__name__ == animal_type]
            result += f"\n----- {len(animals)} {animal_type}s:"
            for current_animal in animals:
                result += f"\n{current_animal.__repr__()}"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"

        for worker_type in ["Keeper", "Caretaker", "Vet"]:
            workers = [a for a in self.workers if a.__class__.__name__ == worker_type]
            result += f"\n----- {len(workers)} {worker_type}s:"
            for current_worker in workers:
                result += f"\n{current_worker.__repr__()}"
        return result
